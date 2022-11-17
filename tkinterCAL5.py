from tkinter import *
root=Tk()

def btntouch(number):
    global val
    val=val+str(number)
    c.set(val)

def btnclear():
    global val
    val=""
    c.set("")

def btnequal():
    global val
    result=str(eval(val))
    c.set(result)

def btnpai():
    #global val
    g="3.141592"
    c.set(g)

def btnfacto():
    global val
    i = int(input("enter any number to find fartorial="))
    f = 1
    while i > 0:
        f = f * i
        i = i - 1
        c.set(f)
        print(f)


c=StringVar()
display=Entry(root,font=("comic Sans Ms",20,"bold"),bd=12,bg="skyblue",fg="black",justify="right",textvariable=c)
display.grid(row=0,columnspan=4)
val=""

btn7=Button(root,text="7",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(7))
btn7.grid(row=1,column=0)

btn8=Button(root,text="8",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(8))
btn8.grid(row=1,column=1)

btn9=Button(root,text="9",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(9))
btn9.grid(row=1,column=2)

btn_add_=Button(root,text="+",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch("+"))
btn_add_.grid(row=1,column=3)

btn4=Button(root,text="4",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(4))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(5))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(6))
btn6.grid(row=2,column=2)

btn_sub_=Button(root,text="-",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch("-"))
btn_sub_.grid(row=2,column=3)

btn1=Button(root,text="1",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(1))
btn1.grid(row=3,column=0)

btn2=Button(root,text="2",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(2))
btn2.grid(row=3,column=1)

btn3=Button(root,text="3",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(3))
btn3.grid(row=3,column=2)

btn_multi_=Button(root,text="*",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch("*"))
btn_multi_.grid(row=3,column=3)

btn_zero_=Button(root,text="0",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch(0))
btn_zero_.grid(row=4,column=0)

btn_cancle_=Button(root,text="C",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command= btnclear)
btn_cancle_.grid(row=4,column=1)

btn_divide_=Button(root,text="÷",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=lambda:btntouch("/"))
btn_divide_.grid(row=4,column=2)

btn_equal_=Button(root,text="=",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=btnequal)
btn_equal_.grid(row=4,column=3)

btn_pai_=Button(root,text="π",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=btnpai)
btn_pai_.grid(row=5,column=0)

btn_fact_=Button(root,text="!",font=("comic Sans Ms",20,"bold"),bd=12,height=1,width=3,command=btnfacto)
btn_fact_.grid(row=5,column=1)

root.geometry("350x530+1100+250")
root.resizable(0,0)
root.title("my calculator")
root.wm_iconbitmap("pinky.ico")
root.mainloop()