from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import mysql.connector
from tkinter import messagebox

class Bus:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("KARUNYA BUS MANAGEMENT SYSTEM")

        # variables
        self.var_name=StringVar()
        self.var_reg=StringVar()
        self.var_mentor=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_add=StringVar()
        self.var_phone=StringVar()
        self.var_book=StringVar()
        self.var_busno=StringVar()
        self.var_dname=StringVar()
        self.var_dcontact=StringVar()
        self.var_splace=StringVar()
        self.var_stime=StringVar()
        self.var_eplace=StringVar()
        self.var_etime=StringVar()
        self.var_seat=StringVar()
        self.var_gen=StringVar()

        #img=ImageTk.PhotoImage(Image.open("IMAGES/Screenshot 2024-04-14 180912.jpg"))
        #label1=Label(image=img)
        #label1.pack()
        img = Image.open(r"IMAGES\4th.png")
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn1=Button(self.root,image=self.photoimg,bg="white")
        self.btn1.place(x=0,y=0,width=1500,height=150)

        #Background
        img2 = Image.open(r"IMAGES\2nd.png")
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg=Label(self.root,image=self.photoimg2,bd=1,relief=RIDGE,bg="white")
        bg.place(x=0,y=150,width=1530,height=790)

        #Title
        label_title = Label(bg,text="KARUNYA BUS MANAGEMENT SYSTEM",font=("arial black",30,"bold"),fg="White",bg="black")
        label_title.place(x=1,y=0,height=40,width=1400)

        #Manage Frame
        Manage_frame=Frame(bg,bd=1,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=45,height=800,width=1400)

        #Left Fram
        LeftFrame = LabelFrame(Manage_frame,bd=2,relief=RIDGE,padx=2,text="STUDENT AND BUS INFORMATION",font=("arial black",16,"bold"),fg="black",bg="white")
        LeftFrame.place(x=10,y=10,width=620,height=550)

        #Right Fram
        RightFrame = LabelFrame(Manage_frame,bd=2,relief=RIDGE,padx=2,text="INFORMATION DISPLAY",font=("arial black",16,"bold"),fg="black",bg="white")
        RightFrame.place(x=640,y=10,width=740,height=550)

        '''''
        IMAGE in data frame left
        img3 = Image.open(r"IMAGES\2nd.png")
        self.photoimg3=ImageTk.PhotoImage(img2)

        new_img=Label(LeftFrame,self.root,image=self.photoimg3,bd=2,relief=RIDGE)
        new_img.place(x=0,y=0,width=650,height=120)
        '''''

        #Cureent cource Label Frame Information
        Student_label_info = LabelFrame(LeftFrame,bd=2,relief=RIDGE,padx=2,text="STUDENT INFORMATION",font=("times new roman",12,"bold"),fg="black",bg="white")
        Student_label_info.place(x=10,y=10,width=595,height=200)

        #LABELS
        #name
        name = Label(Student_label_info,text="Student Name",font=("times new roman",12),fg="black",bg="white")
        name.grid(row=0,column=0,padx=2,sticky=W)

        tb1 = Entry(Student_label_info,textvariable=self.var_name)
        tb1.grid(row=0,column=1,padx=5,pady=10)


        #Reg no
        regno = Label(Student_label_info,text="Registor Number",font=("times new roman",12),fg="black",bg="white")
        regno.grid(row=0,column=2,padx=2,sticky=W)

        tb2 = Entry(Student_label_info,textvariable=self.var_reg)
        tb2.grid(row=0,column=3,padx=5,pady=10)

        #dept name
        dept = Label(Student_label_info,text="Department",font=("times new roman",12),fg="black",bg="white")
        dept.grid(row=1,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(Student_label_info,textvariable=self.var_dep,font=("times new roman",12),width=17,state="readonly")
        combo_dept["value"]=("Select Department","Computer Science and Engineering","Mechanical Engineering","Biotechnology","Biomedical Engineering","Electronics and Communication Engineering","Arts and Science","Others")
        combo_dept.current(0)
        combo_dept.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Year
        year = Label(Student_label_info,text="Year of Study",font=("times new roman",12),fg="black",bg="white")
        year.grid(row=1,column=2,padx=2,sticky=W)

        year_combo=ttk.Combobox(Student_label_info,textvariable=self.var_year,font=("times new roman",12),width=17,state="readonly")
        year_combo["value"]=("Select Year","I","II","III","IV","PG","PHD","Others")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #mentor name
        mentor = Label(Student_label_info,text="Mentor Name",font=("times new roman",12),fg="black",bg="white")
        mentor.grid(row=2,column=0,padx=2,sticky=W)
        tb3 = Entry(Student_label_info,textvariable=self.var_mentor)
        tb3.grid(row=2,column=1,padx=5,pady=10)

        #Phone number
        phone = Label(Student_label_info,text="Phone Number",font=("times new roman",12),fg="black",bg="white")
        phone.grid(row=2,column=2,padx=2,sticky=W)
        tb4 = Entry(Student_label_info,textvariable=self.var_phone)
        tb4.grid(row=2,column=3,padx=5,pady=10)

        #Address
        add = Label(Student_label_info,text="Address",font=("times new roman",12),fg="black",bg="white")
        add.grid(row=3,column=0,padx=2,sticky=W)
        tb5 = Entry(Student_label_info,textvariable=self.var_add)
        tb5.grid(row=3,column=1,padx=5,pady=10)


        #Bus information
        Bus_label_info = LabelFrame(LeftFrame,bd=2,relief=RIDGE,padx=2,text="BUS INFORMATION",font=("times new roman",12,"bold"),fg="black",bg="white")
        Bus_label_info.place(x=10,y=225,width=595,height=230)

        #Labels

        #bus number
        busno = Label(Bus_label_info,text="Bus Number",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=0,column=0,padx=2,sticky=W)

        tb6 = Entry(Bus_label_info,textvariable=self.var_busno)
        tb6.grid(row=0,column=1,padx=11,pady=11)

        #booking number
        bookno = Label(Bus_label_info,text="Booking Number",font=("times new roman",12),fg="black",bg="white")
        bookno.grid(row=0,column=2,padx=2,sticky=W)

        tb7 = Entry(Bus_label_info,textvariable=self.var_book)
        tb7.grid(row=0,column=3,padx=15,pady=11)

        #bus driver name
        busno = Label(Bus_label_info,text="Driver Name",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=1,column=0,padx=2,sticky=W)

        tb8 = Entry(Bus_label_info,textvariable=self.var_dname)
        tb8.grid(row=1,column=1,padx=11,pady=11)

        #bus driver contact
        busno = Label(Bus_label_info,text="Driver Contact",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=1,column=2,padx=2,sticky=W)

        tb9 = Entry(Bus_label_info,textvariable=self.var_dcontact)
        tb9.grid(row=1,column=3,padx=15,pady=11)

        #bus starting place
        busno = Label(Bus_label_info,text="Departure",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=2,column=0,padx=2,sticky=W)

        tb10 = Entry(Bus_label_info,textvariable=self.var_splace)
        tb10.grid(row=2,column=1,padx=11,pady=11)

        #bus starting time
        busno = Label(Bus_label_info,text="Departure Time",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=3,column=0,padx=2,sticky=W)

        tb11 = Entry(Bus_label_info,textvariable=self.var_stime)
        tb11.grid(row=3,column=1,padx=11,pady=11)

        #bus ending place
        busno = Label(Bus_label_info,text="Destination",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=2,column=2,padx=2,sticky=W)

        tb10 = Entry(Bus_label_info,textvariable=self.var_eplace)
        tb10.grid(row=2,column=3,padx=11,pady=11)

        
        #bus ending time
        busno = Label(Bus_label_info,text="Destination Time",font=("times new roman",12),fg="black",bg="white")
        busno.grid(row=3,column=2,padx=2,sticky=W)

        tb12 = Entry(Bus_label_info,textvariable=self.var_etime)
        tb12.grid(row=3,column=3,padx=11,pady=11)

        #bus seat number
        seatno = Label(Bus_label_info,text="Seat Number",font=("times new roman",12),fg="black",bg="white")
        seatno.grid(row=4,column=0,padx=2,sticky=W)

        tb13 = Entry(Bus_label_info,textvariable=self.var_seat)
        tb13.grid(row=4,column=1,padx=11,pady=11)

        #Gender
        gender = Label(Bus_label_info,text="Gender",font=("times new roman",12),fg="black",bg="white")
        gender.grid(row=4,column=2,padx=2,sticky=W)

        gender_combo=ttk.Combobox(Bus_label_info,textvariable=self.var_gen,font=("times new roman",12),width=17,state="readonly")
        gender_combo["value"]=("Select Gender","Male","Female","LetsBegin","Abinary","Anime","Bakla","Calabai","RCBian","Intelligent","Transperant","Invisible","Translate","Genius","Bakka","Others")
        gender_combo.current(0)
        gender_combo.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        # Button frame
        btn_frame = Frame(LeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=610,height=40)
        
        # Save
        add = Button(btn_frame, text="Save",command=self.add_data,font=("times new roman",12),width = 15,bg="red",fg="white")
        add.grid(row=0,column=0,padx=1)

        # Update
        update = Button(btn_frame, text="Update",command=self.update_data,font=("times new roman",12),width = 16,bg="red",fg="white")
        update.grid(row=0,column=1,padx=1)

        # Delete
        delete = Button(btn_frame, text="Delete",command=self.delete_data,font=("times new roman",12),width = 15,bg="red",fg="white")
        delete.grid(row=0,column=2,padx=1)

        # reset
        reset = Button(btn_frame, text="Reset",command=self.reset_data,font=("times new roman",12),width = 16,bg="red",fg="white")
        reset.grid(row=0,column=3,padx=1)

        #Right Fram
        

        #IMAGE in data frame right
        img4 = Image.open(r"IMAGES\6th.png")
        self.photoimg4=ImageTk.PhotoImage(img4)
  
        new_img=Label(RightFrame,image=self.photoimg4,bd=0,relief=RIDGE)
        new_img.place(x=250,y=0,width=250,height=200)

        SearchFrame = LabelFrame(RightFrame,bd=2,relief=RIDGE,padx=2,text="Search Information",font=("arial black",12,"bold"),fg="black",bg="white")
        SearchFrame.place(x=0,y=200,width=732,height=60)

        #Labels
        #Search
        searchusing = Label(SearchFrame,text="Search Using",font=("times new roman",12),fg="green",bg="white")
        searchusing.grid(row=0,column=0,padx=2,sticky=W)

        #Search Button
        self.var_combo_search=StringVar()
        search_combo=ttk.Combobox(SearchFrame,textvariable=self.var_combo_search,font=("times new roman",12),width=17,state="readonly")
        search_combo["value"]=("Select Option","Register_Number","Booking_Number","Phone_Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,sticky=W)

        search = Label(SearchFrame,text="Search",font=("times new roman",12),fg="green",bg="white")
        search.grid(row=0,column=2,padx=5,sticky=W)

        self.var_search=StringVar()
        tb14 = ttk.Entry(SearchFrame,textvariable=self.var_search)
        tb14.grid(row=0,column=3,padx=5)

        # Delete
        searchbtn = Button(SearchFrame,command=self.search_data,text="Search",font=("times new roman",12),width = 13,bg="red",fg="white")
        searchbtn.grid(row=0,column=4,padx=8)

        # reset
        show= Button(SearchFrame, command=self.fetch_data,text="Show All",font=("times new roman",12),width = 13,bg="red",fg="white")
        show.grid(row=0,column=5,padx=3)

        #---------------------------------------------DETAILS TABLE & SCROLE BAR---------------------------------------------------

        tableframe = Frame(RightFrame,bd=2,relief=RIDGE,bg="white")
        tableframe.place(x=0,y=270,height=240,width=732)

        scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
        self.bus_table=ttk.Treeview(tableframe,column=("Name","Register_Number","Department","Year","Mentor","Phone_Number","Address","Bus_Number","Booking_Number","Driver_Name","Driver_Contact","Departure","Departure_Time","Destination","Destination_Time","Seat_Number","Gender"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.bus_table.xview)
        scrolly.config(command=self.bus_table.yview)

        self.bus_table.heading("Name",text="Student Name")
        self.bus_table.heading("Register_Number",text="Register Number")
        self.bus_table.heading("Department",text="Department")
        self.bus_table.heading("Year",text="Year")
        self.bus_table.heading("Mentor",text="Mentor Name")
        self.bus_table.heading("Phone_Number",text="Phone Number")
        self.bus_table.heading("Address",text="Address")
        self.bus_table.heading("Bus_Number",text="Bus Number")
        self.bus_table.heading("Booking_Number",text="Booking Number")
        self.bus_table.heading("Driver_Name",text="Driver Name")
        self.bus_table.heading("Driver_Contact",text="Driver Contact")
        self.bus_table.heading("Departure",text="Departure")
        self.bus_table.heading("Departure_Time",text="Departure Time")
        self.bus_table.heading("Destination",text="Destination")
        self.bus_table.heading("Destination_Time",text="Destination Time")
        self.bus_table.heading("Seat_Number",text="Seat Number")
        self.bus_table.heading("Gender",text="Gender")

        self.bus_table["show"]="headings"

        self.bus_table.column("Name",width=120)
        self.bus_table.column("Register_Number",width=120)
        self.bus_table.column("Department",width=200)
        self.bus_table.column("Year",width=120)
        self.bus_table.column("Mentor",width=120)
        self.bus_table.column("Phone_Number",width=120)
        self.bus_table.column("Address",width=120)
        self.bus_table.column("Bus_Number",width=120)
        self.bus_table.column("Booking_Number",width=120)
        self.bus_table.column("Driver_Name",width=120)
        self.bus_table.column("Driver_Contact",width=120)
        self.bus_table.column("Departure",width=120)
        self.bus_table.column("Departure_Time",width=120)
        self.bus_table.column("Destination",width=120)
        self.bus_table.column("Destination_Time",width=120)
        self.bus_table.column("Seat_Number",width=120)
        self.bus_table.column("Gender",width=120)
                
        self.bus_table.pack(fill=BOTH,expand=1)
        self.bus_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if (self.var_name.get()=="" or self.var_reg.get()==""or self.var_dep.get()==""):
            messagebox.showerror("ERROR","All Fields are REQUIRED")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="#Mysql123!27",database="riyadb")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_name.get(),
                                                                                                    self.var_reg.get(),
                                                                                                    self.var_dep.get() ,                           
                                                                                                    self.var_year.get(),
                                                                                                    self.var_mentor.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_add.get(),
                                                                                                    self.var_busno.get(),
                                                                                                    self.var_book.get(),
                                                                                                    self.var_dname.get(),
                                                                                                    self.var_dcontact.get(),
                                                                                                    self.var_splace.get(),
                                                                                                    self.var_stime.get(),
                                                                                                    self.var_eplace.get(),
                                                                                                    self.var_etime.get(),
                                                                                                    self.var_seat.get(),
                                                                                                    self.var_gen.get(),
                                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#Mysql123!27",database="riyadb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.bus_table.delete(*self.bus_table.get_children())
            for i in data:
                self.bus_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.bus_table.focus()
        content=self.bus_table.item(cursor_row)
        data=content["values"]

        self.var_name.set(data[0])
        self.var_reg.set(data[1])
        self.var_dep.set(data[2])                        
        self.var_year.set(data[3])
        self.var_mentor.set(data[4])
        self.var_phone.set(data[5])
        self.var_add.set(data[6])
        self.var_busno.set(data[7])
        self.var_book.set(data[8])
        self.var_dname.set(data[9])
        self.var_dcontact.set(data[10])
        self.var_splace.set(data[11])
        self.var_stime.set(data[12])
        self.var_eplace.set(data[13])
        self.var_etime.set(data[14])
        self.var_seat.set(data[15])
        self.var_gen.set(data[16])

    #UPDATE BUTTON

    def update_data(self):
        if (self.var_name.get()=="" or self.var_reg.get()==""or self.var_dep.get()==""):
            messagebox.showerror("ERROR","All Fields are REQUIRED")
        else:
            try:
                updatenew=messagebox.askyesno("UPDATE","Are you sure you want to update the data?",parent=self.root)
                if updatenew>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#Mysql123!27",database="riyadb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update students set Name=%s,Department=%s,Year=%s,Mentor=%s,Phone_Number=%s,Address=%s,Bus_Number=%s,Booking_Number=%s,Driver_Name=%s,Driver_Contact=%s,Departure =%s,Departure_Time =%s,Destination=%s,Destination_Time=%s,Seat_Number=%s,Gender=%s where Register_Number=%s",(
                                                                                                                                                            self.var_name.get(),
                                                                                                                                                            self.var_dep.get(),                      
                                                                                                                                                            self.var_year.get(),
                                                                                                                                                            self.var_mentor.get(),
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_add.get(),
                                                                                                                                                            self.var_busno.get(),
                                                                                                                                                            self.var_book.get(),
                                                                                                                                                            self.var_dname.get(),
                                                                                                                                                            self.var_dcontact.get(),
                                                                                                                                                            self.var_splace.get(),
                                                                                                                                                            self.var_stime.get(),
                                                                                                                                                            self.var_eplace.get(),
                                                                                                                                                            self.var_etime.get(),
                                                                                                                                                            self.var_seat.get(),
                                                                                                                                                            self.var_gen.get(),
                                                                                                                                                            self.var_reg.get()
                                                                                                                                                            ))
                else:
                    if not updatenew:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","The Data has been successfully updated!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # Delete button
    def delete_data(self):
        if self.var_reg.get()=="":
            messagebox.showerror("ERROR","All Fields are REQUIRED")
        else:
            try:
                Deletenew=messagebox.askyesno("DELETE","Are you sre you want to to delete the data?")
                if Deletenew>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="#Mysql123!27",database="riyadb")
                    my_cursor = conn.cursor()
                    my_cursor=conn.cursor()
                    sql="delete from students where Register_Number = %s"
                    value=(self.var_reg.get(),)
                    my_cursor.execute(sql,value)

                else:
                    if not Deletenew:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","The data has been successfully deleted!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # Reset Button
    def reset_data(self):
        self.var_name.set("")
        self.var_reg.set("")
        self.var_dep.set("Select Department")                        
        self.var_year.set("Select Year")
        self.var_mentor.set("")
        self.var_phone.set("")
        self.var_add.set("")
        self.var_busno.set("")
        self.var_book.set("")
        self.var_dname.set("")
        self.var_dcontact.set("")
        self.var_splace.set("")
        self.var_stime.set("")
        self.var_eplace.set("")
        self.var_etime.set("")
        self.var_seat.set("")
        self.var_gen.set("Select Gender")


    # Search button
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("ERROR","Please select an option")

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="#Mysql123!27",database="riyadb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from students where "+str(self.var_combo_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.bus_table.delete(*self.bus_table.get_children())
                    for i in data:
                        self.bus_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   


if __name__ == "__main__":
    root=Tk()
    obj=Bus(root)
    root.mainloop()


