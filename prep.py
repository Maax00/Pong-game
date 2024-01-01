from turtle import Turtle
BR = (480, -280)
TR = (480, 280)
TL = (-480, 280)
BL = (-480, -280)

class draw_field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(10)
        self.hideturtle()
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color("white")
        self.goto(BR)
        self.pendown()
        self.goto(TR)
        self.goto(TL)
        self.goto(BL)
        self.goto(BR)
        self.goto(0, -280)
        self.setheading(90)
        while self.ycor() < 280:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()



