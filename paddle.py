from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        self.side = side
        super().__init__()
        self.current_x = 0
        self.current_y = 0
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        if side == "right":
            self.setposition(440, 0)
        elif side == "left":
            self.setposition(-440, 0)

    def move_up(self):
        self.current_x, self.current_y = self.pos()
        if self.distance(0, 0) < 540:
            self.goto(self.current_x, self.current_y + 30)

    def move_down(self):
        self.current_x, self.current_y = self.pos()
        if self.distance(0, 0) < 540:
            self.goto(self.current_x, self.current_y - 30)

    def reset(self):
        if self.side == "right":
            self.setposition(440, 0)
        elif self.side == "left":
            self.setposition(-440, 0)
