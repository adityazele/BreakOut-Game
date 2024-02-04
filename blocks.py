from turtle import Turtle


class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.initial_x_pos = 370
        self.initial_y_pos = 0
        self.i = 1
        self.blocks = []
        self.height = 3
        self.color = 1

    def generate_blocks(self):
        while self.height > 0:
            for _ in range(18):
                block = Turtle('square')
                if self.color == 1:
                    block.color('red')
                elif self.color == 2:
                    block.color('green')
                else:
                    block.color('blue')
                block.penup()
                block.shapesize(stretch_len=2)
                block.goto(self.initial_x_pos, self.initial_y_pos)
                block.id = self.i
                self.i += 1
                self.initial_x_pos -= 43
                self.blocks.append(block)
            self.height -= 1
            self.initial_x_pos = 370
            self.initial_y_pos += 25
            self.color += 1
