from tkinter import *
import  random
import time
root=Tk()
canvas = Canvas(root, height=600, width=800)
canvas.pack()
class ballgame:
    def __init__(self,colour,size):
        self.ball = canvas.create_oval(10, 10, size,size, fill=colour)
        self.xspeed = random.randrange(1,10)
        self.yspeed = random.randrange(1,10)

    def animate(self):
        canvas.move(self.ball, self.xspeed, self.yspeed)
        pos = canvas.coords(self.ball)
        if pos[3] >= 600 or pos[1] <= 0:

            self.yspeed = -self.yspeed
        if pos[2] >= 800 or pos[0] <= 0:

            self.xspeed = -self.xspeed

moving_ball=[]
color=["red","yellow","gold","blue","orange","grey","green"]
for i in range(500):
    moving_ball.append(ballgame(random.choice(color),random.randrange(50,100)))
while True:
    for j in moving_ball:
        j.animate()
    root.update()
    time.sleep(0.001)

#root.geometry("800x600+120+10")
#mainloop()

