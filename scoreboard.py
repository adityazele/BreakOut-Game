from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def lost(self):
        self.goto(0, 100)
        self.write('Lost', align="center", font=("Courier", 80, "normal"))

    def win(self):
        self.goto(0, 100)
        self.write('Won', align="center", font=("Courier", 80, "normal"))