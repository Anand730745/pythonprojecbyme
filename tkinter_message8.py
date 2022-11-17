from tkinter import *
from tkinter import messagebox
root=Tk()
def msg():
    result=messagebox.showerror(title="Question Box",message="do you want to play?")
    print(result)
    if result==True:
        print("play the game")
    else:
        print("exit the game")

btn=Button(root,text="message checking",command=msg)
btn.pack()
root.geometry("300x400+120+120")
root.wm_resizable(0,0)
root.mainloop()