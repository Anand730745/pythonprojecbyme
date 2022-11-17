from tkinter import *
root=Tk()
def left(event=''):
    print("I LOVE YOU")
btn=Button(root,text=' DO YOU LOVE ME ?',font=("Airel",15,'bold'),command=left,)
btn.pack()
root.bind("<Control-c>",left)
root.geometry("250x300+120+130")
root.mainloop()