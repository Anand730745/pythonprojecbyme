from turtle import *
t=Turtle()
sc=Screen ()
sc.bgpic('india2.gif')
sc=sc.bgcolor('white')
t.pencolor('white')
t.pensize(10)
t.speed(11)
t.pu()
t.goto(-150, 230)
t.pd()

l=['blue','black','red',]
for i in range(3):
    t.pencolor(l[i])
    t.circle(60)
    t.pu()
    t.fd(150)
    t.pd()

t.pu()
t.goto(-75,170)
t.pd()
l=['yellow','green']
for j in range(2):
    t.pencolor(l[j])
    t.circle(60)
    t.pu()
    t.fd(150)
    t.pd()
done()