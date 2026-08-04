"""
Racing Game with AI Opponent
------------------------------
A simple top-down racing game. You control the blue car; a red AI car
races against you by steering toward a sequence of waypoints around the
oval track and adjusting speed for turns.

Controls:
  UP / DOWN    -> accelerate / brake
  LEFT / RIGHT -> steer
  R            -> restart race
"""

import pygame
import math

WIDTH, HEIGHT = 800, 600
FPS = 60

BLACK = (20, 20, 20)
GREY = (90, 90, 90)
WHITE = (240, 240, 240)
BLUE = (70, 130, 220)
RED = (220, 70, 70)
YELLOW = (240, 220, 80)

# Oval track defined as a ring of waypoints (cx, cy, radius-ish ellipse)
CENTER = (WIDTH // 2, HEIGHT // 2)
TRACK_A, TRACK_B = 300, 200  # ellipse radii
NUM_WAYPOINTS = 24
WAYPOINTS = [
    (
        CENTER[0] + TRACK_A * math.cos(2 * math.pi * i / NUM_WAYPOINTS),
        CENTER[1] + TRACK_B * math.sin(2 * math.pi * i / NUM_WAYPOINTS),
    )
    for i in range(NUM_WAYPOINTS)
]


class Car:
    def __init__(self, x, y, angle, color):
        self.x = x
        self.y = y
        self.angle = angle  # degrees
        self.speed = 0
        self.color = color
        self.max_speed = 5.5
        self.laps = 0
        self.next_wp = 0

    def rect_points(self):
        w, h = 18, 10
        rad = math.radians(self.angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        corners = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        return [(self.x + cx * cos_a - cy * sin_a, self.y + cx * sin_a + cy * cos_a) for cx, cy in corners]

    def move(self):
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

    def draw(self, win):
        pygame.draw.polygon(win, self.color, self.rect_points())

    def check_waypoint(self):
        wx, wy = WAYPOINTS[self.next_wp]
        if math.hypot(self.x - wx, self.y - wy) < 40:
            self.next_wp = (self.next_wp + 1) % NUM_WAYPOINTS
            if self.next_wp == 0:
                self.laps += 1


def player_control(car, keys):
    if keys[pygame.K_UP]:
        car.speed = min(car.max_speed, car.speed + 0.15)
    elif keys[pygame.K_DOWN]:
        car.speed = max(-2, car.speed - 0.2)
    else:
        car.speed *= 0.98  # friction

    turn_rate = 3.2 if abs(car.speed) > 0.5 else 0
    if keys[pygame.K_LEFT]:
        car.angle -= turn_rate
    if keys[pygame.K_RIGHT]:
        car.angle += turn_rate


def ai_control(car):
    target_x, target_y = WAYPOINTS[car.next_wp]
    target_angle = math.degrees(math.atan2(target_y - car.y, target_x - car.x))

    diff = (target_angle - car.angle + 180) % 360 - 180
    turn_rate = 3.0
    if diff > turn_rate:
        car.angle += turn_rate
    elif diff < -turn_rate:
        car.angle -= turn_rate
    else:
        car.angle = target_angle

    # slow down for sharp turns, speed up on straights
    target_speed = car.max_speed * (1 - min(abs(diff) / 90, 0.6))
    car.speed += (target_speed - car.speed) * 0.08


def draw_track(win):
    pygame.draw.ellipse(win, GREY, (CENTER[0] - TRACK_A - 60, CENTER[1] - TRACK_B - 60,
                                     2 * (TRACK_A + 60), 2 * (TRACK_B + 60)), 90)
    pygame.draw.ellipse(win, BLACK, (CENTER[0] - TRACK_A + 60, CENTER[1] - TRACK_B + 60,
                                      2 * (TRACK_A - 60), 2 * (TRACK_B - 60)))
    # start/finish line
    sx, sy = WAYPOINTS[0]
    pygame.draw.line(win, WHITE, (sx, sy - 55), (sx, sy + 55), 4)


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game with AI Opponent")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Segoe UI", 22)

    def reset():
        wx0, wy0 = WAYPOINTS[0]
        wx1, wy1 = WAYPOINTS[1]
        start_angle = math.degrees(math.atan2(wy1 - wy0, wx1 - wx0))
        player = Car(wx0, wy0 - 15, start_angle, BLUE)
        ai = Car(wx0, wy0 + 15, start_angle, RED)
        return player, ai

    player, ai = reset()
    running = True
    laps_to_win = 3
    winner = None

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player, ai = reset()
                winner = None

        if winner is None:
            keys = pygame.key.get_pressed()
            player_control(player, keys)
            ai_control(ai)

            player.move()
            ai.move()
            player.check_waypoint()
            ai.check_waypoint()

            if player.laps >= laps_to_win:
                winner = "You win!"
            elif ai.laps >= laps_to_win:
                winner = "AI wins!"

        win.fill((40, 140, 60))
        draw_track(win)
        for wx, wy in WAYPOINTS:
            pygame.draw.circle(win, YELLOW, (int(wx), int(wy)), 3)

        player.draw(win)
        ai.draw(win)

        hud = font.render(f"You: lap {player.laps}/{laps_to_win}   AI: lap {ai.laps}/{laps_to_win}", True, WHITE)
        win.blit(hud, (10, 10))

        if winner:
            msg = font.render(f"{winner}  (press R to restart)", True, WHITE)
            win.blit(msg, (WIDTH // 2 - 140, HEIGHT // 2))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
