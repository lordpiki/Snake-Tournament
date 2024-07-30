import random

WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

class Snake:
    def __init__(self, x, y, color=(random.randint(0,255), 255, 255)):
        self.body = [(x, y), (x + 1, y)]
        self.curr_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.color = color
        self.grow = False

    def move(self, direction):
        
        if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
            raise ValueError("Invalid direction")
        
        self.curr_direction = direction
        head = self.body[0]
        if direction == "UP":
            new_head = (head[0] % GRID_WIDTH, (head[1] - 1) % GRID_HEIGHT)
        elif direction == "DOWN":
            new_head = (head[0] % GRID_WIDTH, (head[1] + 1) % GRID_HEIGHT)
        elif direction == "LEFT":
            new_head = ((head[0] - 1) % GRID_WIDTH, head[1] % GRID_HEIGHT)
        else:  # RIGHT
            new_head = ((head[0] + 1) % GRID_WIDTH, head[1] % GRID_HEIGHT)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def get_direction(self):
        # Raise function not implemented
        raise NotImplementedError
