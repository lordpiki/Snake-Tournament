from Snake import Snake
import random
class Bot (Snake):
    def __init__(self, x, y, color):
        super().__init__(x=x, y=y, color=color)

    # You may only change this function, (you may add helper functions)
    # This is an example function that plays follows the food
    def get_direction(self, other_snake, food: tuple[int, int]) -> str:
        """
        Returns the direction for the snake to move in.

        Parameters:
        - other_snake (list[tuple[int, int]]): A list of coordinates representing the other snake's body. (index 0 is the head)
        - food (tuple[int, int]): The coordinates of the food.
        
        Returns:
        - str: The direction for the snake to move in. Can be one of "UP", "DOWN", "LEFT", or "RIGHT".
        
        """
        
        if self.body[0][0] < food[0] and self.curr_direction != "LEFT":
            return "RIGHT"
        elif self.body[0][0] > food[0] and self.curr_direction != "RIGHT":
            return "LEFT"
        elif self.body[0][1] < food[1] and self.curr_direction != "UP":
            return "DOWN"
        elif self.body[0][1] > food[1] and self.curr_direction != "DOWN":
            return "UP"
        
        return self.random_dir()
    
    
    def random_dir(self):
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
