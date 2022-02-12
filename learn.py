
from turtle import *
import turtle
 
lan = turtle.Turtle()

# 画正方形
lan.forward(100)
lan.left(90)
lan.forward(100)
lan.left(90)
lan.forward(100)
lan.left(90)
lan.forward(100)

# for i in range(4):
#     lan.forward(100)
#     lan.left(90)
# lan.right(90) 

# 瞬移到(100,100)
lan.goto(100,100)

# 到(0,100)
lan.right(90)
lan.forward(100)

# 瞬移到(100,0)
lan.goto(100,0)

lan.home()

lan.circle(60)
lan.circle(100)

lan.dot(109)

# turtle.bgcolor("blue")

lan.fillcolor("red")

# lan.circle(1000)

lan.pencolor("green")

lan.circle(90)

lan.shape("turtle")

lan.clear()







turtle.done()
 