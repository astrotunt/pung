from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.ht()
        self.color("blue")
        self.setposition(0,280)

    def display_score(self):
        self.clear()
        self.write(arg=f"{self.left_score}:{self.right_score}",align="center",font=("Arial", 12, "bold"))