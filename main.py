from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# create paddle
p1 = Paddle(350, 0)
p2 = Paddle(-350, 0)
ball = Ball()

p1.color("cyan")
p2.color("pink")

screen.listen()
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collison with right paddle
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.p2_total_score()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.p1_total_score()

    if scoreboard.p1_score == 8 or scoreboard.p2_score == 8:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
