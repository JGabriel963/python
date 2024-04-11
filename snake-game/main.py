# Setup
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
width, height = 600, 400
screen= pygame.display.set_mode((width, height))
watch = pygame.time.Clock()

# Cores 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Parametro da cobra
size_square = 10
speed_game = 10

def generate_food():
    food_x = round((random.randrange(0, width - size_square) / 20.0)) * 20.0
    food_y = round((random.randrange(0, height - size_square) / 20.0)) * 20.0
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])

def draw_point(point):
    font = pygame.font.SysFont("Helvetica", 35)
    text = font.render(f"Pontos: {point}", True, red)
    screen.blit(text, [1, 1])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = size_square
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = -size_square
    elif key == pygame.K_RIGHT:
        speed_x = size_square
        speed_y = 0
    elif key == pygame.K_LEFT:
        speed_x = -size_square
        speed_y = 0
    return speed_x, speed_y


def run_game():
    game_over = False

    x = height / 2
    y = width / 2

    speed_x = 0
    speed_y = 0

    size_snake = 1
    pixels = []

    food_x, food_y = generate_food()

    while not game_over:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

        # Desnhar comida
        draw_food(size_square, food_x, food_y)

        # Atualizar o posição da cobra
        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True
        x += speed_x
        y+= speed_y

        # Desenhar cobra
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixels == [x, y]:
                game_over = True
        draw_snake(size_square, pixels)

        # Desenhar pontuação
        draw_point(size_snake - 1)

        # Atualizar tela
        pygame.display.update()

        # Criar um nova comida
        if x == food_x and y == food_y:
            size_snake += 1
            food_x, food_y = generate_food() 
        watch.tick(speed_game)


run_game()