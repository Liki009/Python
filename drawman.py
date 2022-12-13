import turtle
from random import randint
def drawalpha(a,clr=False):
    turtle.penup()
    if clr:
        r=round((randint(0,256)/255.0),3)
        g=round((randint(0,256)/255.0),3)
        b=round((randint(0,256)/255.0),3)
        turtle.color(r,g,b)
        turtle.speed(1)
    if a=='a':
        turtle.pendown()
        turtle.left(60)
        turtle.forward(90)
        turtle.right(140)
        turtle.forward(90)
        turtle.back(45)
        turtle.left(260)
        turtle.forward(40)
        turtle.setheading(0)
        turtle.penup()
    if a=='b':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(115)
        turtle.right(90)
        for i in range(90):
            turtle.forward(1)
            turtle.right(2)
        turtle.right(180)
        for i in range(90):
            turtle.forward(1)
            turtle.right(2)
        turtle.setheading(0)
        turtle.penup()
    if a=='c':
        turtle.forward(63)
        turtle.pendown()
        turtle.left(180)
        for i in range(190):
            turtle.forward(1)
            turtle.right(1)
        turtle.setheading(0)
        turtle.penup()
    if a=='d':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(115)
        turtle.right(90)
        for i in range(180):
            turtle.forward(1)
            turtle.right(1)
        turtle.setheading(0)
        turtle.penup()
    if a=='e':
         turtle.pendown()
         turtle.forward(40)
         turtle.back(40)
         turtle.left(90)
         turtle.forward(100)
         turtle.right(90)
         turtle.forward(40)
         turtle.back(40)
         turtle.right(90)
         turtle.forward(50)
         turtle.left(90)
         turtle.forward(20)
         turtle.penup()
    if a=='f':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(40)
        turtle.back(40)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(20)
        turtle.penup()
    if a=='g':
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(100)
        turtle.pendown()
        turtle.left(90)
        for i in range(120):
            turtle.forward(1)
            turtle.left(1.5)
        turtle.left(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.setheading(0)
        turtle.penup()
    if a=='h':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.back(50)
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(50)
        turtle.back(100)
        turtle.setheading(0)
        turtle.penup()
    if a=='i':
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.penup()
    if a=='as':
        
        turtle.pendown()
        
        turtle.setheading(0)
        turtle.penup()
    if a=='j':
        turtle.forward(30)
        turtle.pendown()
        for i in range(50):
            turtle.back(1)
            turtle.right(2)
        for i in range(100):
            turtle.forward(1)
            turtle.left(2)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.back(40)
        turtle.setheading(0)
        turtle.penup()
        
        
        
        
"testeting"
j=100
for i in "j":
    drawalpha(i)
    turtle.goto(j,0)
    j=j+60
"turtle.goto(0,0)"
    
    

        
