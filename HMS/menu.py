from tkinter import *
from doctor import doctor
from patient import patient
from appointment import appointment
from reciept import reciept_call
from about_us import about_us1

def menu(window):
    global window1,winvar
    winvar=window
    window1=Toplevel(window)
    window1.geometry('1280x770+125+10')
    window1.maxsize(width = 1280,height = 770)
    window1.minsize(width = 1280,height = 770)
    window1.title("Hospital Management System")

    img = PhotoImage(file="menu.png")
    label = Label(window1,image=img)
    label.place(x=0, y=45)

    frame1=Frame(window1,width=1280,height=125,bg="#787fff")
    frame1.place(x=0,y=0)
    l1=Label(window1,text="Global Health Care",bg="#787fff",font=('Times',40,'bold'))
    l1.place(x=450,y=5)
    la=Label(window1,text="ADMIN PANEL",bg="#787fff",font=('Times',30))
    la.place(x=528,y=65)
    butt_clr="#878dff"

    b1=Button(window1,text="DOCTOR",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=doctor)
    b1.place(x=110,y=200)

    b2=Button(window1,text="PATIENT",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=patient)
    b2.place(x=410,y=200)

    b3=Button(window1,text="APPOINTMENT",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=appointment)
    b3.place(x=110,y=350)

    b4=Button(window1,text="RECIEPT",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=reciept_call)
    b4.place(x=410,y=350)

    b5=Button(window1,text="ABOUT US",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=about_us1)
    b5.place(x=110,y=500)

    b6=Button(window1,text="LOGOUT",bg=butt_clr,bd=15,font=('Times',18,'bold'),width=12,command=logout)
    b6.place(x=410,y=500)  
    window.withdraw()
    window1.mainloop()
    
    
def logout():
    window1.destroy()
    winvar.destroy()
