import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GOALIE_WIDTH = 50
GOALIE_HEIGHT = 50
NUMBER_SIZE = 30

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Prime Number Catcher")

clock = pygame.time.Clock()


class Goalie:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2 - GOALIE_WIDTH // 2
        self.y = WINDOW_HEIGHT - GOALIE_HEIGHT - 10
        self.speed = 7

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > WINDOW_WIDTH - GOALIE_WIDTH:
            self.x = WINDOW_WIDTH - GOALIE_WIDTH


class Number:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.x = random.randint(0, WINDOW_WIDTH - NUMBER_SIZE)
        self.y = random.randint(-500, -100)
        self.speed_x = random.randint(-1, 1)
        self.speed_y = random.uniform(0.5, 1.5)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.is_prime = self.check_prime()

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WINDOW_WIDTH - NUMBER_SIZE:
            self.speed_x *= -1

        if self.y >= WINDOW_HEIGHT:
            self.reset()

    def reset(self):
        self.number = random.randint(1, 100)
        self.x = random.randint(0, WINDOW_WIDTH - NUMBER_SIZE)
        self.y = random.randint(-500, -100)
        self.speed_x = random.randint(-1, 1)
        self.speed_y = random.uniform(0.5, 1.5)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.is_prime = self.check_prime()

    def check_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False
        return True


def draw_goalie(goalie):
    pygame.draw.rect(
        screen, BLUE, (goalie.x, goalie.y, GOALIE_WIDTH, GOALIE_HEIGHT)
    )


def draw_number(number):
    font = pygame.font.SysFont(None, 24)
    text = font.render(str(number.number), True, number.color)
    screen.blit(text, (number.x, number.y))


def display_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))


def game_over(score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over!", True, RED)
    screen.blit(
        text,
        (
            WINDOW_WIDTH // 2 - text.get_width() // 2,
            WINDOW_HEIGHT // 2 - text.get_height() // 2,
        ),
    )

    font = pygame.font.SysFont(None, 24)
    text = font.render("Your score: " + str(score), True, WHITE)
    screen.blit(
        text,
        (
            WINDOW_WIDTH // 2 - text.get_width() // 2,
            WINDOW_HEIGHT // 2 + text.get_height(),
        ),
    )

    pygame.display.flip()
    pygame.time.wait(2000)


def game_won(score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("You Won!", True, GREEN)
    screen.blit(
        text,
        (
            WINDOW_WIDTH // 2 - text.get_width() // 2,
            WINDOW_HEIGHT // 2 - text.get_height() // 2,
        ),
    )

    font = pygame.font.SysFont(None, 24)
    text = font.render("Your score: " + str(score), True, WHITE)
    screen.blit(
        text,
        (
            WINDOW_WIDTH // 2 - text.get_width() // 2,
            WINDOW_HEIGHT // 2 + text.get_height(),
        ),
    )

    pygame.display.flip()
    pygame.time.wait(2000)


def main():
    goalie = Goalie()
    numbers = []
    score = 0
    running = True

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            goalie.move_left()
        if keys[pygame.K_RIGHT]:
            goalie.move_right()

        if random.random() < 0.003:
            numbers.append(Number())

        for number in numbers[:]:
            number.move()
            draw_number(number)

            if (
                goalie.x < number.x + NUMBER_SIZE
                and goalie.x + GOALIE_WIDTH > number.x
                and goalie.y < number.y + NUMBER_SIZE
                and goalie.y + GOALIE_HEIGHT > number.y
            ):
                if number.is_prime:
                    score += 15
                else:
                    score -= 10
                numbers.remove(number)

        draw_goalie(goalie)
        display_score(score)

        if score < -50:
            game_over(score)
            running = False
        elif score > 100:
            game_won(score)
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
