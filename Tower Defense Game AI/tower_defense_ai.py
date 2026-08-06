"""
Tower Defense Game AI
------------------------
Enemies use BFS to find the shortest path through a grid maze toward your
base, automatically recalculating if you place a tower that blocks their
route. Towers automatically target and shoot the nearest enemy in range.

Controls:
  Left click on grid -> place a tower (costs gold)
  SPACE               -> start next wave early
  R                   -> restart
"""

import pygame
import math
from collections import deque

CELL = 32
COLS, ROWS = 20, 15
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL + 60
FPS = 60

BLACK = (20, 20, 20)
GREY = (70, 70, 70)
LIGHT = (210, 210, 210)
GREEN = (60, 180, 90)
RED = (220, 70, 70)
BLUE = (70, 130, 220)
YELLOW = (240, 220, 80)
WHITE = (245, 245, 245)

START = (0, ROWS // 2)
END = (COLS - 1, ROWS // 2)

TOWER_COST = 50
TOWER_RANGE = 3 * CELL
TOWER_DAMAGE = 12
TOWER_FIRE_RATE = 20  # frames between shots


def bfs_path(blocked, start, end):
    queue = deque([start])
    came_from = {start: None}
    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt = (cur[0] + dx, cur[1] + dy)
            if (0 <= nxt[0] < COLS and 0 <= nxt[1] < ROWS
                    and nxt not in blocked and nxt not in came_from):
                came_from[nxt] = cur
                queue.append(nxt)
    if end not in came_from:
        return None
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path


class Enemy:
    def __init__(self, path, hp, speed):
        self.path = path
        self.progress = 0.0  # index along path (float)
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.alive = True
        self.reached_end = False

    def pos(self):
        idx = int(self.progress)
        if idx >= len(self.path) - 1:
            return self.grid_to_px(self.path[-1])
        a = self.grid_to_px(self.path[idx])
        b = self.grid_to_px(self.path[idx + 1])
        t = self.progress - idx
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

    @staticmethod
    def grid_to_px(cell):
        return (cell[0] * CELL + CELL / 2, cell[1] * CELL + CELL / 2)

    def update(self):
        self.progress += self.speed
        if self.progress >= len(self.path) - 1:
            self.reached_end = True

    def draw(self, win):
        x, y = self.pos()
        pygame.draw.circle(win, RED, (int(x), int(y)), 10)
        # hp bar
        pygame.draw.rect(win, BLACK, (x - 12, y - 18, 24, 4))
        pygame.draw.rect(win, GREEN, (x - 12, y - 18, 24 * (self.hp / self.max_hp), 4))


class Tower:
    def __init__(self, cell):
        self.cell = cell
        self.px = Enemy.grid_to_px(cell)
        self.cooldown = 0

    def update(self, enemies):
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        target = None
        best_dist = TOWER_RANGE
        for e in enemies:
            if not e.alive:
                continue
            ex, ey = e.pos()
            d = math.hypot(ex - self.px[0], ey - self.px[1])
            if d <= best_dist:
                best_dist = d
                target = e
        if target:
            target.hp -= TOWER_DAMAGE
            if target.hp <= 0:
                target.alive = False
            self.cooldown = TOWER_FIRE_RATE

    def draw(self, win):
        pygame.draw.circle(win, BLUE, (int(self.px[0]), int(self.px[1])), 12)
        pygame.draw.circle(win, LIGHT, (int(self.px[0]), int(self.px[1])), TOWER_RANGE, 1)


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense AI")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 20)

    def reset():
        return {
            'towers': [],
            'enemies': [],
            'gold': 150,
            'lives': 10,
            'wave': 0,
            'spawn_timer': 0,
            'spawned_this_wave': 0,
            'game_over': False,
        }

    state = reset()

    def blocked_cells():
        return {t.cell for t in state['towers']}

    def recompute_paths():
        blocked = blocked_cells()
        path = bfs_path(blocked, START, END)
        for e in state['enemies']:
            if e.alive:
                # keep progress roughly, just recompute path from current cell forward
                new_path = bfs_path(blocked, (int(e.pos()[0] // CELL), int(e.pos()[1] // CELL)), END)
                if new_path:
                    e.path = new_path
                    e.progress = 0
        return path

    def start_wave():
        state['wave'] += 1
        state['spawned_this_wave'] = 0
        state['spawn_timer'] = 0

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    state = reset()
                if event.key == pygame.K_SPACE and state['spawned_this_wave'] == 0 and not state['game_over']:
                    start_wave()
            if event.type == pygame.MOUSEBUTTONDOWN and not state['game_over']:
                mx, my = pygame.mouse.get_pos()
                cell = (mx // CELL, my // CELL)
                if (0 <= cell[0] < COLS and 0 <= cell[1] < ROWS
                        and cell not in (START, END)
                        and cell not in blocked_cells()
                        and state['gold'] >= TOWER_COST):
                    trial_blocked = blocked_cells() | {cell}
                    if bfs_path(trial_blocked, START, END) is not None:
                        state['towers'].append(Tower(cell))
                        state['gold'] -= TOWER_COST
                        recompute_paths()

        if not state['game_over']:
            if state['wave'] == 0:
                start_wave()

            enemies_per_wave = 5 + state['wave']
            state['spawn_timer'] += 1
            if state['spawned_this_wave'] < enemies_per_wave and state['spawn_timer'] % 45 == 0:
                path = bfs_path(blocked_cells(), START, END)
                if path:
                    hp = 30 + state['wave'] * 8
                    speed = 0.04 + min(state['wave'] * 0.002, 0.03)
                    state['enemies'].append(Enemy(path, hp, speed))
                    state['spawned_this_wave'] += 1

            for e in state['enemies']:
                if e.alive and not e.reached_end:
                    e.update()
                    if e.reached_end:
                        state['lives'] -= 1
                        e.alive = False

            for t in state['towers']:
                t.update(state['enemies'])

            for e in state['enemies']:
                if not e.alive and not e.reached_end:
                    state['gold'] += 10

            state['enemies'] = [e for e in state['enemies'] if e.alive]

            if state['lives'] <= 0:
                state['game_over'] = True

            if (state['spawned_this_wave'] >= enemies_per_wave and not state['enemies']):
                state['gold'] += 30
                start_wave()

        # draw
        win.fill(BLACK)
        for r in range(ROWS):
            for c in range(COLS):
                rect = (c * CELL, r * CELL, CELL - 1, CELL - 1)
                pygame.draw.rect(win, GREY if (r + c) % 2 == 0 else (60, 60, 60), rect)
        sx, sy = START
        ex, ey = END
        pygame.draw.rect(win, GREEN, (sx * CELL, sy * CELL, CELL, CELL))
        pygame.draw.rect(win, RED, (ex * CELL, ey * CELL, CELL, CELL))

        for t in state['towers']:
            t.draw(win)
        for e in state['enemies']:
            e.draw(win)

        hud = font.render(
            f"Gold: {state['gold']}   Lives: {state['lives']}   Wave: {state['wave']}   "
            f"(click grid = place tower, SPACE = next wave)", True, WHITE)
        win.blit(hud, (10, HEIGHT - 40))

        if state['game_over']:
            msg = font.render("GAME OVER - press R to restart", True, RED)
            win.blit(msg, (WIDTH // 2 - 140, HEIGHT // 2))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
