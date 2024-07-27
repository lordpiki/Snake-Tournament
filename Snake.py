import random


class Snake:
    def __init__(self, x, y, color):
        self.body = [(x, y), (x + 1, y)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.color = color
        self.grow = False

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = (head[0], (head[1] - 1))
        elif self.direction == "DOWN":
            new_head = (head[0], (head[1] + 1))
        elif self.direction == "LEFT":
            new_head = ((head[0] - 1), head[1])
        else:  # RIGHT
            new_head = ((head[0] + 1), head[1])

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self):
        # check that the direction is not opposite to the current direction
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction