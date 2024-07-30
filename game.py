import pygame
from Snake import Snake
import random

WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

SNAKE1_WIN = "SNAKE1_WIN"
SNAKE2_WIN = "SNAKE2_WIN"

SELF_KILL = 1
WALL_KILL = 2
STUCK_IN_PLAYER = 3
TIE = 4    

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
        self.winner = None

    def spawn_food(self):
        # Spawning food in a random location that is not occupied by the snakes
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake1.body and food not in self.snake2.body:
                return food

    def check_collision(self):
        # Checking if the snakes collide with anything
        snake1_col = self.check_collision_per_snake(self.snake1, self.snake2)
        snake2_col = self.check_collision_per_snake(self.snake2, self.snake1)
        
        # Checking if there is a tie
        if self.check_tie(snake1_col, snake2_col):
            self.winner = TIE
            return TIE
        if snake1_col:
            self.winner = SNAKE2_WIN
            return SNAKE2_WIN
        if snake2_col:
            self.winner = SNAKE1_WIN
            return SNAKE1_WIN
        return False
    
    def check_tie(self, snake1_col, snake2_col):
        # If the heads collide in the head, it's a tie
        if self.snake1.body[0] in self.snake2.body[0]:
            return TIE
        # If both snakes collide with something at the same time, it's a tie
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
        # Getting direction before playing a move, so that one snake can't see the other snake's move
        snake1_dir = self.snake1.get_direction(self.snake2.body, self.food)
        snake2_dir = self.snake2.get_direction(self.snake1.body, self.food)
        # Moving the snakes
        self.snake1.move(snake1_dir)
        self.snake2.move(snake2_dir)
        # Checking if the snakes eat the food
        for snake in [self.snake1, self.snake2]:
            if snake.body[0] == self.food:
                snake.grow = True
                self.food = self.spawn_food()
        collision = self.check_collision()
        score1 = len(self.snake1.body)
        score2 = len(self.snake2.body)
        if collision:
            self.game_over = True
            return
        if score1 > 20:
            self.winner = SNAKE1_WIN
            self.game_over = True
            return         
        if score2 > 20:
            self.winner = SNAKE2_WIN
            self.game_over = True
            return
