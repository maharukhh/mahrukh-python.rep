import pygame
import heapq
pygame.init()
W = 500
ROWS = 10
SIZE = W // ROWS
screen = pygame.display.set_mode((W, W))
pygame.display.set_caption("A* Fixed Path")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
grid = [[0]*ROWS for _ in range(ROWS)]
start = (9, 0)
goal = (0, 9)
obstacles = [
    (1,1),(1,2),(1,3),(2,3),(3,3),
    (4,3),(5,3),(6,3),(6,4),(6,5),
    (7,5),(8,5),(8,6),(7,7),(6,7),
    (5,7),(4,7),(3,7),(2,7),(1,7)
]
for x, y in obstacles:
    grid[x][y] = 1
def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
def astar():
    pq = [(h(start, goal), 0, start)]  # (f, g, node)
    came = {}
    g = {start: 0}
    visited = set()
    while pq:
        f, cost, cur = heapq.heappop(pq)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == goal:
            path = []
            while cur in came:
                path.append(cur)
                cur = came[cur]
            path.append(start)
            return path[::-1]
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = cur[0]+dx, cur[1]+dy
            if 0 <= nx < ROWS and 0 <= ny < ROWS:
                if grid[nx][ny] == 1:
                    continue
                new_g = g[cur] + 1
                if (nx, ny) not in g or new_g < g[(nx, ny)]:
                    g[(nx, ny)] = new_g
                    heapq.heappush(pq, (new_g + h((nx, ny), goal), new_g, (nx, ny)))
                    came[(nx, ny)] = cur
    return []
path = astar()
run = True
while run:
    screen.fill(WHITE)
    for i in range(ROWS):
        for j in range(ROWS):
            color = BLUE
            if grid[i][j] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, (j*SIZE, i*SIZE, SIZE, SIZE))
            pygame.draw.rect(screen, WHITE, (j*SIZE, i*SIZE, SIZE, SIZE), 1)
    for p in path:
        pygame.draw.circle(screen, GREEN,
                           (p[1]*SIZE+SIZE//2, p[0]*SIZE+SIZE//2), 10)
    pygame.draw.circle(screen, RED,
                       (start[1]*SIZE+SIZE//2, start[0]*SIZE+SIZE//2), 15)
    pygame.draw.circle(screen, GREEN,
                       (goal[1]*SIZE+SIZE//2, goal[0]*SIZE+SIZE//2), 15)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
pygame.quit()
