from turtle import *
t=Turtle()
sc=Screen()
sc.title('hamara desh mahan')
sc.bgcolor('white')
sc.bgpic('bharat.gif')
t.speed(10)



t.pu()
t.goto(-300,350)
t.pd()

t.hideturtle()
t.fillcolor('red')
t.begin_fill()
t.fd(300)
t.right(90)
t.fd(50)
t.right(90)
t.fd(300)
t.right(90)
t.fd(50)
t.end_fill()
t.right(180)
t.fd(50)
t.left(90)


t.fd(300)
t.right(90)
t.fd(50)
t.right(90)
t.fd(300)
t.right(90)
t.fd(50)

t.right(180)
t.fd(50)
t.left(90)

t.fillcolor('green')
t.begin_fill()
t.fd(300)
t.right(90)
t.fd(50)
t.right(90)
t.fd(300)
t.right(90)
t.fd(50)
t.end_fill()
t.fd(100)

t.fillcolor('black')
t.begin_fill()
t.fd(10)
t.left(90)
t.fd(15)
t.left(90)

t.fd(600)
t.right(180)
t.fd(600)
t.right(90)
t.fd(15)
t.right(90)
t.fd(600)
t.end_fill()

t.left(90)
t.fd(50)
t.right(90)
t.fd(30)
t.right(90)
t.fd(115)
t.right(90)
t.fd(30)
t.right(90)
t.fd(50)
t.fd(15)
t.pu()
t.fd(50)
t.right(90)
t.fd(30)
t.left(90)
t.pd()

t.fd(50)
t.right(90)
t.fd(30)
t.right(90)
t.fd(215)
t.right(90)
t.fd(30)
t.right(90)
t.fd(50)
t.right(180)
t.fd(50)
t.left(90)
t.fd(30)
t.right(90)


t.fd(50)
t.left(90)
t.fd(30)
t.right(90)
t.right(180)
t.fd(315)
t.left(90)
t.fd(30)
t.left(90)
t.fd(50)

#t.pencolor('black')
t.right(90)
t.pu()
t.fd(600)
t.pd()

t.pencolor('black')
t.right(90)
t.fd(30)
t.pu()
t.right(90)
t.fd(25)
t.pd()
t.circle(22)
#t.left(180)
t.right(90)
t.pu()
t.goto(-148,275)
t.pd()
t.setheading(90)
for _ in range(24):
    t.fd(22)
    t.pu()
    t.goto(-148,275)
    t.right(35)
    t.pd()

t.pu()
t.goto(-80,60)
t.pd()



mainloop()


done()







