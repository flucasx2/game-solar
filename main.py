from turtle import Screen
from soleil import Soleil
from planete import Planete
import time

screen = Screen()
screen.title("Système solaire")
screen.tracer(0)

soleil = Soleil()

info_pla = [
    (0,'green',4,(150,0)),
    (45,'red',5,(125,125)),
    (90,'gray',3,(0,175)),
    (135,'brown',6,(-200,200))
]

listepalnete:list[Planete] = []

for ang,col,spe,coor in info_pla:
    p = Planete(ang,col,spe,coor)
    listepalnete.append(p)


is_move = True
while is_move:
    time.sleep(0.5)
    screen.update()
    for elt in listepalnete:
        elt.move()

screen.exitonclick()