from tkinter import *
class myname:
    def msg(self):
        print("present sir")

    def __int__(self,window):
        self.btn=Button(window,text="attendence",command=self.msg)
        self.btn.pack()

root=Tk()
win=myname(root)
root.mainloop()