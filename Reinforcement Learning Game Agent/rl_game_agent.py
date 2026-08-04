"""
Reinforcement Learning Game Agent
------------------------------------
A tabular Q-learning agent learns to navigate a grid world from START to
GOAL while avoiding traps, purely through trial and error (reward signals),
with no hardcoded path. Training runs instantly in the terminal; then a
Pygame window replays the trained agent's learned policy.

Controls (during replay window):
  SPACE -> replay another episode with the learned (greedy) policy
  T     -> retrain from scratch
  ESC   -> quit
"""

import random
import pygame

COLS, ROWS = 8, 6
CELL = 80
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL + 50

START = (0, 0)
GOAL = (COLS - 1, ROWS - 1)
TRAPS = {(2, 1), (2, 2), (2, 3), (5, 4), (5, 2), (5, 3)}

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
DELTA = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

# Hyperparameters
ALPHA = 0.15       # learning rate
GAMMA = 0.95        # discount factor
EPISODES = 3000
MAX_STEPS = 100

BLACK = (20, 20, 20)
WHITE = (240, 240, 240)
GREY = (80, 80, 80)
GREEN = (60, 190, 100)
RED = (210, 60, 60)
BLUE = (70, 130, 220)
YELLOW = (240, 220, 80)


def step(state, action):
    dx, dy = DELTA[action]
    nx, ny = state[0] + dx, state[1] + dy
    if not (0 <= nx < COLS and 0 <= ny < ROWS):
        nx, ny = state  # bump into wall, stay put

    if (nx, ny) in TRAPS:
        return (nx, ny), -25, True
    if (nx, ny) == GOAL:
        return (nx, ny), 25, True
    return (nx, ny), -1, False  # small step penalty to encourage short paths


def train():
    Q = {(c, r): {a: 0.0 for a in ACTIONS} for c in range(COLS) for r in range(ROWS)}
    epsilon = 1.0

    for ep in range(EPISODES):
        state = START
        for _ in range(MAX_STEPS):
            if random.random() < epsilon:
                action = random.choice(ACTIONS)
            else:
                action = max(Q[state], key=Q[state].get)

            next_state, reward, done = step(state, action)
            best_next = max(Q[next_state].values())
            Q[state][action] += ALPHA * (reward + GAMMA * best_next - Q[state][action])

            state = next_state
            if done:
                break

        epsilon = max(0.05, epsilon * 0.997)

    return Q


def greedy_path(Q):
    state = START
    path = [state]
    for _ in range(MAX_STEPS):
        action = max(Q[state], key=Q[state].get)
        state, _, done = step(state, action)
        path.append(state)
        if done:
            break
    return path


def draw(win, font, path_so_far, Q, episode_label):
    win.fill(BLACK)
    for c in range(COLS):
        for r in range(ROWS):
            rect = (c * CELL, r * CELL, CELL - 1, CELL - 1)
            color = GREY
            if (c, r) in TRAPS:
                color = RED
            elif (c, r) == GOAL:
                color = GREEN
            elif (c, r) == START:
                color = BLUE
            pygame.draw.rect(win, color, rect)

    for (c, r) in path_so_far:
        cx, cy = c * CELL + CELL // 2, r * CELL + CELL // 2
        pygame.draw.circle(win, YELLOW, (cx, cy), 8)

    label = font.render(episode_label, True, WHITE)
    win.blit(label, (10, HEIGHT - 35))
    pygame.display.update()


def main():
    print("Training Q-learning agent...")
    Q = train()
    print("Training complete.")

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Reinforcement Learning Game Agent")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 18)

    path = greedy_path(Q)
    reveal_index = 0
    running = True

    while running:
        clock.tick(6)  # slow reveal speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    path = greedy_path(Q)
                    reveal_index = 0
                if event.key == pygame.K_t:
                    print("Retraining...")
                    Q = train()
                    path = greedy_path(Q)
                    reveal_index = 0
                    print("Retraining complete.")

        if reveal_index < len(path):
            reveal_index += 1

        status = "Reached goal!" if path[-1] == GOAL else "Fell into a trap"
        label = f"Learned policy — {status}  |  SPACE=replay, T=retrain, ESC=quit"
        draw(win, font, path[:reveal_index], Q, label)

    pygame.quit()


if __name__ == "__main__":
    main()
