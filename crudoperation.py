
from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import pymysql
from tkinter.ttk import Scrollbar,Treeview

root=Tk(className='Mysql crud operation')
root.geometry('850x500')
global conn
def conction():
    con=mysql.connect(
        host='localhost',
        user='root',
        password='',
        db='student'
    )
    conn=con.cursor()

def insert_data():
    global  id
    id=Id.get()
    global name
    name=Name.get()
    global adress
    adress=Address.get()
    global phone
    phone=Phone.get()
    if  name=='' or address=='' or phone=='':
        Messagebox.showinfo(title='Insert Status',message='All field are required')
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='',
            db='student'
        )
        conn = con.cursor()
        conn.execute("insert into student_profile values(id,'" +name+"','" +adress+"','"+phone+"')")
        conn.execute("commit");
        entry_id.delete(0,END)
        entry_name.delete(0, END)
        entry_address.delete(0, END)
        entry_phone.delete(0, END)
        # show_all()
        display_data()
        Messagebox.showinfo("Insert status"," Data Inserted succefully")
        conn.close()


def update_data():
    id = Id.get()
    name = Name.get()
    address = Address.get()
    phone = Phone.get()
    if name == '' or address == '' or phone == '':
        Messagebox.showinfo(title='Update Status', message='All field are required')
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='',
            db='student'
        )
        conn = con.cursor()
        msg=Messagebox.askyesno("Update status", " Are you sure you want to update", icon='question')
        if msg>0:
            conn.execute(" update student_profile set name='"+ name +"',address='"+ address +"',phone='"+ phone +"' where id ='"+id+"'")
            conn.execute("commit");
            entry_id.delete(0, END)
            entry_name.delete(0, END)
            entry_address.delete(0, END)
            entry_phone.delete(0, END)
            # show_all()
            display_data()
            conn.close()
            return
def get_data():
    id = Id.get()
    # selected = student_records.focus()
    # temp = student_records.item(selected, 'values')
    # id= temp[0]
    # print(id)
    if id == '':
        Messagebox.showinfo(title='Fetch Status', message='Id is compolsary to get data ')
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='',
            db='student'
        )
        conn = con.cursor()
        conn.execute("select * from student_profile where id='"+id+"' ")
        rows=conn.fetchall()
        for row in rows:
            # entry_id.insert(0,row[0])
            entry_name.insert(0,row[1])
            entry_address.insert(0, row[2])
            entry_phone.insert(0, row[3])
        # show_all()
        display_data()
        conn.close()
def delete():
    id = Id.get()
    # selected = student_records.focus()
    # temp = student_records.item(selected, 'values')
    # id = temp[0]
    if id == '':
        Messagebox.showinfo(title='Delete Status', message='Id is compolsary to delete the  data ')
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='',
            db='student'
        )
        conn = con.cursor()
        d_msg=Messagebox.askyesno("Delete status", " Are you sure you delete the data")
        if d_msg>0:
            conn.execute("delete from student_profile where id='" + id + "'")
            conn.execute("commit")
            entry_id.delete(0, END)
            entry_name.delete(0, END)
            entry_address.delete(0, END)
            entry_phone.delete(0, END)
            # show_all()
            display_data()
            conn.close()
            return
def tree_info(event):
    treeinfo =student_records.focus()
    leanerdata=student_records.item(treeinfo)
    item=leanerdata['values']
    Id.set(item[0])
    Name.set(item[1])
    Address.set(item[2])
    Phone.set(item[3])


# def show_all():
#     con = mysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='student'
#     )
#     conn = con.cursor()
#     conn.execute("select * from student_profile ")
#     rows=conn.fetchall()
#     list.delete(0,list.size())
#     for row in rows :
#         inserting_data=str(row[0])+'   '+row[1]+'   '+row[2] +'    '+row[3]
#         list.insert(list.size()+1,inserting_data)
#     conn.close()

def display_data():
    con = mysql.connect(
        host='localhost',
        user='root',
        password='',
        db='student'
    )
    conn = con.cursor()
    conn.execute("select * from student_profile ")
    result=conn.fetchall()
    if len(result) !=0:
        student_records.delete(*student_records.get_children())
        for row in result :
            student_records.insert('',END,value=row)
    conn.execute('commit')
    conn.close()

Id=StringVar()
Name=StringVar()
Address=StringVar()
Phone=StringVar()

#label frame
labelframe=LabelFrame(root)
labelframe.grid(row=0,column=1,ipady=20,padx=40)

id=Label(root,text='Enter id:',font='arial 15')
id.grid(row=0,column=1)

name=Label(root,text=' Name:',font='arial 15')
name.grid(row=1,column=1)

address=Label(root,text='Address:',font='arial 15')
address.grid(row=2,column=1)

phone=Label(root,text='Phone Number:',font='arial 15')
phone.grid(row=3,column=1)

#end label portions

entry_id=Entry(root, textvariable=Id,)
entry_id.grid(row=0,column=2)

entry_name=Entry(root, textvariable=Name,)
entry_name.grid(row=1,column=2)

entry_address=Entry(root, textvariable=Address,)
entry_address.grid(row=2,column=2)


entry_phone=Entry(root, textvariable=Phone,)
entry_phone.grid(row=3,column=2)

# button frame
button_frame=Frame(root,)
button_frame.grid(row=4,column=2)
# button frame
insert=Button(button_frame,text='Insert',font='arial 15 italic',command=insert_data)
insert.grid(row=0,column=2,pady=20,padx=8)
update=Button(button_frame,text='Update',font='arial 15 italic',command=update_data)
update.grid(row=0,column=3,pady=20,padx=8)
delete=Button(button_frame,text='Delete',font='arial 15 italic',command=delete)
delete.grid(row=0,column=4,pady=20,padx=8)
show=Button(button_frame,text='Get',font='arial 15 italic',command=get_data)
show.grid(row=0,column=5,pady=20,padx=8)

#list frame
list_frame=Frame(root,)
list_frame.grid(row=6,column=2)
# list=Listbox(list_frame,width=70)
# list.grid(row=0,column=2)
# show_all()
# list_item = list.cur
# print(list_item)


#-------------------tree view table-------------------------
scroll_y=Scrollbar(list_frame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

student_records=Treeview(list_frame,height=30,column=("std_id","name","address","phone"),yscrollcommand=scroll_y.set)
student_records.heading("std_id",text="StudentId", anchor=CENTER)
student_records.heading("name",text="Student Name", anchor=CENTER)
student_records.heading("address",text="Student Address", anchor=CENTER)
student_records.heading("phone",text="Phone Number", anchor=CENTER)
student_records['show']='headings'

student_records.column("std_id",width=70,stretch=YES, anchor=CENTER)
student_records.column("name",stretch=YES, anchor=CENTER)
student_records.column("address",stretch=YES, anchor=CENTER)
student_records.column("phone",stretch=YES, anchor=CENTER)

student_records.pack(fill=BOTH,expand=1)

student_records.bind('<ButtonRelease>',tree_info)

display_data()
root.mainloop()
