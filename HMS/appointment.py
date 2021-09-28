from tkinter import *
from tkinter import ttk
from tkcalendar import * 
from tkinter import messagebox
from datetime import *
import MySQLdb

def appointment():
    global window5
    window5=Tk()
    window5.geometry('1800x1200') 
    window5.title("Hospital Management System")
    frame2=Frame(window5,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window5,text="MANAGE APPOINTMENT",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window5,text="DOCTOR NAME",font=('calibre',20,'bold'))
    lg.place(x=280,y=100)
    
    lh=Label(window5,text="PATIENT NAME",font=('calibre',20,'bold'))
    lh.place(x=280,y=150)

    li=Label(window5,text="DATE",font=('calibre',20,'bold'))
    li.place(x=280,y=200)

    lj=Label(window5,text="TIME:",font=('calibre',20,'bold'))
    lj.place(x=280,y=450)

    lk=Label(window5,text="Hours-",font=('calibre',15,'bold'))
    lk.place(x=400,y=450)

    ll=Label(window5,text="Minutes-",font=('calibre',15,'bold'))
    ll.place(x=400,y=500)

    lm=Label(window5,text="Meridiem-",font=('calibre',15,'bold'))
    lm.place(x=400,y=550)

    global e1,e2,e3,ei,ek,today,day,month,year
    global search,doctor,patient,cal,doc,pat
    global doc_name,pat_name
    doc_name=[]
    pat_name=[]
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    cs.execute("SELECT name FROM doctor")
    for rows in cs.fetchall():
        doc_name.append(rows)
    cm=conn.cursor()
    cm.execute("SELECT name FROM patient")
    for rows in cm.fetchall():
        pat_name.append(rows)
    doctor=StringVar()
    patient=StringVar()
    today=datetime.today()
    day=today.day
    month=today.month
    year=today.year
    doc=ttk.Combobox(window5, width = 18, textvariable = doctor)
    doc['values'] = doc_name
    doc.place(x=550,y=100) 
    doc['state'] = 'readonly'

    pat=ttk.Combobox(window5, width = 18, textvariable = patient)
    pat['values'] = pat_name
    pat.place(x=550,y=150) 
    pat['state'] = 'readonly'

    cal=Calendar(window5,year=year, month=month, day=day)
    cal.place(x=550,y=200)

    global hours,minutes,time_,click
    hrs=['']
    mins=['']
    for i in range(1,13):
        hrs.append(i)
    for i in range(0,59):
        mins.append(i)
    click1=StringVar()
    click2=StringVar()
    click=StringVar()
    hours=ttk.Combobox(window5, width = 18, textvariable = click)
    hours['values'] = hrs
    hours.place(x=550,y=450) 
    hours['state'] = 'readonly'
    
    minutes=ttk.Combobox(window5, width = 18, textvariable = click1) 
    minutes['values'] = mins
    minutes.place(x=550,y=500)
    minutes['state'] = 'readonly'
    
    time_=ttk.Combobox(window5, width = 18, textvariable = click2)
    time_['values'] = ("AM","PM")
    time_.place(x=550,y=550)
    time_['state'] = 'readonly'
    
    
    
    bf=Button(window5,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    bf.place(x=0,y=1)

    bg=Button(window5,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=appointment1)
    bg.place(x=300,y=700)

    bh=Button(window5,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bh.place(x=530,y=700)

    bj=Button(window5,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    bj.place(x=760,y=700)


def back():
    window5.destroy()


def appointment1():
      
    a=doc.get()
    b=pat.get()
    c=cal.get_date()
    d=hours.get()+':'+minutes.get()+' '+time_.get()
    print(a,b,c,d)
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="INSERT INTO appointment(doc_name,pat_name,date,time)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
     

def show():
    window6=Tk()
    window6.geometry('1800x1200')
    window6.title("Hospital Management System")
    tree=ttk.Treeview(window6,column=(1,2,3,4,5),show="headings",height=30)
    tree.heading(1,text="ID")
    tree.heading(2,text="Doctor")
    tree.heading(3,text="Patient")
    tree.heading(4,text="Date")
    tree.heading(5,text="Time")
    tree.place(x=250,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Appointments",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=550,y=0)


    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    cs.execute("SELECT * FROM appointment")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)
        

def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")
    a=pat.get()
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="DELETE FROM appointment WHERE pat_name=%s"
    val=(a,)
    cs.execute(sql,val)     
    conn.commit()
    cs.close()
    conn.close()         







