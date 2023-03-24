import tkinter
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
#The method sets the title of the GUI window to "Hospital Management System" using the .title() method of the Tkinter module.
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.NHSNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="black",bg="pink",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
#Creating a Dataframe-->
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Arial",14,"bold"),text="Patient Information:")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("Arial", 14, "bold"), text="Prescription:")
        DataFrameRight.place(x=990, y=5, width=460, height=350)
#Creating Button Frame-->
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=70)
#Creating Details Frame-->
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=600, width=1530, height=190)
#DataFrameLeft-->
        LblNameTablet=Label(DataFrameLeft,text="Names of Tablets-",font=("times new roman", 12, "bold"),padx=2,pady=6)
        LblNameTablet.grid(row=0,column=0,sticky=W)

        ComNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameOfTablets ,font=("times new roman", 12),width=36)
        ComNameTablet["values"]=("Hydrocodone","Metformin","Losartan","Antibiotics","Albuterol","Antihistamines","Gabapentin","Omeprazole","Levothyroxine","Atorvastatin")
        ComNameTablet.grid(row=0,column=1)

        LblRef = Label(DataFrameLeft,font=("times new roman", 12, "bold"),text="Reference Number-",padx=2)
        LblRef.grid(row=1, column=0,sticky=W)
        TextRef = Entry(DataFrameLeft,textvariable=self.Ref, font=("times new roman", 13),width=35)
        TextRef.grid(row=1, column=1)

        LblDose = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Dose-", padx=2,pady=4)
        LblDose.grid(row=2, column=0, sticky=W)
        TextDose = Entry(DataFrameLeft,textvariable=self.Dose, font=("times new roman", 13), width=35)
        TextDose.grid(row=2, column=1)

        LblNoOfTablets = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Number of Tablets-", padx=2, pady=6)
        LblNoOfTablets.grid(row=3, column=0, sticky=W)
        TextNoOfTablets = Entry(DataFrameLeft,textvariable=self.NumberOfTablets, font=("times new roman", 13), width=35)
        TextNoOfTablets.grid(row=3, column=1)

        LblLot= Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Lot Number-", padx=2, pady=6)
        LblLot.grid(row=4, column=0, sticky=W)
        TextLot = Entry(DataFrameLeft,textvariable=self.Lot, font=("times new roman", 13), width=35)
        TextLot.grid(row=4, column=1)

        LblIssueDate = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Issue Date-", padx=2, pady=6)
        LblIssueDate.grid(row=5, column=0, sticky=W)
        TextIssueDate = Entry(DataFrameLeft,textvariable=self.IssueDate, font=("times new roman", 13), width=35)
        TextIssueDate.grid(row=5, column=1)

        LblExpDate = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Exp Date-", padx=2, pady=6)
        LblExpDate.grid(row=6, column=0, sticky=W)
        TextExpDate = Entry(DataFrameLeft,textvariable=self.ExpDate, font=("times new roman", 13), width=35)
        TextExpDate.grid(row=6, column=1)

        LblDailyDose = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Daily Dose-", padx=2, pady=6)
        LblDailyDose.grid(row=7, column=0, sticky=W)
        TextDailyDose = Entry(DataFrameLeft,textvariable=self.DailyDose, font=("times new roman", 13), width=35)
        TextDailyDose.grid(row=7, column=1)

        LblSideEffect = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Side Effect-", padx=2, pady=6)
        LblSideEffect.grid(row=8, column=0, sticky=W)
        TextSideEffect = Entry(DataFrameLeft,textvariable=self.SideEffect, font=("times new roman", 13), width=35)
        TextSideEffect.grid(row=8, column=1)

        LblFurthuerInfo = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Further Information-", padx=2, pady=6)
        LblFurthuerInfo.grid(row=0, column=2, sticky=W)
        TextFurtherInfo = Entry(DataFrameLeft,textvariable=self.FurtherInformation, font=("times new roman", 13), width=35)
        TextFurtherInfo.grid(row=0, column=3)

        LblBloodPressure = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Blood Pressure-", padx=2, pady=6)
        LblBloodPressure.grid(row=1, column=2, sticky=W)
        TextBloodPressure = Entry(DataFrameLeft,textvariable=self.DrivingUsingMachine, font=("times new roman", 13), width=35)
        TextBloodPressure.grid(row=1, column=3)

        LblStorage = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Storage Advice-",padx=2, pady=6)
        LblStorage.grid(row=2, column=2, sticky=W)
        TextStorage = Entry(DataFrameLeft,textvariable=self.StorageAdvice, font=("times new roman", 13), width=35)
        TextStorage.grid(row=2, column=3)

        LblMedicine = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Medication-",padx=2, pady=6)
        LblMedicine.grid(row=3, column=2, sticky=W)
        TextMedicine = Entry(DataFrameLeft,textvariable=self.HowToUseMedication, font=("times new roman", 13), width=35)
        TextMedicine.grid(row=3, column=3)

        LblPatientId = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Patient ID Number-",padx=2, pady=6)
        LblPatientId.grid(row=4, column=2, sticky=W)
        TextPatientId = Entry(DataFrameLeft,textvariable=self.PatientId, font=("times new roman", 13), width=35)
        TextPatientId.grid(row=4, column=3)

        LblNhsNumber = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="NHS Number-", padx=2, pady=6)
        LblNhsNumber.grid(row=5, column=2, sticky=W)
        TextNshNumber = Entry(DataFrameLeft,textvariable=self.NHSNumber, font=("times new roman", 13), width=35)
        TextNshNumber.grid(row=5, column=3)

        LblPatientName = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Patient Name-", padx=2,pady=6)
        LblPatientName.grid(row=6, column=2, sticky=W)
        TextPatientName = Entry(DataFrameLeft,textvariable=self.PatientName, font=("times new roman", 13), width=35)
        TextPatientName.grid(row=6, column=3)

        LblDateOfBirth = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Date Of Birth-", padx=2,pady=6)
        LblDateOfBirth.grid(row=7, column=2, sticky=W)
        TextDateOfBirth = Entry(DataFrameLeft,textvariable=self.DateOfBirth, font=("times new roman", 13), width=35)
        TextDateOfBirth.grid(row=7, column=3)

        LblPatientAddress = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Patient Address-", padx=2,pady=6)
        LblPatientAddress.grid(row=8, column=2, sticky=W)
        TextPatientAddress = Entry(DataFrameLeft,textvariable=self.PatientAddress, font=("times new roman", 13), width=35)
        TextPatientAddress.grid(row=8, column=3)
