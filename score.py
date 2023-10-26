from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-40, 270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score} ", align="left", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(-0, 0)
        self.write(arg="GAME OVER", align="left", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
