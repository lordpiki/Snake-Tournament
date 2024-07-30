import os
import sys
import random
import importlib.util
from typing import List, Type

import pygame
from Game import Game, SNAKE1_WIN, SNAKE2_WIN, TIE

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

K_FACTOR = 20

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
# Currently playing at 30 FPS (To be able to see the game normally)
# You can increase the FPS to speed up the game
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class GUIManager:
    def __init__(self, game: Game, stop_on_end: bool=False):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Bot Competition")
        self.clock = pygame.time.Clock()
        self.game = game
        self.stop_on_end = stop_on_end
        self.run()

    def run(self):
        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.game.update()
            self.draw()
            self.clock.tick(FPS)
            
        # Check if user wants to close the window
        if self.stop_on_end:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

    def draw(self):
        self.screen.fill(BLACK)
        for snake in [self.game.snake1, self.game.snake2]:
            for index, segment in enumerate(snake.body):
                color = WHITE if index == 0 else snake.color
                pygame.draw.rect(self.screen, color, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, RED, (self.game.food[0] * GRID_SIZE, self.game.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()

class Tournament:
    def __init__(self) -> None:
        self.bot_rating = {}
        self.bot_classes = self.get_bot_classes(self.get_files_from_folder("Bots"))
        for bot_class in self.bot_classes:
            self.bot_rating[bot_class] = 200

    def run(self):
        for bot_class in self.bot_classes:
            for _ in range(len(self.bot_classes) * 2):
                random_class = random.choice([bot for bot in self.bot_classes if bot != bot_class])
                winner = self.duel(bot_class, random_class)
                self.calc_ratings(winner, bot_class, random_class)
        self.log_results()

    def log_results(self):
        with open("results.txt", "w") as f:
            for bot_class, rating in self.bot_rating.items():
                f.write(f"{str(bot_class)[8:-6]}: {int(rating)}\n")

    def duel(self, bot_class1, bot_class2):
        bot1 = bot_class1(x=random.randint(5, GRID_WIDTH // 2), y=random.randint(3, GRID_HEIGHT - 3), color=GREEN)
        bot2 = bot_class2(x=random.randint(GRID_WIDTH // 2, GRID_WIDTH - 5), y=random.randint(3, GRID_HEIGHT - 3), color=BLUE)
        game = Game(bot1, bot2)
        GUIManager(game)
        return game.winner

    @staticmethod
    def load_bot_from_file(filepath: str = "Bots/Bot.py"):
        try:
            module_name = os.path.splitext(os.path.basename(filepath))[0]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            bot_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(bot_module)
            return getattr(bot_module, "Bot")
        except Exception as e:
            print(f"Error loading bot from {filepath}: {e}")
            return None

    @staticmethod
    def get_files_from_folder(path: str = "."):
        return [os.path.join(path, file_name) for file_name in os.listdir(path) if file_name.endswith(".py")]

    @staticmethod
    def get_bot_classes(file_names: List[str]):
        return [Tournament.load_bot_from_file(file_name) for file_name in file_names if Tournament.load_bot_from_file(file_name)]

    def calc_ratings(self, winner, bot1, bot2):
        expected_score1 = 1 / (1 + 10 ** ((self.bot_rating[bot2] - self.bot_rating[bot1]) / 400))
        expected_score2 = 1 / (1 + 10 ** ((self.bot_rating[bot1] - self.bot_rating[bot2]) / 400))
        if winner == SNAKE1_WIN:
            self.bot_rating[bot1] += K_FACTOR * (1 - expected_score1)
            self.bot_rating[bot2] += K_FACTOR * (0 - expected_score2)
        elif winner == SNAKE2_WIN:
            self.bot_rating[bot1] += K_FACTOR * (0 - expected_score1)
            self.bot_rating[bot2] += K_FACTOR * (1 - expected_score2)
        else:
            self.bot_rating[bot1] += K_FACTOR * (0.5 - expected_score1)
            self.bot_rating[bot2] += K_FACTOR * (0.5 - expected_score2)

def main():
    # tournament = Tournament()
    # tournament.run()
    
    # If you want to just run the Tournament, uncomment the above lines and comment lines below
    bot_class1 = Tournament.load_bot_from_file("Bots/randomBot.py")
    bot_class2 = Tournament.load_bot_from_file("Bots/exampleBot.py")
    game = Game(bot_class1(x=random.randint(5, GRID_WIDTH // 2), y=random.randint(3, GRID_HEIGHT - 3), color=GREEN), bot_class2(x=random.randint(GRID_WIDTH // 2, GRID_WIDTH - 5), y=random.randint(3, GRID_HEIGHT - 3), color=BLUE))
    gui = GUIManager(game, True)
    
if __name__ == "__main__":
    main()
