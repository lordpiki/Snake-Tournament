import importlib
import importlib.util
import importlib.machinery
from Game import Game, SNAKE1_WIN, SNAKE2_WIN, TIE
import pygame
import sys
import random
import os

K_FACTOR = 20

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 165

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

class Tournament:
    def __init__(self) -> None:
        self.bot_rating = {}
        self.bot_classes = self.get_bot_classes(self.get_files_from_folder("Bots"))
        for bot_class in self.bot_classes:
            self.bot_rating[bot_class] = 200
    
    def run(self) -> dict:
        for bot_class in self.bot_classes:
            for _ in range(10):
                random_class = random.choice(self.bot_classes)
                winner = self.duel(bot_class, random_class)
                self.calc_ratings(winner, bot_class, random_class)
                print(self.bot_rating)
        return self.bot_rating
    
    def duel(self, bot_class1, bot_class2):
        # Putting the bots in different sides of the game
        bot1 = bot_class1(x=random.randint(5, GRID_WIDTH // 2), y=random.randint(3, GRID_HEIGHT - 3), color=GREEN)
        bot2 = bot_class2(x=random.randint(GRID_WIDTH // 2, GRID_WIDTH - 5), y=random.randint(3, GRID_HEIGHT - 3), color=BLUE)
        game = Game(bot1, bot2)
        gui_manager = GUIManager(game)
        winner = game.winner
        return winner
        
    # Function to load bots from file path
    @staticmethod
    def load_bot_from_file(filepath: str = "Bots/Bot.py"):
        try:
            module_name = os.path.splitext(os.path.basename(filepath))[0]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            bot_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(bot_module)
            bot_class = getattr(bot_module, "Bot")
            return bot_class
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def get_files_from_folder(path: str = "."):
        file_names = []
        for file_name in os.listdir(path):
            if file_name.endswith(".py"):
                file_names.append(path + "/" + file_name)
        return file_names
    
    @staticmethod
    def get_bot_classes(file_names: list):
        bot_classes = []
        for file_name in file_names:
            bot_class = Tournament.load_bot_from_file(file_name)
            if bot_class:
                bot_classes.append(bot_class)
        return bot_classes
    
    # Calculate the new ratings of the bots using the Elo rating system
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
    tournament = Tournament()
    tournament.run()
    # Choosing 2 bots at random
    # Making sure the bots spawn in different sides of the game
    # bot1 = random.choice(bot_classes)(x=random.randint(5, GRID_WIDTH / 2), y=random.randint(3, GRID_HEIGHT - 3), color=GREEN)
    # bot2 = random.choice(bot_classes)(x=random.randint(GRID_WIDTH / 2, GRID_WIDTH - 5), y=random.randint(3, GRID_HEIGHT - 3), color=BLUE)
   
    # game = Game(bot1, bot2) 
    # gui_manager = GUIManager(game)
    # gui_manager.start()

if __name__ == "__main__":
    main()