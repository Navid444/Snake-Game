from turtle import Turtle
from food import Food


ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="Center", font=("Courier", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
