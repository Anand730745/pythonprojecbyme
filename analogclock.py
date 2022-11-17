
from turtle import *
import time
t=Turtle()
sc=Screen()
t.speed(10)
t.hideturtle()
time.time()
t.pensize(3)

sc.bgcolor('black')
sc.title('my analog clock')
sc.tracer(0)
def clock(h,m,s,t):
    t.pencolor('green')
    t.pu()
    t.goto(0,210)
    t.setheading(180)
    t.pd()
    t.circle(210)
    #clock hand
    t.pu()
    t.goto(0,0)
    t.setheading(90)
    for i in range(12):
        t.fd(185)
        t.pd()
        t.fd(20)
        t.pu()
        t.goto(0,0)
        t.right(30)

    # clock minute hand
    t.pu()
    t.goto(0, 0)
    t.setheading(90)
    for i in range(60):

        t.fd(200)
        t.pd()
        t.fd(10)
        t.pu()
        t.goto(0, 0)
        t.right(6)


    #draw no on clock face
    #one
    t.pu()
    t.goto(0,0)
    t.setheading(60)
    t.fd(145)
    t.setheading(0)
    t.fd(15)
    t.write(1,move=False,align='center',font=('arial',20,'normal'))

    # two
    t.pu()
    t.goto(0, 0)
    t.setheading(30)
    t.fd(135)
    t.setheading(0)
    t.fd(35)
    t.write(2, move=False, align='center', font=('arial', 20, 'normal'))

    # three
    t.pu()
    t.goto(0, 0)
    t.setheading(352)
    t.fd(150)
    t.setheading(0)
    t.fd(25)
    t.write(3, move=False, align='center', font=('arial', 20, 'normal'))

    # four
    t.pu()
    t.goto(0, 0)
    t.setheading(315)
    t.fd(150)
    t.setheading(0)
    t.fd(45)
    t.write(4, move=False, align='center', font=('arial', 20, 'normal'))

    # five
    t.pu()
    t.goto(0, 0)
    t.setheading(290)
    t.fd(178)
    t.setheading(0)
    t.fd(25)
    t.write(5, move=False, align='center', font=('arial', 20, 'normal'))

    # six
    t.pu()
    t.goto(0, 0)
    t.setheading(270)
    t.fd(188)
    #t.setheading(0)
    #t.fd(15)
    t.write(6, move=False, align='center', font=('arial', 20, 'normal'))

    # seven
    t.pu()
    t.goto(0, 0)
    t.setheading(258)
    t.fd(170)
    t.setheading(180)
    t.fd(48)
    t.write(7, move=False, align='center', font=('arial', 20, 'normal'))

    # eight
    t.pu()
    t.goto(0, 0)
    t.setheading(228)
    t.fd(150)
    t.setheading(180)
    t.fd(45)
    t.write(8, move=False, align='center', font=('arial', 20, 'normal'))

    # nine
    t.pu()
    t.goto(0, 0)
    t.setheading(185)
    t.fd(200)
    t.setheading(0)
    t.fd(25)
    t.write(9, move=False, align='center', font=('arial', 20, 'normal'))

    # ten
    t.pu()
    t.goto(0, 0)
    t.setheading(158)
    t.fd(180)
    t.setheading(0)
    t.fd(25)
    t.write(10, move=False, align='center', font=('arial', 20, 'normal'))

    # eleven
    t.pu()
    t.goto(0, 0)
    t.setheading(120)
    t.fd(145)
    t.setheading(180)
    t.fd(15)
    t.write(11, move=False, align='center', font=('arial', 20, 'normal'))

    # twelve
    t.pu()
    t.goto(0, 0)
    t.setheading(90)
    t.fd(150)
    #t.setheading()
    #t.fd(15)
    t.write(12, move=False, align='center', font=('arial', 20, 'normal'))

    # draw hour hand
    t.pu()
    t.goto(0,0)
    t.pencolor('red')
    t.setheading(90)
    angle=(h/12)*360
    t.rt(angle)
    t.pd()
    t.fd(80)
    #mainloop()

# draw minute hand
    t.pu()
    t.goto(0,0)
    t.pencolor('blue')
    t.setheading(90)
    angle=(m/60)*360
    t.rt(angle)
    t.pd()
    t.fd(120)
    #mainloop()

    # draw second hand
    t.pu()
    t.goto(0, 0)
    t.pencolor('yellow')
    t.setheading(90)
    angle = (s / 60) * 360
    t.rt(angle)
    t.pd()
    t.fd(150)


    #designed by
    t.pu()
    t.goto(0,0)
    #t.pencolor('blue')
    t.setheading(268)
    t.fd(125)
    t.setheading(0)
    t.fd(5)
    t.write('www.techanand.com', move=False, align='center', font=('arial', 10, 'normal'))



while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    clock(h,m,s,t)
    time.sleep(1)
    sc.update()
    t.clear()

#mainloop()
#t.done()