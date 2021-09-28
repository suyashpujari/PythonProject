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


from tkinter import *
from doctor import doctor
from patient import patient
from appointment import appointment
from reciept import reciept_call
from about_us import about_us1
def admin():
        global window1
        window1=Tk()
        window1.geometry('1600x1100')
        window1.title("Hospital Management System")
        
        frame1=Frame(window1,width=1600,height=150,bg="light blue")
        frame1.place(x=0,y=0)
        l1=Label(window1,text="Global Health Care",bg="light blue",font=('Times',40,'bold'))
        l1.place(x=600,y=10)
        la=Label(window1,text="ADMIN PANEL",bg="light blue",font=('Times',30))
        la.place(x=680,y=80)
        
        b1=Button(window1,text="DOCTOR",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=doctor)
        b1.place(x=10,y=200)

        b2=Button(window1,text="PATIENT",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=patient)
        b2.place(x=10,y=300)

        b3=Button(window1,text="APPOINTMENT",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=appointment)
        b3.place(x=10,y=400)

        b4=Button(window1,text="RECIEPT",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=reciept_call)
        b4.place(x=10,y=500)

        b5=Button(window1,text="ABOUT US",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=about_us1)
        b5.place(x=10,y=600)

        b6=Button(window1,text="LOGOUT",bg="#00d3d6",bd=15,font=('Times',18,'bold'),width=15,command=logout)
        b6.place(x=10,y=700)

        window.destroy()
               
        

def login():
    a=e1.get()
    b=e2.get()
    if a=="" and b=="":
        admin()
    else:
        messagebox.showinfo("Warning !","Your Username and Password is Wrong")
def logout():
    window1.destroy()        

          
b=Button(window,text="LOGIN",bg="light blue",bd=10,font=('Times',20,'bold'),width=8,command=login)
b.place(x=285,y=470)

window.mainloop()


    









    
