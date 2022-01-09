from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox  
window=Tk()
window.geometry('1280x770+125+10')
window.maxsize(width = 1280,height = 770)
window.minsize(width = 1280,height = 770)
canvas=Canvas(window,width=1280,height=720)
image1=ImageTk.PhotoImage(Image.open("F:\Suyash\Python\Python project\HMS\login.png"))
canvas.create_image(0,0,anchor=NW,image=image1)
canvas.place(x=0,y=50)

window.title("Hospital Management System")
frame=Frame(window,width=1280,height=100,bg="light blue")
frame.place(x=0,y=0)
l1=Label(window,text="Welcome To Global Health Care",bg="light blue",font=('Times',40,'bold'))
l1.place(x=330,y=20)

l2=Label(window,text="USERNAME",font=('Times',20,'bold'),bg="white")
l2.place(x=250,y=250)
global user,pwd
global e1,e2
user=StringVar()
pwd=StringVar()
e1=Entry(window,textvar='user',bd=3,width=20,font=('Times',16,'bold'))
e1.place(x=250,y=300)


l3=Label(window,text="PASSWORD",font=('Times',20,'bold'),bg="white")
l3.place(x=250,y=350)
e2=Entry(window,textvar='pwd',show='✱',bd=3,width=20,font=('Times',16,'bold'))
e2.place(x=250,y=400)

from menu import * 

def login():
    a=e1.get()
    b=e2.get()
    if a=="" and b=="":
        menu(window)
           
    else:
        messagebox.showinfo("Warning !","Your Username and Password is Wrong")      



b=Button(window,text="LOGIN",bg="light blue",bd=10,font=('Times',20,'bold'),width=8,command=login)
b.place(x=285,y=470)

window.mainloop()


    









    
