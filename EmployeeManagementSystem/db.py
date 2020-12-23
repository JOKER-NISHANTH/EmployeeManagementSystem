import sqlite3

class DataBase():
    def __init__(self,db) -> None:

        # Create Connection Object
        self.con = sqlite3.connect(db)

        # Craete cursor object
        self.cur =self.con.cursor()

        # Create query
        # This query used to create the table
        sql = """
                CREATE TABLE IF NOT EXISTS employees(
                id Integer Primary Key,
                name text,
                age text,
                doj text,
                email text,
                gender text,
                contact text,
                address text
                )
                """
        # Run the query
        self.cur.execute(sql)
        self.con.commit()



    # Insert Method
    def insert(self,name,age,doj,email,gender,contact,address):
        # Prevent for sql injection use placeholder and binding now (NULL,?,?,?,?,?,?,?) Here NULL denote ID it's auto increment
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?) ",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    #Fetch All data from DB

    def fetch(self):
        self.cur.execute("SELECT * from employees")

        rows = self.cur.fetchall()
        return rows
        self.con.commit()

    # Delete the record in DB
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

    # Update a Record in DB
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute(" update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()


Obj = DataBase("Employee.db")

#Obj.insert(name="Sandy",age='21',doj='12-12-2012',email='sandyrx@gmail.com',gender='male',contact='9876543210',address='9/91-A Sathy')
#print(Obj.fetch())
#print(x)
#Obj.remove("2")
# print(Obj.fetch())
# Obj.update(id='1',name='Nisha',age='20',doj='10-10-2010',email='nishasubject90@gmail.com',gender='male',contact='8765432190',address='10/9-C gobi')
# print(Obj.fetch())
