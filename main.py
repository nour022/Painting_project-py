from turtle import Turtle,Screen
import random
item=Turtle()
screen=Screen()
#screen.bgcolor("black")
screen.colormode(255)
""" Random Colors """
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
y=-200
item.speed("fastest")
for _ in range(6):
    y+=50
    item.penup()
    item.goto(-200,y)
    item.pendown()
    for _ in range(20):
        item.color(random_color())
        item.dot(10)
        item.penup()
        item.forward(20)
        item.pendown()
item.left(90)
x=-200
for _ in range(7):
    x+=50
    item.penup()
    item.goto(x,-200)
    item.pendown()
    for _ in range(18):
        item.color(random_color())
        item.dot(10)
        item.penup()
        item.forward(20)
        item.pendown()


screen.exitonclick()