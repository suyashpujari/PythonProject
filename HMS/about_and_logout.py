from tkinter import *
from tkinter import ttk
from tkcalendar import *
def about_us():
    global window9
    window9=Tk()
    window9.geometry('1800x1200') 
    window9.title("Hospital Management System")
    frame2=Frame(window9,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window9,text="About Us",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window9,text="Hospital Name: Global Health Care",font=('Times',25,'bold'))
    lg.place(x=280,y=100)
    
    lh=Label(window9,text="Address: Global Health Care Bulding no.32 main road,Pune,Pin Code:405335",font=('Times',25,'bold'))
    lh.place(x=280,y=200)

    li=Label(window9,text="Contact: 0217-858510",font=('Times',25,'bold'))
    li.place(x=280,y=300)

    lj=Label(window9,text="Email: globalhealthcare@domain.com",font=('Times',25,'bold'))
    lj.place(x=280,y=400)