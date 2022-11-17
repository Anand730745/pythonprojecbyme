from tkinter import *
root=Tk()
root.title("LEARNER")
def msg():
    c=float(f.get())+float(s.get())
    print(c)
    u.set(c)
    f.set('')
    s.set('')


#root.title('TECHANAND')
label1=Label(root,text="enter the number",font=("comic Sans Ms",20,"bold"),bg="blue",fg="yellow")
label1.grid(row=0,column=0)

f=StringVar()
#f=IntVar()
text1=Entry(root,font=("comic Sans Ms",20,"bold"),textvariable=f,justify='right',width=20,bd=10)
text1.grid(row=0,column=1)


label2=Label(root,text="enter the number",font=("comic Sans Ms",20,"bold"),bg="blue",fg="yellow")
label2.grid(row=1,column=0)

s=StringVar()
#s=IntVar()
text2=Entry(root,font=("comic Sans Ms",20,"bold"),textvariable=s,justify='right',width=20,bd=10)
text2.grid(row=1,column=1)

btn=Button(root,text='add',bg='white',fg='black', font=("Comic Sans Ms",20,"bold"),command=msg)
btn.grid(row=2,column=0,columnspan=2)

u=StringVar()
#u=IntVar()
result=Label(root, text="",font=("comic Sans Ms",20,"bold"),textvariable=u)
result.grid(row=7,column=0,columnspan=2)

root.geometry("600x350+50+50")
root.resizable(0,0)
root.wm_iconbitmap("rinky.ico")
root.mainloop()