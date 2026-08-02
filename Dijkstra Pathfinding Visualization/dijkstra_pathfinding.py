"""
Dijkstra Pathfinding Visualization
-----------------------------------
Click to place a START node, an END node, and then walls (obstacles).
Press SPACE to run Dijkstra's algorithm and watch it search for the
shortest path. Press C to clear the grid.

Controls:
  Left click            -> place start, then end, then walls
  Right click            -> erase a cell
  SPACE                   -> run Dijkstra
  C                       -> clear grid
"""

import pygame
import heapq

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREY = (200, 200, 200)
GREEN = (60, 200, 100)
RED = (220, 70, 70)
BLUE = (70, 130, 220)
YELLOW = (240, 220, 80)
PURPLE = (150, 90, 220)


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_wall = False
        self.is_start = False
        self.is_end = False

    def pos(self):
        return self.row, self.col

    def neighbors(self, grid):
        result = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < ROWS and 0 <= c < COLS and not grid[r][c].is_wall:
                result.append(grid[r][c])
        return result


def make_grid():
    return [[Node(r, c) for c in range(COLS)] for r in range(ROWS)]


def draw_grid_lines(win):
    for i in range(ROWS + 1):
        pygame.draw.line(win, GREY, (0, i * CELL), (WIDTH, i * CELL))
    for j in range(COLS + 1):
        pygame.draw.line(win, GREY, (j * CELL, 0), (j * CELL, HEIGHT))


def draw(win, grid, visited=set(), path=set()):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            x, y = node.col * CELL, node.row * CELL
            color = WHITE
            if node.is_wall:
                color = BLACK
            elif node.is_start:
                color = GREEN
            elif node.is_end:
                color = RED
            elif node.pos() in path:
                color = YELLOW
            elif node.pos() in visited:
                color = BLUE
            pygame.draw.rect(win, color, (x, y, CELL, CELL))
    draw_grid_lines(win)
    pygame.display.update()


def dijkstra(win, grid, start, end):
    dist = {start.pos(): 0}
    prev = {}
    visited_order = set()
    pq = [(0, id(start), start)]
    visited_set = set()

    while pq:
        d, _, current = heapq.heappop(pq)
        if current.pos() in visited_set:
            continue
        visited_set.add(current.pos())
        visited_order.add(current.pos())

        # animate
        if current != start and current != end:
            draw(win, grid, visited=visited_order)
            pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if current == end:
            break

        for neighbor in current.neighbors(grid):
            new_dist = d + 1
            if new_dist < dist.get(neighbor.pos(), float('inf')):
                dist[neighbor.pos()] = new_dist
                prev[neighbor.pos()] = current.pos()
                heapq.heappush(pq, (new_dist, id(neighbor), neighbor))

    # reconstruct path
    path = set()
    if end.pos() in prev or end == start:
        cur = end.pos()
        while cur in prev:
            path.add(cur)
            cur = prev[cur]
        path.add(start.pos())

    draw(win, grid, visited=visited_order, path=path)


def get_clicked_pos(pos):
    x, y = pos
    return y // CELL, x // CELL


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dijkstra Pathfinding Visualization")

    grid = make_grid()
    start = None
    end = None
    running = True

    while running:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:  # left click
                row, col = get_clicked_pos(pygame.mouse.get_pos())
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.is_start = True
                elif not end and node != start:
                    end = node
                    end.is_end = True
                elif node != start and node != end:
                    node.is_wall = True

            elif pygame.mouse.get_pressed()[2]:  # right click
                row, col = get_clicked_pos(pygame.mouse.get_pos())
                node = grid[row][col]
                node.is_wall = False
                if node == start:
                    start = None
                    node.is_start = False
                elif node == end:
                    end = None
                    node.is_end = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    dijkstra(win, grid, start, end)
                if event.key == pygame.K_c:
                    start, end = None, None
                    grid = make_grid()

    pygame.quit()


if __name__ == "__main__":
    main()
