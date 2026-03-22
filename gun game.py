import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Bullet
bullet_width = 5
bullet_height = 10
bullets = []

# Enemy
enemy_size = 50
enemy_speed = 2
enemies = []

# Clock
clock = pygame.time.Clock()

def draw_window():
    win.fill(WHITE)
    pygame.draw.rect(win, RED, (player_x, player_y, player_size, player_size))
    for bullet in bullets:
        pygame.draw.rect(win, (0, 0, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(win, (0, 255, 0), enemy)
    pygame.display.update()

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_size)
    enemies.append(pygame.Rect(x, 0, enemy_size, enemy_size))

# Main loop
run = True
spawn_timer = 0
while run:
    clock.tick(60)
    spawn_timer += 1
    if spawn_timer > 60:
        spawn_enemy()
        spawn_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player_x + player_size//2, player_y, bullet_width, bullet_height))

    # Update bullets
    for bullet in bullets[:]:
        bullet.y -= 5
        if bullet.y < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            print("Game Over!")
            run = False
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

    draw_window()

pygame.quit()
