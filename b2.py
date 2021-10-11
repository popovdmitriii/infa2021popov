from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
vx=rnd(0,10)
vy=rnd(0,10)
r = rnd(30,50)
x = rnd(100,700)
y = rnd(100,500)
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
   
colors = ['red', 'orange', 'yellow', 'green', 'blue']

print(x,y)
def new_ball():
    canv.delete(ALL)
    x==x+vx
    y==y+vy
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(100,new_ball)
        
new_ball()
mainloop()