from graph import *

penColor(255,0,255)
penSize(5)
brushColor("yellow")
circle(0, 0, 50)
brushColor(0,0,0)
circle(-13, 13, 2)
circle(13, 13, 2)
brushColor(255,0,0)

circle(-13, 13, 4)
circle(13, 13, 4)

brushColor(0,0,0)
rectangle(-13, -13, 13, 10)
penSize(24)
line(13,19,45,45)
line(-13,19,-45,-45)
run()