
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 600
full_height = height - 100  # Adjusted height for score display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game 🐍')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90,
                          
                          50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Game settings
speed = 10
clock = pygame.time.Clock()



# Food settings
food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (full_height//10)) * 10]
food_spawn = True

# Score
score = 100




# Font
font = pygame.font.SysFont('times new roman', 20)

def show_score():
    score_surface = font.render(f'Score: {score}', True, white)
    screen.blit(score_surface, (10, 10))

def game_over():
    msg = font.render('Game Over! Press any key to exit.', True, red)
    screen.blit(msg, (width//4, height//2))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    direction = change_to
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10
    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,
                    random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Background
    screen.fill(red)

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Check for collisions
    if (snake_pos[0] < 0 or snake_pos[0] > width-10 or
        snake_pos[1] < 0 or snake_pos[1] > height-10):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score()
    pygame.display.update()
    
