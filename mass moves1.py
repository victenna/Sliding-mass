import turtle,time,math
wn=turtle.Screen()
wn.setup(1300,900)
wn.bgcolor('white')
turtle.tracer(1,0)
t=[]
line=[]
clr=['red','blue','gold','grey']
image=['image00.gif','image11.gif','image22.gif','image33.gif']
for i in range(4):
    if i<4:
        wn.addshape(image[i])
        t.append(turtle.Turtle())
        t[i].shape(image[i])
        t[i].up()
    line.append(turtle.Turtle('circle'))
    line[i].up()
    line[i].color(clr[i])
    line[i].shapesize(0.2)
    line[i].pensize(3)
    line[i].setheading(20+10*i)
    line[i].goto(-212,-209)
    line[i].down()
    

t[0].goto(100,0)
t[1].goto(-400,350)
t[2].goto(540,-275)
t[3].goto(120,-10)
t[3].hideturtle()
t[2].setheading(-90)
for i in range (455):
    t[1].fd(1)
    t[2].fd(1)
    line[0].fd(1)
    line[1].fd(1)
    line[2].fd(1)
    line[3].fd(1)
        
    time.sleep(0.01)
t[3].showturtle()
