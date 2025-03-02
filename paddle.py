from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:  # Prevent moving above the screen
            self.goto(self.xcor(), self.ycor() + 40)

    def go_down(self):
        if self.ycor() > -240:  # Prevent moving below the screen
            self.goto(self.xcor(), self.ycor() - 40)
