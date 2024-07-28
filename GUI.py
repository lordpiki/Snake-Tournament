from Game import Game
import pygame
import sys
from Bot import Bot

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GUIManager:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Bot Competition")
        self.clock = pygame.time.Clock()
        self.game = game
        # Initialing the screen
        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.game.update()
            self.draw()
            self.clock.tick(FPS)

        # When the game is over, stay on the screen until the user closes it
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    def draw(self):
        self.screen.fill(BLACK)
        for snake in [self.game.snake1, self.game.snake2]:
            for index, segment in enumerate(snake.body):
                if index == 0:
                    pygame.draw.rect(self.screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                else:
                    pygame.draw.rect(self.screen, snake.color, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, RED, (self.game.food[0] * GRID_SIZE, self.game.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()

if __name__ == "__main__":
    bot1 = Bot(color=GREEN)
    bot2 = Bot(color=BLUE)
    game = Game(bot1, bot2)
    
    gui_manager = GUIManager(game)
    gui_manager.start()