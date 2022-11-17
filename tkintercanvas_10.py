from tkinter import *
root=Tk()
canvas=Canvas(root,height=600,width=700,bg="yellow")
canvas.pack()
#line=canvas.create_line(20,30,400,400,fill="red",width="5")
#reactangle=canvas.create_rectangle(30,300,100,100,fill="red",width="5")
# point=[200,110,480,200,280,280,200,110]
# poly=canvas.create_polygon(point,fill="green")
arc=canvas.create_arc(100,100,300,300,fill="orange",outline="white",extent=-180)
filename = PhotoImage(file = "anna.gif")
image = canvas.create_image(200, 200, anchor=NE, image=filename)

root.geometry("800x600+120+120")
root.mainloop()