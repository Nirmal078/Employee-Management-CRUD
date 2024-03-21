from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB import Database

db=Database("OFFICE.db")
app=Tk()
app.title("Employee Management System")
app.geometry("1280x720+0+0")
app.iconbitmap("user-manage_114453.ico")
# app.resizable(False,False)
app.config(bg="black")
app.state("zoomed")


# Global variables to use input
id=StringVar()
name=StringVar()
# age=StringVar()
dob=StringVar()
email=StringVar()
gender=StringVar()
# phone_no=StringVar()





                ################# ENTRIES FRAME #################
entries_frame=Frame(app,bg="lightblue")
entries_frame.pack(side=LEFT,fill=BOTH)

txttitle=Label(entries_frame,text="CRUD OPERATION",font=("cambria",16,"bold"),bg="blue",fg="white",padx=140).grid(row=0,column=0,columnspan=2)
txttitle2=Label(entries_frame,text="EMPLOYEE TABLE",bg="black",fg="yellow",font=("cambria",16,"bold")).grid(ipadx=400,row=0,column=4)

#My wrong way to get backgroung color to fill((((((Title frame
# title_frame=Frame(entries_frame,bg="grey")
# title_frame.place(x=0,y=0,width=1366,height=33)
# entries_frame.pack(fill=X)

# txttitle=Label(title_frame,text="Employee Management System",font=("cambria",16,"bold"),fg="yellow",bg="grey")
# txttitle.place(x=450) )))))))))




