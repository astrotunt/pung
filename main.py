from turtle import Screen
import time
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(950,600)
screen.bgcolor("black")
screen.title("pung")

right_paddle = Paddle('right')
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

screen.tracer(0)
game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.08)
    if ball.distance(right_paddle.pos()) <= 50 and ball.xcor() > 440:
        ball.setheading(random.randint(91, 269))
    if ball.distance(left_paddle.pos()) <= 50 and ball.xcor() < -440:
        choices = [random.randint(1, 89), random.randint(271, 359)]
        ball.setheading(random.choice(choices))
    if ball.xcor() >= 470:
        scoreboard.left_score += 1
        scoreboard.display_score()
        ball.reset()
        right_paddle.reset()
        left_paddle.reset()
        time.sleep(1)
    elif ball.xcor() <= -470:
        scoreboard.right_score += 1
        scoreboard.display_score()
        ball.reset()
        right_paddle.reset()
        left_paddle.reset()
        time.sleep(1)


screen.exitonclick()
