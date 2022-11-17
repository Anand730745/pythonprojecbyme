from tkinter import *
from tkinter import ttk
def msg():
    print(b.get())
root=Tk()
l=["january","february","march","april","may","june","july","august","september","october","november","december"]
b=ttk.Combobox(root,values=l)
b.set("select month")
b.pack()
btn=Button(root,text="Calender",command=msg)
btn.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()