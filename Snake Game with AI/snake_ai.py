"""
Snake Game with AI
-------------------
The snake is controlled by an AI that uses Breadth-First Search (BFS) to
find the shortest path to the food each frame, avoiding its own body and
walls. If no safe path to food exists, it falls back to a move that keeps
it alive as long as possible.

Controls:
  A -> toggle AI control on/off
  Arrow keys -> manual control (when AI is off)
  R -> restart
"""

import pygame
import random
from collections import deque

CELL = 20
COLS, ROWS = 30, 24
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL
FPS = 12

BLACK = (15, 15, 15)
GREEN = (60, 200, 100)
DARK_GREEN = (30, 140, 70)
RED = (220, 70, 70)
WHITE = (240, 240, 240)

DIRS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
OPPOSITE = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}


def new_food(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


def bfs_path(start, goal, snake_body):
    """Find shortest path from start to goal avoiding the snake body."""
    blocked = set(snake_body)
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for dx, dy in DIRS.values():
            nxt = (current[0] + dx, current[1] + dy)
            if (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS
                    and nxt not in blocked and nxt not in came_from):
                came_from[nxt] = current
                queue.append(nxt)

    if goal not in came_from:
        return None

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path


def direction_to(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    for name, (ddx, ddy) in DIRS.items():
        if (ddx, ddy) == (dx, dy):
            return name
    return None


def ai_choose_direction(snake, direction, food):
    head = snake[0]
    body_without_tail = snake[:-1]  # tail cell will move away, so it's safe

    path = bfs_path(head, food, body_without_tail)
    if path:
        return direction_to(head, path[0])

    # Fallback: pick any safe move that doesn't immediately trap the snake
    best = None
    best_space = -1
    for name, (dx, dy) in DIRS.items():
        if name == OPPOSITE.get(direction):
            continue
        nxt = (head[0] + dx, head[1] + dy)
        if not (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS):
            continue
        if nxt in body_without_tail:
            continue
        # measure reachable open space from this move (flood fill size)
        space = flood_fill_size(nxt, body_without_tail)
        if space > best_space:
            best_space = space
            best = name

    return best or direction


def flood_fill_size(start, blocked_cells, limit=200):
    blocked = set(blocked_cells)
    seen = {start}
    queue = deque([start])
    count = 0
    while queue and count < limit:
        cur = queue.popleft()
        count += 1
        for dx, dy in DIRS.values():
            nxt = (cur[0] + dx, cur[1] + dy)
            if (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS
                    and nxt not in blocked and nxt not in seen):
                seen.add(nxt)
                queue.append(nxt)
    return count


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake with AI")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 20)

    def reset():
        snake = [(COLS // 2, ROWS // 2)]
        direction = 'RIGHT'
        food = new_food(snake)
        return snake, direction, food

    snake, direction, food = reset()
    ai_enabled = True
    score = 0
    game_over = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    ai_enabled = not ai_enabled
                if event.key == pygame.K_r:
                    snake, direction, food = reset()
                    score = 0
                    game_over = False
                if not ai_enabled and not game_over:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

        if not game_over:
            if ai_enabled:
                direction = ai_choose_direction(snake, direction, food)

            dx, dy = DIRS[direction]
            head = (snake[0][0] + dx, snake[0][1] + dy)

            if (head in snake or not (0 <= head[0] < COLS) or not (0 <= head[1] < ROWS)):
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = new_food(snake)
                else:
                    snake.pop()

        # draw
        win.fill(BLACK)
        for i, seg in enumerate(snake):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(win, color, (seg[0] * CELL, seg[1] * CELL, CELL - 1, CELL - 1))
        pygame.draw.rect(win, RED, (food[0] * CELL, food[1] * CELL, CELL - 1, CELL - 1))

        mode = "AI" if ai_enabled else "Manual"
        text = font.render(f"Score: {score}   Mode: {mode} (press A to toggle)", True, WHITE)
        win.blit(text, (10, HEIGHT - 28))

        if game_over:
            over_text = font.render("Game Over - press R to restart", True, WHITE)
            win.blit(over_text, (WIDTH // 2 - 140, HEIGHT // 2))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
