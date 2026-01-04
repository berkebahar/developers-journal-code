import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Prime Number Snake Game")

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (1, 0)
        self.grow_pending = False
    
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0] * CELL_SIZE, head[1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def grow(self):
        self.grow_pending = True
    
    def change_direction(self, dir):
        if (dir[0] * -1, dir[1] * -1) != self.direction:
            self.direction = dir

    def eat_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WINDOW_WIDTH, y))

def generate_numbers():
    numbers = []
    primes = set()
    for _ in range(17):
        number = random.randint(2, 100)
        if Snake().eat_prime(number):
            primes.add(number)
        x = random.randint(0, WINDOW_WIDTH / CELL_SIZE - 1) * CELL_SIZE
        y = random.randint(0, WINDOW_HEIGHT / CELL_SIZE - 1) * CELL_SIZE
        numbers.append((number, x, y))
    return numbers, primes

def end_screen():
    font = pygame.font.SysFont(None, 48)
    text = font.render("You Won!", True, GREEN)
    screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()

    pygame.time.wait(2000)

    return 'quit'

snake = Snake()
numbers, primes = generate_numbers()
primes_collected = set()

running = True
while running:
    screen.fill((0, 0, 0))

    draw_grid()

    # Draw snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Draw numbers
    font = pygame.font.SysFont(None, 24)
    for number, x, y in numbers:
        text = font.render(str(number), True, WHITE)
        screen.blit(text, (x, y))

    pygame.display.flip()

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        snake.change_direction((-1, 0))
    if keys[pygame.K_RIGHT]:
        snake.change_direction((1, 0))
    if keys[pygame.K_UP]:
        snake.change_direction((0, -1))
    if keys[pygame.K_DOWN]:
        snake.change_direction((0, 1))

    snake.move()

    for number, x, y in numbers:
        if snake.body[0][0] == x and snake.body[0][1] == y:
            if snake.eat_prime(number):
                snake.grow()
                numbers.remove((number, x, y))
                primes_collected.add(number)
                if primes_collected == primes:
                    end_result = end_screen()
                    if end_result == 'quit':
                        running = False
            else:
                running = False

pygame.quit()



