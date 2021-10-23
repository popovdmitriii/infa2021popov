from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g=1
d=0
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
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
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
    def __init__(self, x=40, y=450):
        self.points = 0
        self.live = 1
        # FIXME: doesn't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        self.new_target()

    def new_target(self):
        self.f=1
        vx = self.vx = -2
        vy = self.vy = -1
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        self.f=0
        canv.itemconfig(self.id_points, text=self.points)
    def t(self):
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
            self.x = self.x +  self.vx
            self.y = self.y + self.vy
            x = self.x 
            y = self.y 
            r = self.r 
            canv.coords(self.id, x-r, y-r, x+r, y+r)
            color = self.color
            canv.itemconfig(self.id, fill=color)



t1 = target()
t2 = target()

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet, x
    t1.new_target()
    t2.new_target()

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
               
                canv.itemconfig(screen1, text='Вы уничтожили цель 1за ' + str(bullet) + ' выстрелов')
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            
                canv.itemconfig(screen1, text='Вы уничтожили цель2 за ' + str(bullet) + ' выстрелов')
            if  t1.live==0 and t2.live==0:
                new_game()

        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

mainloop()