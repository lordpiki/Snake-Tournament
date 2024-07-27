import pygame
import sys
from Snake import Snake
import random

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 30

SNAKE1_WIN = "SNAKE1_WIN"
SNAKE2_WIN = "SNAKE2_WIN"

SELF_KILL = 1
WALL_KILL = 2
STUCK_IN_PLAYER = 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


        

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Bot Competition")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake1 = Snake(GRID_WIDTH // 4, GRID_HEIGHT // 2, GREEN)
        self.snake2 = Snake(3 * GRID_WIDTH // 4, GRID_HEIGHT // 2, BLUE)

        self.food = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake1.body and food not in self.snake2.body:
                return food

    def check_collision(self):
        if self.check_collision_per_snake(self.snake1, self.snake2):
            return SNAKE2_WIN
        if self.check_collision_per_snake(self.snake2, self.snake1):
            return SNAKE1_WIN
        return False
    
    def check_collision_per_snake(self, snake1, snake2):
        if snake1.body[0] in snake1.body[1:]:
            return SELF_KILL
        if snake1.body[0] in snake2.body:
            return STUCK_IN_PLAYER
        if snake1.body[0][0] < 0 or snake1.body[0][0] >= GRID_WIDTH or snake1.body[0][1] < 0 or snake1.body[0][1] >= GRID_HEIGHT:
            return WALL_KILL
        return False


    def update(self):
        for snake in [self.snake1, self.snake2]:
            snake.move()
            if snake.body[0] == self.food:
                snake.grow = True
                self.food = self.spawn_food()
            snake.change_direction()  # Random movement
        collision = self.check_collision()
        if collision:
            print("Game Over")
            print(collision)
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        for snake in [self.snake1, self.snake2]:
            for index, segment in enumerate(snake.body):
                if index == 0:
                    pygame.draw.rect(self.screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                else:
                    pygame.draw.rect(self.screen, snake.color, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, RED, (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()
            self.draw()
            self.clock.tick(FPS)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()