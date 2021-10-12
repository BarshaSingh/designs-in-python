import turtle
import tkinter as TK
col =('red','yellow','green','cyan','blue','white')
t=turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(30)
for i in range(100):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
