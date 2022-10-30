from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.setposition(0,0)
        self.penup()
        self.setheading(random.randint(0,360))
        self.new_heading = 0
        self.current_heading = 0

    def move(self):
        self.forward(30)
        if self.ycor() >= 300 or self.ycor() <= -300:
            self.bounce()

    def bounce(self):
        self.current_heading = self.heading()
        self.new_heading = 360 - self.heading()
        self.setheading(self.new_heading)

    def reset(self):
        self.setposition(0,0)
        self.setheading(random.randint(0, 360))