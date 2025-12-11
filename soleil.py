from turtle import Turtle

class Soleil(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.goto(0,0)
        self.shapesize(10,10)