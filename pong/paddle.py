from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, tx, ty):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(tx, ty)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 241:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
