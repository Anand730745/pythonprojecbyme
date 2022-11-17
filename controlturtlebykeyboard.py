from turtle import *
sc=Screen()
t=Turtle()
t.shape('turtle')
def aage():
    t.fd(100)
    k = 20
    for i in range(10):
        t.pu()
        t.setpos(30, 30)
        t.pd()
        #t.stamp()
        k=10
def pichhe():
    t.bk(100)


def baye():
    t.left(90)



def daye():
    t.right(90)


sc.onkey(aage,'Up')
sc.onkey(pichhe,'Down')
sc.onkey(baye,'Left')
sc.onkey(daye,'Right')
sc.listen()

done ()