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
label1.place(x=50,y=80)

f=StringVar()
#f=IntVar()
text1=Entry(root,font=("comic Sans Ms",20,"bold"),textvariable=f,justify='right',width=20,bd=10)
text1.place(x=400,y=80)


label2=Label(root,text="enter the number",font=("comic Sans Ms",20,"bold"),bg="blue",fg="yellow")
label2.place(x=50,y=200)

s=StringVar()
#s=IntVar()
text2=Entry(root,font=("comic Sans Ms",20,"bold"),textvariable=s,justify='right',width=20,bd=10)
text2.place(x=400,y=200)

btn=Button(root,text='add',bg='white',fg='black', font=("Comic Sans Ms",20,"bold"),command=msg)
btn.place(x=350,y=300)

u=StringVar()
#u=IntVar()
result=Label(root, text="",font=("comic Sans Ms",20,"bold"),textvariable=u)
result.place(x=350,y=370)

root.geometry("800x450+50+50")
root.resizable(0,0)
root.wm_iconbitmap("rinky.ico")
root.mainloop()