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
TIE = 4

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


        

class Game:
    def __init__(self, snake1, snake2):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Bot Competition")
        self.clock = pygame.time.Clock()
        self.snake1 = snake1
        self.snake2 = snake2
        self.game_over = False
        self.food = self.spawn_food()

    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake1.body and food not in self.snake2.body:
                return food

    def check_collision(self):
        # Checking if the snakes collide with anything
        snake1_col = self.check_collision_per_snake(self.snake1, self.snake2)
        snake2_col = self.check_collision_per_snake(self.snake2, self.snake1)
        
        # Checking if both snakes collide with anything, if they both do at the same move, it's a tie
        if self.check_tie(snake1_col, snake2_col):
            return TIE
        if snake1_col:
            return SNAKE2_WIN
        if snake2_col:
            return SNAKE1_WIN
        return False
    
    def check_tie(self, snake1_col, snake2_col):
        # If the heads collide, it's a tie
        if self.snake1.body[0] in self.other_snake.body[0]:
            return TIE
        if snake1_col and snake2_col:
            return TIE
        return False
    
    
    def check_collision_per_snake(self, snake, other_snake):
        # Check if the snake collides with itself
        if snake.body[0] in snake.body[1:]:
            return SELF_KILL
        # Check if the snake collides with the other snake
        if snake.body[0] in other_snake.body:
            return STUCK_IN_PLAYER
        # Check if the snake collides with the wall
        if snake.body[0][0] < 0 or snake.body[0][0] >= GRID_WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= GRID_HEIGHT:
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