from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

# pip install pymysql (cmd command)

#create database fashion
#use fashion
#create table fashion(PId int, CName varchar(50), gender varchar(10),
#address varchar(100), MobNo bigint , ClType varchar(50), brand varchar(50), cost int );


class FashionDB:

    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "Fashion Clothing")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width =False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief = RIDGE, bg ='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg="cadet blue", relief= RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2,pady=4, relief= RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg="cadet blue", relief= RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2,pady=2, relief= RIDGE)
        RightFrame1a.pack(side=TOP)
        
        #=============================================================================================

        ProductID =StringVar()
        CustomerName =StringVar()
        Gender =StringVar()
        Address =StringVar()
        MobileNo =StringVar()
        ClothType =StringVar()
        Brand =StringVar()
        Cost =StringVar()

        #============================================================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Fashion Clothing", "Confirm if you want to exit!!")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entProductID.delete(0,END)
            self.entCustomerName.delete(0,END)
            Gender.set("")
            self.entAddress.delete(0,END)
            self.entMobileNo.delete(0,END)
            ClothType.set("")
            Brand.set("")
            self.entCost.delete(0,END)

        def addData():
            if ProductID.get() =="" or CustomerName.get() =="" or Gender.get()=="":
                tkinter.messagebox.showerror("Enter Correct Details!!")
            else:
                sqlCon =pymysql.connect(host="localhost",user="root",password="root",database="fashion")
                cur =sqlCon.cursor()
                cur.execute("insert into fashion values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    ProductID.get(),
                    CustomerName.get(),
                    Gender.get(),
                    Address.get(),
                    MobileNo.get(),
                    ClothType.get(),
                    Brand.get(),
                    Cost.get(),
                    ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully!!")

        def DisplayData():
            sqlCon = pymysql.connect(host="localhost",user="root",password="root",database="fashion")
            cur = sqlCon.cursor()
            cur.execute("select * from fashion")
            result = cur.fetchall()
            if len(result) !=0:
                self.Customer_records.delete(*self.Customer_records.get_children())
                for row in result:
                    self.Customer_records.insert('', END, values = row)
                sqlCon.commit()
                sqlCon.close()

        def fashionInfo(ev):
            viewInfo = self.Customer_records.focus()
            learnerData = self.Customer_records.item(viewInfo)
            row = learnerData['values']
            ProductID.set(row[0])
            CustomerName.set(row[1])
            Gender.set(row[2])
            Address.set(row[3])
            MobileNo.set(row[4])
            ClothType.set(row[5])
            Brand.set(row[6])
            Cost.set(row[7])

        def update():
            sqlCon =pymysql.connect(host="localhost",user="root",password="root",database="fashion")
            cur =sqlCon.cursor()
            cur.execute("update fashion set CName=%s,gender=%s,address=%s,MobNo=%s,ClType=%s,brand=%s,cost=%s where PId=%s",
                    (
                    CustomerName.get(),
                    Gender.get(),
                    Address.get(),
                    MobileNo.get(),
                    ClothType.get(),
                    Brand.get(),
                    Cost.get(),
                    ProductID.get()
                    ))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully!!")

        def deleteDB():
            sqlCon =pymysql.connect(host="localhost",user="root",password="root",database="fashion")
            cur =sqlCon.cursor()
            cur.execute("delete from fashion where PID=%s",ProductID.get())
        
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Deleted Successfully!!")
            Reset()

        def searchDB():
            try:
                sqlCon =pymysql.connect(host="localhost",user="root",password="root",database="fashion")
                cur =sqlCon.cursor()
                cur.execute("select * from fashion where PId=%s",ProductID.get())
                
                row = cur.fetchone()
                
                ProductID.set(row[0])
                CustomerName.set(row[1])
                Gender.set(row[2])
                Address.set(row[3])
                MobileNo.set(row[4])
                ClothType.set(row[5])
                Brand.set(row[6])
                Cost.set(row[7])
        
                sqlCon.commit() 
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No such Record Found!!")
                Reset()
            sqlCon.close()

        #=============================================================================================

        self.lbltitle=Label(TitleFrame, font=('Bauhaus 93',40,'bold'),text="Fashion Clothing",bd=7)
        self.lbltitle.grid(row=0,column=0, padx=132)

        #=============================================================================================

        self.lblProductID=Label(LeftFrame1, font=('arial',12,'bold'),text="Product ID",bd=7)
        self.lblProductID.grid(row=0,column=0, sticky=W, padx=5)
        self.entProductID=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',
                                textvariable=ProductID)
        self.entProductID.grid(row=0,column=1, sticky=W, padx=5)

        self.lblCustomerName=Label(LeftFrame1, font=('arial',12,'bold'),text="Customer Name",bd=7)
        self.lblCustomerName.grid(row=1,column=0, sticky=W, padx=5)
        self.entCustomerName=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',
                                   textvariable=CustomerName)
        self.entCustomerName.grid(row=1,column=1, sticky=W, padx=5)

        self.lblGender=Label(LeftFrame1, font=('arial',12,'bold'),text="Gender",bd=5)
        self.lblGender.grid(row=2,column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial',12,'bold'),width=42, state='readonly',
                                       textvariable=Gender)
        self.cboGender['values']=(' ','Female','Male','Trans-Gender')
        self.cboGender.current(0)
        self.cboGender.grid(row=2,column=1)

        self.lblAddress=Label(LeftFrame1, font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=3,column=0, sticky=W, padx=5)
        self.entAddress=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',
                             textvariable=Address)
        self.entAddress.grid(row=3,column=1, sticky=W, padx=5)

        self.lblMobileNo=Label(LeftFrame1, font=('arial',12,'bold'),text="Mobile Number",bd=7)
        self.lblMobileNo.grid(row=4,column=0, sticky=W, padx=5)
        self.entMobileNo=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',
                               textvariable=MobileNo)
        self.entMobileNo.grid(row=4,column=1, sticky=W, padx=5)

        self.lblClothType=Label(LeftFrame1, font=('arial',12,'bold'),text="Cloth Type",bd=7)
        self.lblClothType.grid(row=5,column=0, sticky=W, padx=5)
        self.cboClothType = ttk.Combobox(LeftFrame1, font=('arial',12,'bold'),width=42, state='readonly',
                                          textvariable=ClothType)
        self.cboClothType['values']=(' ','PANT','SHORTS','LHENGA','TOP','T-SHIRT','MIDI','SAREE','DRESS')
        self.cboClothType.current(0)
        self.cboClothType.grid(row=5,column=1)

        self.lblBrand=Label(LeftFrame1, font=('arial',12,'bold'),text="Brand",bd=7)
        self.lblBrand.grid(row=6,column=0, sticky=W, padx=5)
        self.cboBrand = ttk.Combobox(LeftFrame1, font=('arial',12,'bold'),width=42, state='readonly',
                                    textvariable = Brand)
        self.cboBrand['values']=(' ','H&M','Tommy Hilfiger','Anouk','Only','Buffalo','Mango','Silk','Banarasi','Levis')
        self.cboBrand.current(0)
        self.cboBrand.grid(row=6,column=1)

        self.lblCost=Label(LeftFrame1, font=('arial',12,'bold'),text="Cost",bd=7)
        self.lblCost.grid(row=7,column=0, sticky=W, padx=5)
        self.entCost=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5, width=44, justify='left',
                           textvariable=Cost)
        self.entCost.grid(row=7,column=1, sticky=W, padx=5)

        #==========================================Table TreeView==============================================================

        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)

        self.Customer_records = ttk.Treeview(LeftFrame, height=12, columns=("PId", "CName","gender","address","MobNo","ClType","brand",
                                                                            "cost"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side = RIGHT, fill= Y)

        self.Customer_records.heading("PId", text="ProductID")
        self.Customer_records.heading("CName", text="CustomerName")
        self.Customer_records.heading("gender", text="Gender")
        self.Customer_records.heading("address", text="Address")
        self.Customer_records.heading("MobNo", text="MobileNo")
        self.Customer_records.heading("ClType", text="ClothType")
        self.Customer_records.heading("brand", text="Brand")
        self.Customer_records.heading("cost", text="Cost")

        self.Customer_records['show']='headings'
        
        self.Customer_records.column("PId", width=70)
        self.Customer_records.column("CName", width=70)
        self.Customer_records.column("gender", width=70)
        self.Customer_records.column("address", width=70)
        self.Customer_records.column("MobNo", width=70)
        self.Customer_records.column("ClType", width=70)
        self.Customer_records.column("brand", width=70)
        self.Customer_records.column("cost", width=70)

        self.Customer_records.pack(fill=BOTH, expand=1)
        self.Customer_records.bind("<ButtonRelease-1>",fashionInfo)

        #==========================================Button======================================================

        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Add New",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=addData).grid(row=0,column=0,padx=1)

        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text="Display",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=DisplayData).grid(row=1,column=0,padx=1)
        
        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=update).grid(row=2,column=0,padx=1)
        
        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=deleteDB).grid(row=3,column=0,padx=1)

        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text="Search",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=searchDB).grid(row=4,column=0,padx=1)

        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=Reset).grid(row=5,column=0,padx=1)
        
        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,bg="cadet blue", pady=1, padx=24,
                              width = 8, height=2, command=iExit).grid(row=6,column=0,padx=1)
        
        #=======================================================================================================

    #return value:-

if __name__=='__main__':
    root = Tk()
    application = FashionDB(root)
    root.mainloop()
