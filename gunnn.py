from random import randrange as rnd, choice
import tkinter as tk
import math
import time
from PIL import ImageTk, Image
# понадобится модуль pillow
from random import randrange as rnd, choice
# print (dir(math))
aa=1
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g=1
points=0
id_points=0
id_points = canv.create_text(30,30,text = points,font = '28')
g=1
d=0
xx=yy=0
id_tx = canv.create_text(300,30,text = 'в кляксу не стрелять',font = '28')
rr=10
img = ImageTk.PhotoImage(Image.open("pic.png"))
def click(event):
 canv.delete(id_tx)
panel = tk.Label(canv, image = img, height=2*rr, width=2*rr)

canv.bind('<Key>', click )

xx=yy=0
rr=40
w=2
wx=0
wy=0
wvx=0
wvy=0
bx=0
by=0
bvx=0
bvy=0
svx=0
svy=0
d=0
q=0
w=2
class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def move(self):
        global bx, by, bvx, bvy, q
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if(self.x-self.r<=0 and q==0):
         self.vx=-self.vx
         q=1
         print('dfg')
        if(self.x-self.r>=10):
         q=0
        if(self.x+self.r>=800):
         print('ktf')
         self.vx=-self.vx
        if(self.y-self.r<=0):
         self.vy=-self.vy
         print('gf')

        if(self.y+self.r>=600):
         self.vy=-self.vy
         print('ktuyff')
         print(self.y)
        bx=self.x
        by=self.y
        bvx=self.x
        bvy=self.y
        self.x += self.vx
        self.vy -= g
        self.y -= self.vy
        
        self.set_coords()
    def hittest(self, obj):
        d=(self.x-obj.x)*(self.x-obj.x)+(self.y-obj.y)*(self.y-obj.y)
        if(d<(self.r+obj.r)*(self.r+obj.r)):
         return True
         
        else:
         return False


class gun():
    def __init__(self, x=40, y=450):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, g=100):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an) 
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self, x=40, y=450, w=0):
        self.w=w
        self.points = 0
        self.live = 1
        # FIXME: doesn't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()
        
    def new_target(self, w=None):
        global panel
        self.f=1
        
        vx = self.vx = -2
        vy = self.vy = -1
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        rr=self.r
        if (self.w==0):
         color = self.color = 'red'
         canv.coords(self.id, x-r, y-r, x+r, y+r)
         canv.itemconfig(self.id, fill=color)

        if (self.w==1):
         color = self.color = 'grey'
         panel.destroy()
         panel = tk.Label(canv, image = img, height=2*rr, width=2*rr)
         panel.place(x = x-rr, y = y-rr)
        

    def hit(self):
        """Попадание шарика в цель."""
        global points, id_points, panel
        canv.coords(self.id, -10, -10, -10, -10)
        canv.delete(id_points)
        if (self.w==0):
         points=points+1
        if (self.w==1):
         points=points-1
         panel.destroy()

        self.f=0
        canv.delete(id_points)
        id_points = canv.create_text(30,30,text = points,font = '28')    
    def t(self):
        global wx, wy, wvx, wvy, bx, by, bvx, bvy, ax, ay, svx, svy, panel
        if(self.f==1):
            if(self.x-self.r<=0):
             self.vx=-self.vx
             print('dfg')

            if(self.x+self.r>=800):
             print('ktf')
             self.vx=-self.vx
            if(self.y-self.r<=0):
             self.vy=-self.vy
             print('gf')

            if(self.y+self.r>=600):
             self.vy=-self.vy
             print('ktuyff')
             print(self.y)
            if (self.w==1):
             wx=self.x
             wy=self.y
             wvx=self.vx
             wvy=self.vy
             ax=0.5*bx+bvx*0+0.5*wx+wvx*0
             ay=0.5*by+bvy*0+0.5*wy+wvy*0
             self.vx=(ax-wx)*0.1
             self.vy=(ay-wy)*0.1
            
             
            if (self.w==1 or self.w==0):
             self.x = self.x +  self.vx
             self.y = self.y + self.vy
             
           
            x = self.x 
            y = self.y 
            r = self.r
            if (self.w==0):
             canv.coords(self.id, x-r, y-r, x+r, y+r)
             
             color = self.color
            if (self.w==1):
             panel.destroy()
             #уничтожили картинку
             
             #создали новые координаты
             #canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
             panel = tk.Label(canv, image = img, height=2*rr, width=2*rr)
             #создали картинку заново
             panel.place(x = x-rr, y = y-rr)
             # поместили картинку в координаты 
             #root.after(1000,t)




t1 = target(w=0)
t2 = target(w=1)

#screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    
    global gun, t1, t2, screen1, balls, bullet, x, w
    for b in balls:  
     canv.delete(b.id)
   
    t1.new_target(w=0)
    t2.new_target(w=1)
    
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or balls or t2.live:
        for b in balls:
            b.move()
            
            t1.t()
            t2.t()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                self=t1
                canv.delete(t1)
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                self=t2
                canv.delete(t2)

            if  t1.live==0:
                for b in balls:  
                   canv.delete(b.id)
                new_game()

        canv.bind('<Button-3>', new_game)
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()

    #canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()
