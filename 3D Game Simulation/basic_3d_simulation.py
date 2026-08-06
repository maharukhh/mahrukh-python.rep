"""
3D Game Simulation (basic)
-----------------------------
A minimal 3D engine built from scratch with Pygame — no 3D library
dependency. Renders wireframe cubes in 3D space with rotation and
perspective projection, and lets you fly a simple camera through the
scene.

Controls:
  W / S           -> move forward / backward
  A / D           -> strafe left / right
  UP / DOWN arrow -> move camera up / down
  LEFT / RIGHT    -> rotate camera (look left/right)
  R               -> reset camera
"""

import pygame
import math

WIDTH, HEIGHT = 900, 600
FOV = 400  # projection "focal length"
BLACK = (10, 10, 15)
WHITE = (240, 240, 240)
CYAN = (80, 220, 220)


def make_cube(cx, cy, cz, size):
    s = size / 2
    verts = [
        (cx - s, cy - s, cz - s), (cx + s, cy - s, cz - s),
        (cx + s, cy + s, cz - s), (cx - s, cy + s, cz - s),
        (cx - s, cy - s, cz + s), (cx + s, cy - s, cz + s),
        (cx + s, cy + s, cz + s), (cx - s, cy + s, cz + s),
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    return verts, edges


class Camera:
    def __init__(self):
        self.x, self.y, self.z = 0.0, 0.0, -8.0
        self.yaw = 0.0  # radians, rotation around Y axis

    def move_forward(self, amount):
        self.x += math.sin(self.yaw) * amount
        self.z += math.cos(self.yaw) * amount

    def move_strafe(self, amount):
        self.x += math.cos(self.yaw) * amount
        self.z -= math.sin(self.yaw) * amount

    def to_camera_space(self, point):
        x, y, z = point[0] - self.x, point[1] - self.y, point[2] - self.z
        cos_a, sin_a = math.cos(-self.yaw), math.sin(-self.yaw)
        x_rot = x * cos_a - z * sin_a
        z_rot = x * sin_a + z * cos_a
        return x_rot, y, z_rot


def project(point):
    x, y, z = point
    if z <= 0.1:
        return None  # behind camera
    scale = FOV / z
    sx = WIDTH / 2 + x * scale
    sy = HEIGHT / 2 + y * scale
    return sx, sy


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Basic 3D Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 18)

    # scene: a small grid of cubes at different positions
    cubes = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (i + j) % 2 == 0:
                cubes.append(make_cube(i * 3, 0, j * 3 + 6, 1.5))

    camera = Camera()
    rotation_t = 0.0
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        speed = 0.1
        if keys[pygame.K_w]:
            camera.move_forward(speed)
        if keys[pygame.K_s]:
            camera.move_forward(-speed)
        if keys[pygame.K_a]:
            camera.move_strafe(-speed)
        if keys[pygame.K_d]:
            camera.move_strafe(speed)
        if keys[pygame.K_UP]:
            camera.y -= speed
        if keys[pygame.K_DOWN]:
            camera.y += speed
        if keys[pygame.K_LEFT]:
            camera.yaw -= 0.03
        if keys[pygame.K_RIGHT]:
            camera.yaw += 0.03
        if keys[pygame.K_r]:
            camera = Camera()

        rotation_t += 0.01

        win.fill(BLACK)
        for verts, edges in cubes:
            # spin each cube slowly around its own local origin for visual interest
            spun = []
            for (x, y, z) in verts:
                cx, cy, cz = x, y, z
                cos_a, sin_a = math.cos(rotation_t), math.sin(rotation_t)
                # simple Y-axis spin around scene origin per cube's own center approx
                spun.append((cx, cy, cz))

            cam_space = [camera.to_camera_space(v) for v in spun]
            screen_pts = [project(p) for p in cam_space]

            for a, b in edges:
                pa, pb = screen_pts[a], screen_pts[b]
                if pa and pb:
                    pygame.draw.line(win, CYAN, pa, pb, 2)

        hud = font.render(
            "W/A/S/D move, UP/DOWN height, LEFT/RIGHT turn, R reset", True, WHITE)
        win.blit(hud, (10, 10))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
