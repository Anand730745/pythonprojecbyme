from tkinter import *
root=Tk()

label1=Label(root,text="KARMA BROTHER'S MANAGEMENT SYSTEM"
             ,font=('Algerian',50,'bold'),bg="red",fg="yellow")
label1.place(x=0,y=30)

label2=Label(root,text="Admin Login Page",font=('Broadway',30,'bold'))
label2.place(x=470,y=180)

lb1=LabelFrame(root,text="hi")

label3=Label(lb1,text="Enter User Name",font=('Broadway',25,'bold'))
label3.place(x=300,y=310)

ent=Entry(lb1,font=('Broadway',25,'bold'))
ent.place(x=700,y=310)

label4=Label(lb1,text="Enter password",font=('Broadway',25,'bold'))
label4.place(x=300,y=410)

ent1=Entry(lb1,font=('Broadway',25,'bold'))
ent1.place(x=700,y=410)


btn=Button(lb1,text="Login",font=('Broadway',25,'bold'))
btn.place(x=650,y=540)

lb1.place(x=650,y=540)

root.title("KARMA_BROTHER'S MANGEMENT")
root.mainloop()