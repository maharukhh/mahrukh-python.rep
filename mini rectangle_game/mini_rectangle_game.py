import pygame

pygame.init()

# Window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("mini rectangle Game")

# Dino
x = 50
y = 300
jump = False
velocity = 15

# Obstacle
obs_x = 800

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    screen.fill((255, 255, 255))

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Jump
    keys = pygame.key.get_pressed()

    if not jump and keys[pygame.K_SPACE]:
        jump = True

    if jump:
        y -= velocity
        velocity -= 1

        if y >= 300:
            y = 300
            jump = False
            velocity = 15

    # Obstacle movement
    obs_x -= 7
    if obs_x < 0:
        obs_x = 800

    # Draw dino
    pygame.draw.rect(screen, (0, 200, 0), (x, y, 40, 40))

    # Draw obstacle
    pygame.draw.rect(screen, (0, 0, 0), (obs_x, 300, 20, 60))

    # Collision
    dino = pygame.Rect(x, y, 40, 40)
    obstacle = pygame.Rect(obs_x, 300, 20, 60)

    if dino.colliderect(obstacle):
        print("Game Over")
        run = False

    pygame.display.update()

pygame.quit()