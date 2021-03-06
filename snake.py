#!/usr/bin/env python3

# Snake Game with Turtle Module V 0.3
# Changelog V 0.1 to V 0.3
# Made it Executable with Hashbang, V 0.2
# Made Score into Function
# Made Minor Optimzations to the Code to shorten it. V 0.3


# Imports
import turtle
import time
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Coded by Sam")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Added Global Game Delay
delay = 0.01

# Scores Setup on Game Init
score = 0
high_score = 0

# Make the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake segments on Init
# Starts with an empty array as a null list
segments = []

# Scoring pen on Game Init. Global set to 0 Score.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Menlo", 24, "normal"))


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Functions Global

# Directional Functions - Check for directional ifs.


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"

# Move functions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def pen_score():
    pen.clear()
    pen.write("Score: {} High Score {}".format(score, high_score), align="center",
              font=("Menlo", 24, "normal"))


# Keyboard bindings for arrow keys, alter can be awsd.
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# Main Game Loop
while True:
    wn.update()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset Score to 0 as it colided
        score = 0
        # Reset the delay
        delay = 0.1

        pen_score()

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random location
        food.goto(x=random.randint(-290, 290), y=random.randint(-290, 290))

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay, Modify to increase difficulty * difficulty setting *
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen_score()

    # Move the end segments first in reverse order
    # Segments in index -1 but 0

    for index in range(len(segments)-1, 0, -1):
        segments[index].goto(segments[index-1].xcor(),
                             segments[index-1].ycor())

    # For the 0th head to goto the first pos
    if len(segments) > 0:
        segments[0].goto(x=head.xcor(), y=head.ycor())

    # Init Move
    move()

    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset Score to 0 as it colided
            score = 0
            # Reset the delay
            delay = 0.1

            pen_score()

    # Slow it down
    time.sleep(delay)

# Loop factor
wn.mainloop()
