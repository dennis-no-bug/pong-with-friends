from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.score_recorder()

    def score_recorder(self):
        self.goto(-100, 190)
        self.write(arg=self.p2_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 190)
        self.write(arg=self.p1_score, align="center", font=("Courier", 70, "normal"))

    def p1_total_score(self):
        self.p1_score += 1
        self.clear()
        self.score_recorder()

    def p2_total_score(self):
        self.p2_score += 1
        self.clear()
        self.score_recorder()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 70, "normal"))
