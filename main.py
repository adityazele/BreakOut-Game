from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BreakOut Game")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()
block = Blocks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

pos = 380

block.generate_blocks()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.ycor() - paddle.ycor() < 20 and (
            (ball.xcor() - paddle.xcor() < 80) and (ball.xcor() - paddle.xcor() > -80)):
        ball.bounce_y()

    # Detect collision with blocks
    for blk in block.blocks:
        if ((blk.ycor() - ball.ycor() < 20) and (blk.ycor() - ball.ycor() > -20)) and ((blk.xcor() - ball.xcor() < 20) and (blk.xcor() - ball.xcor() > -20)):
            ball.bounce_y()
            print(blk.id)
            block.blocks.remove(blk)
            blk.reset()
            scoreboard.score += 1
            scoreboard.update_scoreboard()
            break

    # Game Over
    if ball.ycor() < -290:
        ball.reset_position()
        scoreboard.lost()
        game_is_on = False

    if scoreboard.score == 54:
        scoreboard.win()
        game_is_on = False

screen.exitonclick()
