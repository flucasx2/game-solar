from turtle import Turtle
from math import cos,sin,pi

class Planete(Turtle):
    def __init__(self,langle:int,color='gray',thespeed = 1,coord:tuple=(0,0)):
        super().__init__()
        self.langle = langle
        self.coord = coord
        if self.coord[0] != 0:
            self.rayon = self.coord[0]/cos(pi*self.langle/180)
        else:
            if self.coord[1] != 0:
                self.rayon = self.coord[1]/sin(pi*self.langle/180)
            else:
                self.rayon = 0
        self.thespeed = thespeed
        self.shape('circle')
        self.shapesize(1)
        self.color(color)
        self.penup()
        self.goto(coord)

    def move(self):
        self.langle += self.thespeed
        x_pos = self.rayon*cos(pi*self.langle/180)
        y_pos = self.rayon*sin(pi*self.langle/180)
        self.pendown()
        self.goto(x_pos,y_pos)
        