import random


class Snake:
    def __init__(self, x=random.randint(0, 10), y=random.randint(0,10), color=(random.randint(0,255), 255, 255)):
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
            new_head = (head[0], (head[1] - 1))
        elif direction == "DOWN":
            new_head = (head[0], (head[1] + 1))
        elif direction == "LEFT":
            new_head = ((head[0] - 1), head[1])
        else:  # RIGHT
            new_head = ((head[0] + 1), head[1])

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def get_direction(self):
        # Raise function not implemented
        raise NotImplementedError
