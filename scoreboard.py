from turtle import Turtle
FONT = ("Arial", 24, "normal")
LEVEL_POSITION = (-250, 250)
filename = "turtle_data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.level = 1
        with open(filename, "r") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.level_write()

    def level_write(self):
        self.write(f"Level: {self.level} \t\tHigh level: {self.high_score}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.level_write()

    def game_over(self):
        self.goto(0, 0)
        self. write("GAME OVER", align="center", font=FONT)
        self.level = 0

    def high_level(self):
        if self.level > self.high_score:
            self.high_score = self.level
        self.clear()
        self.level_write()

        with open(filename, mode="w") as f:
            f.write(str(self.high_score))
