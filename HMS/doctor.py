
from tkinter import *
from tkinter import ttk
import MySQLdb
from tkinter import messagebox


def doctor():
    
    global window3
    window3=Tk()
    window3.geometry('1800x1200') 
    window3.title("Hospital Management System")
    frame2=Frame(window3,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window3,text="MANAGE DOCTOR",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)

    lg=Label(window3,text="ID",font=('calibre',20,'bold'))
    lg.place(x=280,y=150)
    
    lc=Label(window3,text="NAME",font=('calibre',20,'bold'))
    lc.place(x=280,y=200)
    
    ld=Label(window3,text="SPECIALIZATION",font=('calibre',20,'bold'))
    ld.place(x=280,y=250)

    le=Label(window3,text="CONTACT",font=('calibre',20,'bold'))
    le.place(x=280,y=300)

    lf=Label(window3,text="ADDRESS",font=('calibre',20,'bold'))
    lf.place(x=280,y=350)

    lh=Label(window3,text="Enter Name To Search",font=('calibre',20,'bold'))
    lh.place(x=900,y=150)

    global Name, specialization,contact,address
    Name=StringVar()
    specialization=StringVar()
    contact=StringVar()
    address=StringVar()
    id=int()
    global ea,eb,ec,ed,ee,ef
    ea=Entry(window3,textvar="Name",width=20,font=('calibre',18,'bold'))
    ea.place(x=550,y=200)

    eb=Entry(window3,textvar="specialization",width=20,font=('calibre',18,'bold'))
    eb.place(x=550,y=250)

    ec=Entry(window3,textvar="contact",width=20,font=('calibre',18,'bold'))
    ec.place(x=550,y=300)

    ed=Entry(window3,textvar="address",width=20,font=('calibre',18,'bold'))
    ed.place(x=550,y=350)

    ee=Entry(window3,textvar="Search",width=20,font=('calibre',18,'bold'))
    ee.place(x=900,y=200)

    ef=Entry(window3,textvar="id",width=20,font=('calibre',18,'bold'))
    ef.place(x=550,y=150)


    
    ba=Button(window3,text="BACK",bg="orange",font=('calibre',18,'bold'),width=15,command=back)
    ba.place(x=0,y=1)

    bb=Button(window3,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=doctor1)
    bb.place(x=300,y=500)

    bc=Button(window3,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=delete)
    bc.place(x=530,y=500)

    bd=Button(window3,text="UPDATE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=update)
    bd.place(x=760,y=500)

    be=Button(window3,text="VIEW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=show)
    be.place(x=990,y=500)

    bi=Button(window3,text="SEARCH",bg="orange",font=('calibre',15,'bold'),width=15,bd=5,command=search)
    bi.place(x=1200,y=200)
    window3.mainloop()
    
    


        

def back():
    window3.destroy()
    


def doctor1():
    a=ea.get()
    b=eb.get()
    c=ec.get()
    d=ed.get()
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="INSERT INTO doctor(name,specialization,contact,address)VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ea.delete(first=0,last=20)
    eb.delete(first=0,last=20)
    ec.delete(first=0,last=20)
    ed.delete(first=0,last=20)


def show():
  
    window6=Tk()
    window6.geometry('1800x1200')
    window6.title("Hospital Management System")
    tree=ttk.Treeview(window6,column=(1,2,3,4,5),show="headings",height=30)
    tree.column("1",width=200)
    tree.column("2",width=200)
    tree.column("3",width=200)
    tree.column("4",width=200)
    tree.column("5",width=200)

    tree.heading(1,text="ID")
    tree.heading(2,text="Name")
    tree.heading(3,text="Specialization")
    tree.heading(4,text="Contact")
    tree.heading(5,text="Address")
    
    tree.place(x=250,y=100)
    frame2=Frame(window6,width=1600,height=54,bg="violet")
    frame2.place(x=0,y=0)
    lb=Label(window6,text="List Of Doctors",bg="violet",font=('calibre',30,'bold'))
    lb.place(x=615,y=0)


    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    cs.execute("SELECT * FROM doctor")
    rows=cs.fetchall()
    for x in rows:
        tree.insert('','end',values=x)
   
        
        

def delete():
    messagebox.askquestion("Confirmation","Are you sure want to delete?")  

    b=ea.get()
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="DELETE FROM doctor WHERE name=%s"
    val=(b,)
    cs.execute(sql,val)     
    conn.commit()
    cs.close()
    conn.close()
    ea.delete(first=0,last=20)
    eb.delete(first=0,last=20)
    ec.delete(first=0,last=20)
    ed.delete(first=0,last=20) 
    
 
def update():
    a=ea.get()
    b=eb.get()
    c=ec.get()
    d=ed.get()
    e=ef.get()
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="update doctor set name=%s,specialization=%s,contact=%s,address=%s WHERE id=%s"
    val=(a,b,c,d,e)
    cs.execute(sql,val)
    conn.commit()
    cs.close()
    conn.close()
    ea.delete(first=0,last=20)
    eb.delete(first=0,last=20)
    ec.delete(first=0,last=20)
    ed.delete(first=0,last=20)

def search():
    s=ee.get()
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",database="hms")
    cs=conn.cursor()
    sql="SELECT * FROM doctor WHERE Name=%s "
    val=(s,)
    cs.execute(sql,val)
    rows=cs.fetchall()
    global x
    for x in rows:
        a=x[0]
        b=x[1]
        c=x[2]
        d=x[3]
        e=x[4]
        if s==b:
            ef.insert(0,a)
            ea.insert(0,b)
            eb.insert(0,c)
            ec.insert(0,d)
            ed.insert(0,e)
    if x[0]==None :
        messagebox.showinfo("Warning !","No Data Found")
    ee.delete(first=0,last=20)






