from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
vx = [10, 20, 20]
vy=[20, 10, 20]
x=[400, 200, 300]
y=[300, 200, 300]
r=[50, 80, 40]
a=0

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    
    global x,y,r,vx,vy, a
    canv.delete(ALL)
    for i in (0,1,2):
     if(x[i]-r[i]<=0):
         vx[i]=rnd(1,3)
     if(x[i]+r[i]>=800):
         vx[i]=rnd(1,3)*(-1)
     if(y[i]-r[i]<=0):
         vy[i]=rnd(1,3)
     if(y[i]+r[i]>=600):
         vy[i]=rnd(1,3)*(-1)

     x[i] = x[i] + vx[i]
     y[i] = y[i]+vy[i]
     if(i<2):
      canv.create_oval(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i], fill=choice(colors), width=0)
     if(i==2):
      canv.create_rectangle(x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i])
    root.after(10, new_ball)
        
        
def click(event):
    global x,y,r,vx,vy, a
    for i in (0,1,2):
     if(i<2):
      if((x[i]-event.x)**2+(y[i]-event.y)**2<r[i]**2):
       a=a+1
       print(a)
      #if((x[i]-event.x)**2+(y[i]-event.y)**2>r[i]**2):
         # print('')
     if(i==2):
      if(event.x<x[i]+r[i] and x[i]<event.x and event.x<y[i]+r[i] and y[i]<event.x):
       a=a+2 
       print(a)
     # if(event.x<x[i]+r[i] or x[i]<event.x or event.x<y[i]+r[i] or y[i]<event.x):
      # print('')
new_ball()
canv.bind('<Button-1>', click)
mainloop()