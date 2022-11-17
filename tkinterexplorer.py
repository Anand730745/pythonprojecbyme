from tkinter import *
root=Tk()
root.title('MY NAME IS KHAN')
def sum():
    a=5
    b=4
    y=a+b
    print(y)
btn=Button(root,text='add',bg='white',fg='black', font=("Comic Sans Ms",20,"bold"),command=sum)
btn.pack()

root.geometry("400x300+200+100")
root.resizable(0,0)
root.wm_iconbitmap("rinky.ico")
root.mainloop()