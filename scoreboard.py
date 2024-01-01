from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = "Center"
class Score_Board(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.write(f"Score: {self.score}", font=FONT)

    def score_right(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN , font=FONT)

    def score_left(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN , font=FONT)