#DataFrameRight-->

        self.TxtPrescription=Text(DataFrameRight,font=("times new roman",12),width=45,height=16,padx=2,pady=6)
        self.TxtPrescription.grid(row=0,column=0)

#Buttons-->

        BtnPrescription = Button(ButtonFrame,text="Prescription", bg="black",fg="white",font=("arial",12, "bold"), width=23,padx=2, pady=6)
        BtnPrescription.grid(row=0, column=0)
        BtnPrescriptionData = Button(ButtonFrame, command=self.iPrescriptionData, text="Enter", bg="black",fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
        BtnPrescriptionData.grid(row=0, column=1)

        BtnUpdate = Button(ButtonFrame, text="Update", bg="black", fg="white",font=("arial", 12, "bold"), width=23,padx=2, pady=6)
        BtnUpdate.grid(row=0, column=2)

        BtnDelete = Button(ButtonFrame, text="Delete", bg="black", fg="white",font=("arial", 12, "bold"), width=23,padx=2, pady=6)
        BtnDelete.grid(row=0, column=3)

        BtnClear = Button(ButtonFrame, text="Clear", bg="Black", fg="white",font=("arial", 12, "bold"), width=23,padx=2, pady=6)
        BtnClear.grid(row=0, column=4)

        BtnExit = Button(ButtonFrame, text="Exit", bg="red", fg="white",font=("arial", 12, "bold"), width=23,padx=2, pady=6)
        BtnExit.grid(row=0, column=5)

#Table & Scroll Bar-->

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.Hospital_Table=ttk.Treeview(DetailsFrame,column=("nameOftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.Hospital_Table.xview)
        scroll_y = ttk.Scrollbar(command=self.Hospital_Table.yview)

        self.Hospital_Table.heading("nameOftable",text="Name of Table")
        self.Hospital_Table.heading("ref", text="Reference Number")
        self.Hospital_Table.heading("dose", text="Dose")
        self.Hospital_Table.heading("nooftablets", text="Name of Tablets")
        self.Hospital_Table.heading("lot", text="Lot")
        self.Hospital_Table.heading("issuedate", text="Issue Date")
        self.Hospital_Table.heading("expdate", text="Exp Date")
        self.Hospital_Table.heading("dailydose", text="Daily Dose")
        self.Hospital_Table.heading("storage",text="Storage")
        self.Hospital_Table.heading("nhsnumber", text="NHS Number")
        self.Hospital_Table.heading("pname", text="Patient Name")
        self.Hospital_Table.heading("dob", text="Date of Birth")
        self.Hospital_Table.heading("address", text="Address")

        self.Hospital_Table["show"]="headings"
        # self.Hospital_Table.pack(fill=BOTH,expand=1)

        self.Hospital_Table.column("nameOftable",width=100)
        self.Hospital_Table.column("ref", width=100)
        self.Hospital_Table.column("dose", width=100)
        self.Hospital_Table.column("nooftablets", width=100)
        self.Hospital_Table.column("lot", width=100)
        self.Hospital_Table.column("issuedate", width=100)
        self.Hospital_Table.column("expdate", width=100)
        self.Hospital_Table.column("dailydose", width=100)
        self.Hospital_Table.column("storage", width=100)
        self.Hospital_Table.column("nhsnumber", width=100)
        self.Hospital_Table.column("pname", width=100)
        self.Hospital_Table.column("dob", width=100)
        self.Hospital_Table.column("address",width=100)

        self.Hospital_Table.pack(fill=BOTH,expand=1)
        self.Hospital_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


#Function Declaration-->

    def iPrescriptionData(self):
        if self.NumberOfTablets.get() == "" or self.Ref.get() == "":
                messagebox.showerror("Error", "All fields are required!!")
        else:
            try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Shihab4483",
                                                   database="hospital_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (self.NameOfTablets.get(),
                                       self.Ref.get(),
                                       self.Dose.get(),
                                       self.NumberOfTablets.get(),
                                       self.Lot.get(),
                                       self.IssueDate.get(),
                                       self.ExpDate.get(),
                                       self.DailyDose.get(),
                                       self.StorageAdvice.get(),
                                       self.NHSNumber.get(),
                                       self.PatientName.get(),
                                       self.DateOfBirth.get(),
                                       self.PatientAddress.get())
                                      )
                    conn.commit()
                    self.fatch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                    print(str(e))
                    messagebox.showerror("Error", "An error occurred while inserting data.")


    def fatch_data(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="Shihab4483",database="hospital_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Hospital_Table.delete(*self.Hospital_Table.get_children())
            for i in rows:
                self.Hospital_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Hospital_Table.focus()
        content=self.Hospital_Table.item(cursor_row)
        row=content["values"]
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NHSNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])










root=Tk()
ob=Hospital(root)
root.mainloop()