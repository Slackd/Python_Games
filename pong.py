# Pong Game with Turtle Module V 0.1
# Changelog
# .......
# .......
# .......


# Imports
import turtle
import os
import time

# Setup the screen
wn = turtle.Screen()
wn.title(" Pong @ Coded by Sam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Added Global Game Delay
delay = 0.1

# Score Initialization
score_a = 0
score_b = 0

# Create Screen Interaction Objects

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("Score A: 0  | Score B: 0", align="center",
          font=("Menlo", 24, "normal"))

# Ball Velocity Multiplier
ball.dx = 2
ball.dy = 2

# Functional Area
# Paddle Movement Function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Score update on screen function


def pen_score():
    pen.clear()
    pen.write("Score A: {} | Score B: {}".format(score_a, score_b), align="center",
              font=("Menlo", 24, "normal"))


# Control Keybindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Logic Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check (Top, Bottom, Right & Left)

    # Top & Bottom Logic
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        # Shorten the delay, Modify to increase difficulty * difficulty setting *
        delay -= 0.01
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        # Shorten the delay, Modify to increase difficulty * difficulty setting *
        delay -= 0.01
    # Left & Right Logic
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen_score()

    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen_score()

    # Paddle and Ball Collisions, Logic
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
