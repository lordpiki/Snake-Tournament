from Snake import Snake
import random

class Bot (Snake):
    def __init__(self, color):
        super().__init__(color=color)

    # You may only change this function, (you may add helper functions)
    # This is an example function that plays completely randomly
    def get_direction(self, other_snake: list[tuple[int, int]], food: tuple[int, int]):
        # Choose a random direction
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        
        # Check that the direction is not opposite to the current direction
        if direction == "UP" and self.curr_direction != "DOWN":
            return direction
        elif direction == "DOWN" and self.curr_direction != "UP":
            return direction
        elif direction == "LEFT" and self.curr_direction != "RIGHT":
            return direction
        elif direction == "RIGHT" and self.curr_direction != "LEFT":
            return direction
        return self.curr_direction