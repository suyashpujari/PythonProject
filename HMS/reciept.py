from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+125+50")
        self.root.maxsize(width = 1280,height = 705)
        self.root.minsize(width = 1280,height = 705)
        self.root.title("Global Health Care Billing System")

        self.pat_name = StringVar()
        self.p_phone = StringVar()
        x = random.randint(99,99999)
        self.p_bill_no = StringVar()
        self.p_bill_no.set(str(x))

        self.Room_Rent = IntVar()
        self.Nursing_Charge = IntVar()
        self.Injections = IntVar()
        self.ICU_Rent = IntVar()
        self.ICU_Nursing = IntVar()
        self.Surgeon_Charge = IntVar()
        self.Specialist_Charge = IntVar()
        self.Consultants_Charge = IntVar()
        self.Anesthesia = IntVar()
        self.Blood = IntVar()
        self.Oxygen = IntVar()
        self.Surgical_Appliances = IntVar()
        self.OT_Charges = IntVar()
        self.Medicines = IntVar()
        self.Dialysis = IntVar()
        self.Radiotherapy = IntVar()
        self.Chemotherapy = IntVar()
        self.Laboratory = IntVar()
        self.X_Ray_Scan = IntVar()
        self.MRI_Scan = IntVar()
        self.bill = StringVar()
        self.taxes = StringVar()
        self.total_bill = StringVar()
        
        bg_color = "white"##00d3d6
        fg_color = "black"#black
        lbl_color = 'black'
        title = Label(self.root,text = "Global Health Care Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        F1 = LabelFrame(self.root,text = "Patient Details",font = ("time new roman",12,"bold"),fg = "red",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        cname_lbl = Label(F1,text="Patient Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.pat_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.p_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.p_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = bg_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        F2 = LabelFrame(self.root,text = 'Billing Heads',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 900,height = 380)

        R_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Room Rent")
        R_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        R_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Room_Rent)
        R_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        N_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Nursing Charge")
        N_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        N_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Nursing_Charge)
        N_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        IN_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Injections")
        IN_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        IN_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Injections)
        IN_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        I_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "ICU Rent")
        I_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        I_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.ICU_Rent)
        I_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        ICU_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "ICU Nursing")
        ICU_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        ICU_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.ICU_Nursing)
        ICU_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        S_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Surgeon Charge")
        S_lbl.grid(row = 0,column = 2,padx = 10,pady = 20)
        S_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Surgeon_Charge)
        S_en.grid(row = 0,column = 3,ipady = 5,ipadx = 5)

        C_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Consultants Charge")
        C_lbl.grid(row = 1,column = 2,padx = 10,pady = 20)
        C_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Consultants_Charge)
        C_en.grid(row = 1,column = 3,ipady = 5,ipadx = 5)

        Sp_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Specialist Charge")
        Sp_lbl.grid(row = 2,column = 2,padx = 10,pady = 20)
        Sp_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable=self.Specialist_Charge)
        Sp_en.grid(row = 2,column = 3,ipady = 5,ipadx = 5)

        A_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Anesthesia")
        A_lbl.grid(row = 3,column = 2,padx = 10,pady = 20)
        A_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Anesthesia)
        A_en.grid(row = 3,column = 3,ipady = 5,ipadx = 5)

        B_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Blood")
        B_lbl.grid(row = 4,column = 2,padx = 10,pady = 20)
        B_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Blood)
        B_en.grid(row = 4,column = 3,ipady = 5,ipadx = 5)

        O_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Oxygen")
        O_lbl.grid(row = 0,column = 4,padx = 10,pady = 20)
        O_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Oxygen)
        O_en.grid(row = 0,column = 5,ipady = 5,ipadx = 5)

        Su_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Surgical Appliances")
        Su_lbl.grid(row = 1,column = 4,padx = 10,pady = 20)
        Su_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Surgical_Appliances)
        Su_en.grid(row = 1,column = 5,ipady = 5,ipadx = 5)

        OT_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "O.T Charges")
        OT_lbl.grid(row = 2,column = 4,padx = 10,pady = 20)
        OT_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.OT_Charges)
        OT_en.grid(row = 2,column = 5,ipady = 5,ipadx = 5)

        Me_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Medicines")
        Me_lbl.grid(row = 3,column = 4,padx = 10,pady = 20)
        Me_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Medicines)
        Me_en.grid(row = 3,column = 5,ipady = 5,ipadx = 5)

        
        D_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Dialysis")
        D_lbl.grid(row = 4,column = 4,padx = 10,pady = 20)
        D_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Dialysis)
        D_en.grid(row = 4,column =5,ipady = 5,ipadx = 5)

        
        Ra_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Radiotherapy")
        Ra_lbl.grid(row = 0,column = 6,padx = 10,pady = 20)
        Ra_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Radiotherapy)
        Ra_en.grid(row = 0,column = 7,ipady = 5,ipadx = 5)

        
        Ch_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Chemotherapy")
        Ch_lbl.grid(row = 1,column = 6,padx = 10,pady = 20)
        Ch_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Chemotherapy)
        Ch_en.grid(row = 1,column = 7,ipady = 5,ipadx = 5)

        
        L_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Laboratory")
        L_lbl.grid(row = 2,column = 6,padx = 10,pady = 20)
        L_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.Laboratory)
        L_en.grid(row = 2,column = 7,ipady = 5,ipadx = 5)

        
        X_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "X-Ray Scan")
        X_lbl.grid(row = 3,column = 6,padx = 10,pady = 20)
        X_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.X_Ray_Scan)
        X_en.grid(row = 3,column = 7,ipady = 5,ipadx = 5)

        
        M_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "MRI Scan")
        M_lbl.grid(row = 4,column = 6,padx = 10,pady = 20)
        M_en = Entry(F2,bd = 8,width=8,relief = GROOVE,textvariable = self.MRI_Scan)
        M_en.grid(row = 4,column =7,ipady = 5,ipadx = 5)

         
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 901,y = 180,width = 380,height = 380)
        
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = BOTH)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)


        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bill")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.bill)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Taxes")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.taxes)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Bill")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_bill)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

    def total(self):
        self.total_bill_prices = (
            (self.Room_Rent.get() * 800)+
            (self.Nursing_Charge.get() * 300)+
            (self.Injections.get() * 250)+
            (self.ICU_Rent.get() * 2000)+
            (self.ICU_Nursing.get() * 500)+
            (self.Surgeon_Charge.get() * 5000)+
            (self.Consultants_Charge.get() * 1000)+
            (self.Specialist_Charge.get() * 2500)+
            (self.Anesthesia.get() * 500)+
            (self.Blood.get() * 750)+
            (self.Oxygen.get() * 1000)+
            (self.OT_Charges.get() * 3500)+
            (self.Surgical_Appliances.get() * 4000)+
            (self.Dialysis.get() * 2500)+
            (self.Radiotherapy.get() * 2500)+
            (self.Chemotherapy.get() * 2000)+
            (self.Laboratory.get() * 1000)+
            (self.X_Ray_Scan.get() * 3000)+
            (self.MRI_Scan.get() * 2000)
        )
        self.bill.set("Rs "+str(self.total_bill_prices))
        self.taxes.set("Rs "+str(round(self.total_bill_prices*0.05)))
        self.total_bill.set("Rs "+str(self.total_bill_prices+round(self.total_bill_prices*0.05)))

    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Global Health Care ")
        self.txt.insert(END,f"\nBill No: {str(self.p_bill_no.get())}")
        self.txt.insert(END,f"\nPatient Name: {str(self.pat_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.p_phone.get())}")
        self.txt.insert(END,"\n==========================================")
        self.txt.insert(END,"\nService              Qty           Price")
        self.txt.insert(END,"\n==========================================")

    def clear(self):
        self.txt.delete('1.0',END)

    def bill_area(self):
        self.welcome_soft()
        if self.Room_Rent.get() != 0:
            self.txt.insert(END,f"\nRoom Rent           {self.Room_Rent.get()}Days           {self.Room_Rent.get() * 800}")
        if self.Nursing_Charge.get() != 0:
            self.txt.insert(END,f"\nNursing Charge      {self.Nursing_Charge.get()}Days           {self.Nursing_Charge.get() * 300}")
        if self.Injections.get() != 0:
            self.txt.insert(END,f"\nInjections          {self.Injections.get()}Unit           {self.Injections.get() * 250}")
        if self.ICU_Rent.get() != 0:
            self.txt.insert(END,f"\nICU_Rent            {self.ICU_Rent.get()}Days           {self.ICU_Rent.get() * 2000}")
        if self.ICU_Nursing.get() != 0 :
            self.txt.insert(END,f"\nICU Nursing         {self.ICU_Nursing.get()}Days           {self.ICU_Nursing.get() * 500}")
        if self.Surgeon_Charge.get() != 0:
            self.txt.insert(END,f"\nSurgeon Charge      {self.Surgeon_Charge.get()}               {self.Surgeon_Charge.get() * 5000}")
        if self.Consultants_Charge.get() != 0:
            self.txt.insert(END,f"\nConsultants Charge  {self.Consultants_Charge.get()}               {self.Consultants_Charge.get() * 1000}")
        if self.Specialist_Charge.get() != 0:
            self.txt.insert(END,f"\nSpecialist Charge   {self.Specialist_Charge.get()}               {self.Specialist_Charge.get() * 2500}")
        if self.Anesthesia.get() != 0:
            self.txt.insert(END,f"\nAnesthesia          {self.Anesthesia.get()}Unit           {self.Anesthesia.get() * 500}")
        if self.Blood.get() != 0:
            self.txt.insert(END,f"\nBlood               {self.Blood.get()}Unit           {self.Blood.get() * 750}")
        if self.Oxygen.get() != 0:
            self.txt.insert(END,f"\nOxygen              {self.Oxygen.get()}Days           {self.Oxygen.get() * 1000}")
        if self.OT_Charges.get() != 0:
            self.txt.insert(END,f"\nO.T Charges         {self.OT_Charges.get()}               {self.OT_Charges.get() * 3500}")
        if self.Surgical_Appliances.get() != 0:
            self.txt.insert(END,f"\nSurgical Appliances {self.Surgical_Appliances.get()}               {self.Surgical_Appliances.get() * 4000}")
        if self.Dialysis.get() != 0:
            self.txt.insert(END,f"\nDialysis            {self.Dialysis.get()}               {self.Dialysis.get() * 2500}")
        if self.Radiotherapy.get() != 0:
            self.txt.insert(END,f"\nRadiotherapy        {self.Radiotherapy.get()}               {self.Radiotherapy.get() * 2500}")
        if self.Chemotherapy.get() != 0:
            self.txt.insert(END,f"\nChemotherapy        {self.Chemotherapy.get()}               {self.Chemotherapy.get() * 2000}")
        if self.Laboratory.get() != 0:
            self.txt.insert(END,f"\nLaboratory          {self.Laboratory.get()}               {self.Laboratory.get() * 1000}")
        if self.X_Ray_Scan.get() != 0:
            self.txt.insert(END,f"\nX-Ray Scan          {self.X_Ray_Scan.get()}               {self.X_Ray_Scan.get() * 3000}")
        if self.MRI_Scan.get() != 0:
            self.txt.insert(END,f"\nMRI Scan            {self.MRI_Scan.get()}               {self.MRI_Scan.get() * 2000}")
        self.txt.insert(END,f"\nTaxes                               {round(self.total_bill_prices*0.05)}")
        self.txt.insert(END,"\n==========================================")
        self.txt.insert(END,f"\n                         Total:{self.total_bill.get()}")
        self.txt.insert(END,"\n\nTake Care & Stay SAFE Stay HEALTHY :)")


    def exit(self):
        self.root.destroy()



        

def reciept_call():
    root = Toplevel()
    object = Bill_App(root)
    root.mainloop()


