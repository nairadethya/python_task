from tkinter import *
from random import randint
from sympy import root

root=Tk()

root.geometry("300x300")
root.title("Python task")
root.resizable(False,False)

canvas=Canvas(root, width=300, height=300)
canvas.pack()

ball=canvas.create_oval(140,140,150,150, fill="green3")
canvas.create_rectangle(3,3,300,300)

xspeed=4
yspeed=3

def move_ball():
   global xspeed, yspeed
   canvas.move(ball, xspeed, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords(ball)
   if leftpos <=0 or rightpos>=300:
      xspeed=-randint(1,3)*xspeed
      yspeed=-randint(1,3)*yspeed
   if toppos <=0 or bottompos >=300:
      yspeed=-randint(1,3)*yspeed
      xspeed=-randint(1,3)*xspeed

   canvas.after(50,move_ball)

canvas.after(50, move_ball)

root.mainloop()