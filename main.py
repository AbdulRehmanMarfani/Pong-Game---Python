import time
import pygame
from turtle import Screen, Turtle

pygame.mixer.init()  # Initialize the mixer for sound

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# Function to set a custom background with error handling
def set_background(image_path):
    try:
        screen.bgpic(image_path)
        print("Background image loaded successfully.")
    except Exception as e:
        print(f"Error loading background image: {e}")

# Load sound effects
bounce_sound = pygame.mixer.Sound("Pong/bounce.mp3")  # Updated path to the bounce sound
point_scored_sound = pygame.mixer.Sound("Pong/point_scored.mp3")  # Load the point scored sound

# Draw dashed dividing line
def draw_dividing_line():
    divider = Turtle()
    divider.color("white")
    divider.penup()
    divider.goto(0, 300)
    divider.setheading(270)  # Point downwards
    divider.pendown()
    
    # Draw dashed line to cover the full height of the screen
    for _ in range(30):  # Adjusted number of dashes
        divider.pendown()
        divider.forward(20)  # Length of each dash
        divider.penup()
        divider.forward(10)  # Space between dashes

    divider.hideturtle()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Set the custom background to bg_resized.png
set_background("Pong/bg_resized.png")

# Draw the dividing line
draw_dividing_line()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280: 
        bounce_sound.play()  # Play sound when hitting the wall
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        bounce_sound.play()  # Play sound when hitting the paddle

    if ball.xcor() > 380:
        point_scored_sound.play()  # Play sound when left player scores
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        point_scored_sound.play()  # Play sound when right player scores
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
