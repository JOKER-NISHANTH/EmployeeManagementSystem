from tkinter import *
from tkinter import ttk # for comboBox
from tkinter import messagebox

from db import DataBase
db = DataBase("Employee.db")

root=Tk()
root.title("Employee Mangement System")

# Screen Resolution
# root.geometry('500x500+400+50') # Demo view
root.geometry('1366x768+0+0') # +0+0 ==> X-axies 0 and y-axies 0


#root.config(bg='red') # --> Colores in hex_decimal value #2c3e50
root.config(bg='#2c3e50')


root.state("zoomed")


name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()


# Entries Frame
entries_frame=Frame(root,bg='#535c68')
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text='Employee Mangement System',font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)


# sticky="w" --> for west side align the lable
lblName=Label(entries_frame,text="Name",font=("Calibri",16) , bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName = Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")


lblAge=Label(entries_frame,text="Age",font=("Calibri",16) , bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge = Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")


lbldoj=Label(entries_frame,text="D.O.J",font=("Calibri",16) , bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj = Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblEmail=Label(entries_frame,text="Email",font=("Calibri",16) , bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail = Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

# Gender Combo-Box
lblGender=Label(entries_frame,text="Gender",font=("Calibri",16) , bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
ComboGender=ttk.Combobox(entries_frame,font=("Calibri",16),width=28,textvariable=gender,state="readonly")
ComboGender['values']=("Male","Female")
ComboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")


lblContact=Label(entries_frame,text="Contact No",font=("Calibri",16) , bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtContact = Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w")




# Create Text Field
# columnspan=4 --> Merge the colums
lblAddress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtAddress=Text(entries_frame,width=85,height=5, font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    select_row = tv.focus()
    data = tv.item(select_row)
    global row
    row = data["values"]
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)# Clear Old Address
    txtAddress.insert(END,row[7])# After Clear the address then insert

def displayAll():
    # Delete 1st displayed values
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row) # END -->Like Append

def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtEmail.get()=="" or txtdoj.get()=="" \
        or txtContact.get()=="" or txtAddress.get(1.0,END)=="" or ComboGender.get()=="":
        messagebox.showerror("Error in Input","Please Fill All The Details")
        return
    db.insert(name=txtName.get(),age=txtAge.get(),email=txtEmail.get(),doj=txtdoj.get(),
              contact=txtContact.get(),address=txtAddress.get(1.0,END),gender=ComboGender.get())
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtEmail.get()=="" or txtdoj.get()=="" \
        or txtContact.get()=="" or txtAddress.get(1.0,END)=="" or ComboGender.get()=="":
        messagebox.showerror("Error in Input","Please Fill All The Details")
        return
    db.update(id=row[0],name=txtName.get(),age=txtAge.get(),email=txtEmail.get(),doj=txtdoj.get(),
              contact=txtContact.get(),address=txtAddress.get(1.0,END),gender=ComboGender.get())
    messagebox.showinfo("Success","Record Update")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(id=row[0])
    messagebox.showinfo("Success", "Record Deleted")
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END) # 1.0,END --> StartLine, End--> Constant --> To BottomLine



# Button_Frame
btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

# bd=0 --> Border
btnAdd = Button(btn_frame,command=add_employee,text="Add Details",width=15,
                font=("Calibri",16,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=0,padx=10)

btnEdit = Button(btn_frame,command=update_employee,text="Update Details",width=15,
                font=("Calibri",16,"bold"),fg="white",bg="#2980b9",bd=0).grid(row=0,column=1,padx=10)

btnDelete = Button(btn_frame,command=delete_employee,text="Delete Details",width=15,
                font=("Calibri",16,"bold"),fg="white",bg="#c0392b",bd=0).grid(row=0,column=2,padx=10)

btnClear = Button(btn_frame,command=clearAll,text="Clear Details",width=15,
                font=("Calibri",16,"bold"),fg="white",bg="#f39c12",bd=0).grid(row=0,column=3,padx=10)


# Table Frame
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1366,height=255)
style =ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",14),rowheight=50) # Modify font of the body

style.configure("mystyle.Treeview.Heading",font=("Calibri",15),rowheight=50) # Modify font of the heading

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=1)
tv.heading("2",text="Name")
tv.column("2",width=50)
tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="D.O.J")
tv.column("4",width=20)
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=10)
tv.heading("7",text="Contact")
tv.column("7",width=20)
tv.heading("8",text="Address")
tv['show']="headings"
tv.pack(fill="x")

# <ButtonRelease-1> for capture the clicking event , getData is method
tv.bind("<ButtonRelease-1>",getData)


displayAll()
# For Screen display
root.mainloop()