# ID lable
lblid=Label(entries_frame,text="ID:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblid.grid(row=1,column=0,padx=10,pady=10,sticky="w")

# getting input for id by creating entry widget
txtid=Entry(entries_frame,textvariable=id,font=("cambria",13),fg="black", width=30)
txtid.grid(row=1,column=1,padx=20,sticky="w")


# Name lable
lblname=Label(entries_frame,text="Name:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblname.grid(row=2,column=0,padx=10,pady=10,sticky="w")

# getting input for name by creating entry widget
txtName=Entry(entries_frame,textvariable=name,font=("cambria",13),fg="black", width=30)
txtName.grid(row=2,column=1,padx=20,sticky="w")



# Age lable
lblage=Label(entries_frame,text="Age:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblage.grid(row=3,column=0,padx=10,pady=10,sticky="w")

# getting input for age by creating entry widget
# txtage=Entry(entries_frame,textvariable=ageinnum,font=("cambria",13),fg="black", width=30)
# txtage.grid(row=2,column=1,padx=20,sticky="w")

def ageinnum(value):
    return value.isdigit()
validationage=entries_frame.register(ageinnum)

txtage=Entry(entries_frame,text=validationage,validate="key",validatecommand=(validationage,"%S"),font=("cambria",13),fg="black", width=30)
txtage.grid(row=3,column=1,padx=20,sticky="w")

# DOB lable
lbldob=Label(entries_frame,text="DOB:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lbldob.grid(row=4,column=0,padx=10,pady=10,sticky="w")

# getting input for dob by creating entry widget
txtdob=Entry(entries_frame,textvariable=dob,font=("cambria",13),fg="black", width=30)
txtdob.grid(row=4,column=1,padx=20,sticky="w")


# Email lable
lblemail=Label(entries_frame,text="Email:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblemail.grid(row=5,column=0,padx=10,pady=10,sticky="w")

# getting input for email by creating entry widget
txtemail=Entry(entries_frame,textvariable=email,font=("cambria",13),fg="black", width=30)
txtemail.grid(row=5,column=1,padx=20,sticky="w")


# Gender label
lblgender=Label(entries_frame,text="Gender:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblgender.grid(row=6,column=0,padx=10,pady=10,sticky="w")

# getting input for gender by creating combobox widget
gendercombobox=ttk.Combobox(entries_frame,textvariable=gender,font=("cambria",13),width=28,state="readonly")
gendercombobox["values"]=("Male",'Female',"Other")
gendercombobox.grid(row=6,column=1,padx=20,sticky="w")


# PHONE_NO Label
lblphone_no=Label(entries_frame,text="Phone_no:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lblphone_no.grid(row=7,column=0,padx=10,pady=10,sticky="nw")

def phoneinnum(value):
    return value.isdigit()
ph_validation=entries_frame.register(phoneinnum)


# getting input for PHONE_NO by creating entry
txtphone_no=Entry(entries_frame,text=ph_validation,validate="key",validatecommand=(ph_validation,"%S"),font=("cambria",13),fg="black",width=30)
txtphone_no.grid(row=7,column=1,padx=20,pady=10,sticky="nw")


# Address lable
lbladdress=Label(entries_frame,text="Address:",font=("cambria",13,"bold"),fg="black",bg="lightblue")
lbladdress.grid(row=8,column=0,padx=10,pady=10,sticky="nw")

# Getting input for address by creating Text
# txtaddress=Entry(entries_frame,textvariable=address,font=("cambria",13),fg="black",width=30)
# txtaddress.grid(row=4,column=1,padx=20,sticky="w")
txtaddress=Text(entries_frame,font=("cambria",13),width=30,height=5)
txtaddress.grid(row=8,column=1,columnspan=3,padx=20,pady=10,sticky="nw")


def getdata(event):
    selected_row=tv.focus()
    data = tv.item(selected_row)
    global row
    row=data["values"]
    # print(row)
    id.set(row[0])
    name.set(row[1])
    # age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    # phone_no.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])

# definiton for display table datum
def displayall():
    tv.delete(*tv.get_children())  # if we call select fn twice this operation clearall all the record and then insert the row values
    for row in db.select():
        tv.insert("",END,values=row)


# definition for add employee
def add_employee():
    if txtid.get() == "" or txtName.get() == "" or txtage.get() == "" or txtemail.get() == "" or txtdob.get() == "" or gendercombobox.get() == "" or txtphone_no.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("INPUT INVALID", "Please fill all the DETAILS")
    else:
        db.insert(txtid.get(),txtName.get(),txtage.get(), txtdob.get(),txtemail.get(),gendercombobox.get(),txtphone_no.get(),txtaddress.get(1.0,END))
        clearall()
        displayall()
        messagebox.showinfo("Success","Employee Details Inserted")



# definition for update employee
def update_employee():
    # if txtemail.get()==row[2]: # and txtid.get()==row[0]:
    #     messagebox.showerror("Unique Contraint Failed","Email is already exists")
    #     return
    if txtid.get() == "" and txtName.get() == "" and txtage.get() == "" and txtemail.get() == "" and txtdob.get() == "" and gendercombobox.get() == "" and txtphone_no.get() == "" and txtaddress.get(1.0, END) == "":
        messagebox.showerror("INPUT INVALID","Enter some details to update")
    else:
        db.update(txtid.get(),txtName.get(),txtage.get(),txtdob.get(),txtemail.get(),gendercombobox.get(),txtphone_no.get(),txtaddress.get(1.0,END))
        messagebox.showinfo("Success","Employee Details Updated")
        clearall()
        displayall()

    

# definition for delete employee
def delete_employee():
    # messagebox.askyesnocancel()

    if txtid.get()=="":
        messagebox.showerror("Operation Failed","Employee ID required")

    else:
        db.delete(txtid.get())
        messagebox.showinfo("Success","Employee Details Deleted")
        clearall()
        displayall()

# definition for clearall data
def clearall():
    # id.set("")
    # name.set("")
    # age.set("")
    # dob.set("")
    # email.set("")
    # gender.set("")
    # phone_no.set("")
    # txtaddress.delete(1.0, END)
    txtid.delete(0,END)
    txtName.delete(0,END)
    txtage.delete(0,END)
    txtdob.delete(0,END)
    txtphone_no.delete(0,END)
    txtemail.delete(0,END)
    gender.set("")
    txtaddress.delete(1.0,END)
    displayall()

                ############# Create a Button Frame for operations ###############
button_frame=Frame(entries_frame,bg="lightblue")
# button_frame.grid(row=9,column=0,columnspan=2,padx=10,pady=10,sticky="w")
button_frame.place(x=0,y=480)

# adFrame=Frame(button_frame,highlightcolor="white",highlightthickness=10)
# adFrame=LabelFrame(button_frame,bd=2,bg="white")
# adFrame.grid(padx=10)
                    ############ Insert Button ####################
btn_insert=Button(button_frame,text="Add Employee",command=add_employee,font=("verdana",12,"bold"),bg="#1aff1a",fg="black",bd=5,width=13,padx=5,pady=5,activebackground="green",activeforeground="white").grid(row=1,column=0,padx=10,pady=5)
# btn_insert.grid(row=9,column=0,padx=10)


# Update Button
btn_update=Button(button_frame,text="Update Employee",command=update_employee,font=("verdana",12,"bold"),bd=5,bg="#3399ff",fg="black",width=13,padx=10,pady=5,activebackground="blue",activeforeground="white").grid(row=1,column=1,padx=10,pady=5)#grid(row=9,column=1,padx=10)

# Delete Button
btn_delete=Button(button_frame,text="Delete Employee",command=delete_employee,font=("verdana",12,"bold"),bd=5,bg="#ff4d4d",fg="black",width=13,padx=20,pady=5,activebackground="red",activeforeground="white").grid(row=2,column=0,padx=10,pady=10)

# clearall Button
btn_clear=Button(button_frame,text="Clear All Fields",command=clearall,font=("verdana",12,"bold"),bd=5,bg="#ffd633",fg="black",width=13,padx=20,pady=5,activebackground="yellow",activeforeground="white").grid(row=2,column=1,padx=10,pady=10)



                         ############# Table Frame ############
tree_frame=Frame(app,bg="white")
tree_frame.place(x=460,y=31,width=910,height=675)

# Creating object to configure table style
style=ttk.Style()
style.configure("mystyle.Treeview",font=("verdana",10),rowheight=60)

# configuring heading style
style.configure("mystyle.Treeview.Heading",font=("verdana",10,"bold"))

# Creating heading rows using treview inside the ttk package
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading(column=1,text="ID")
tv.column(1,width=-10)
tv.heading(column=2,text="NAME")
tv.column(2,width=100)
tv.heading(column=3,text="AGE")
tv.column(3,width=-5)
tv.heading (column=4,text="DOB")
tv.column(4,width=35)
tv.heading (column=5,text="EMAIL")
tv.column(5,width=145)
tv.heading(column=6,text="GENDER")
tv.column(6,width=20)
tv.heading (column=7,text="PHONE_NO")
tv.column(7,width=40)
tv.heading(column=8,text="ADDRESS")
# tv.column(8,width=10)
tv["show"]="headings"
tv.bind("<ButtonRelease-1>",getdata)
tv.pack(fill=X)

# calling display all funtion
displayall()

app.mainloop()