import sqlite3
from tabulate import tabulate
class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="create table if not exists Employee(ID integer primary key,NAME text not null,AGE integer,DOB text,EMAIL text unique,GENDER integer,PHONE_NO integer,ADDRESS text)"
        self.con.execute(sql)
        self.con.commit()
    # Insert Function
    def insert(self,id,name,age,dob,email,gender,PHONE_NO,address):
        self.cur.execute("insert into employee values (?,?,?,?,?,?,?,?)",(id,name,age,dob,email,gender,PHONE_NO,address))
        self.con.commit()

    # Fetching all Data
    def select(self):
        self.cur.execute("select * from employee")
        row=self.cur.fetchall()
        print(tabulate(row,headers=("ID","NAME","AGE","DOB","EMAIL","GENDER","PHONE_NO.","ADDRESS")))
        return row

    # Delete a particular id
    def delete(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()
    # Updating a row
    def update(self,id,name,age,dob,email,gender,PHONE_NO,address):
        self.cur.execute("update employee set name=?,age=?,dob=?,email=?,gender=?,PHONE_NO=?,address=? where id=?",(name,age,dob,email,gender,PHONE_NO,address,id))
        self.con.commit()


# Creating a object to access class database
ob1=Database("OFFICE.db")

# inserting values into database by calling insert function through object
# ob1.insert("Nirmal","23","11-04-2001","nk1332921@gmail.com","Male","6385371439","191,Mettu street,Mullai nagar,Thirumullaivasal")
# ob1.insert("Kumar","25","11-05-2002","k1332921@gmail.com","Male","6385371438","19,Thenpathi,sirkali")

# Deleting values from database by calling delete function through object
# ob1.delete("1")


# Updating values in the database by calling update function through object
# ob1.update("1","Nirmal","25","11-04-2002","nk1332921@gmaill.com","Malee","638537143","192,Mettu street,Mullai nagar,Thirumullaivasal")


# Fetching datum from database by calling select function through object
# ob1.select()