from  tkinter import *
import time
root=Tk()
canvas=Canvas(root,height=600,width=800)
canvas.pack()
ball=canvas.create_oval(10,10,100,100,fill="red")
ball1=canvas.create_oval(10,10,100,100,fill="green")
'''for i in range(400):

    canvas.move(ball,1,0)
    root.update()
    print()
    time.sleep(0.01)'''

xspeed=1
yspeed=10
xspeed1=2
yspeed1=11
while True:
    canvas.move(ball,xspeed,yspeed)
    pos=canvas.coords(ball)
    '''
    pos=[left(0),top(1),right(2),bottom(3)]
    '''
    if pos[3]>=600 or pos[1]<=0:
        yspeed=-yspeed
    if pos[2]>=800 or pos[0]<=0:
        xspeed=-xspeed

    canvas.move(ball1, xspeed1, yspeed1)
    pos = canvas.coords(ball1)
    '''
    pos=[left(0),top(1),right(2),bottom(3)]
    '''
    if pos[3] >= 600 or pos[1] <= 0:
        yspeed1 = -yspeed1
    if pos[2] >= 800 or pos[0] <= 0:
        xspeed1 = -xspeed1
    #print(pos)
    root.update()
    time.sleep(0.01)

root.title("my ball game")
root.resizable(0,0)
root.geometry("800x600+10+10")
root.mainloop()