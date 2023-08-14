from tkinter import *
import tkinter.messagebox as MessageBox
import sqlite3




root = Tk()
root.geometry("1280x720")
root.title("GUIforGAU.com")
root.configure(bg="#f0f0f0")
root.resizable(False, False)
def exit():
    sure = MessageBox.askyesno("EXIT", "Do you want to exit?")
    if sure == True:
        root.destroy()
        

def create_table():
    con = sqlite3.connect("GAU.db")
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Person (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Phone VARCHAR(9) NOT NULL,
            UNIQUE(ID)
        )
    """)
    con.commit()
    con.close()

#------------ Functions --------------------
def Insert():
    if id_entry.get() == "" or name_entry.get() == "" or phone_entry.get() == "":
        MessageBox.showinfo("ALERT", "Please enter all the values")
    else:
        con = sqlite3.connect("GAU.db")
        cursor = con.cursor()

        # Get values from the entry fields
        id = id_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()

        # Execute the INSERT query
        query = "INSERT INTO Person (ID, name, phone) VALUES (?, ?, ?)"
        cursor.execute(query, (id, name, phone))

        con.commit()
        con.close()

        MessageBox.showinfo("Status", "Successfully Inserted")

def Del():
    if id_entry.get() == "":
        MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
        con = sqlite3.connect("GAU.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM Person WHERE ID=?", (id_entry.get(),))
        con.commit()

        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')

        MessageBox.showinfo("Status", "Successfully Deleted")
 
def Update():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if (name == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please enter field you want to update!")
    else:
        con = sqlite3.connect("GAU.db")
        cursor = con.cursor()
        query = "UPDATE Person SET name = ?, phone = ? WHERE ID = ?"
        cursor.execute(query, (name, phone, id))

        con.execute("commit");
        

        MessageBox.showinfo("Status", "Successfully Updated")
        con.close();

def Select():
    if id_entry.get() == "":
        MessageBox.showinfo("ALERT", "ID is required to select a row!")
    else:
        con = sqlite3.connect("GAU.db")
        cursor = con.cursor()

        query = "SELECT * FROM Person WHERE ID = ?"
        cursor.execute(query, (id_entry.get(),))

        rows = cursor.fetchall()

        name_entry.delete(0, 'end')  # Remove previous selected value
        phone_entry.delete(0, 'end')  # Remove previous selected value

        for row in rows:
            name_entry.insert(0, row[1])
            phone_entry.insert(0, row[2])

        con.close()

        MessageBox.showinfo("Status", "Successfully Selected")




#------------ id, name, phone - place  --------------------

id = Label(root, text="Enter ID:", font=("Verdana 15"), bg="#f0f0f0")
id.place(x=50, y=240)
id_entry = Entry(root, font=("verdana 15"), bd=0, bg="#f0f0f0")
id_entry.place(x=170, y=240)



name = Label(root, text="Name:", font=("Verdana 15"), bg="#f0f0f0")
name.place(x=50, y=300)

name_entry = Entry(root, font=("verdana 15"), bd=0, bg="#f0f0f0")
name_entry.place(x=170, y=300)
phone = Label(root, text="Phone:", font=("Verdana 15"), bg="#f0f0f0")
phone.place(x=50, y=360)
phone_entry = Entry(root, font=("verdana 15"), bd=0, bg="#f0f0f0")
phone_entry.place(x=170, y=360)
Frame(width=295, height=2, bg="black").place(x=170, y=270)
Frame(width=295, height=2, bg="black").place(x=170, y=330)
Frame(width=295, height=2, bg="black").place(x=170, y=390)



#------------ Buttons --------------------
btnInsert = Button(root, text="Insert", border=0, bg="#0052d0", fg="white",  command=Insert, font=("verdana 15"))
btnInsert.place(x=100, y=430)

btnDelete = Button(root, text="Delete", border=0, bg="#0052d0", fg="white", command=Del, font=("verdana 15"))
btnDelete.place(x=200, y=430)

btnUpdate = Button(root, text="Update", border=0, bg="#0052d0", fg="white", command=Update, font=("verdana 15"))
btnUpdate.place(x=300, y=430)

btnSelect = Button(root, text="Select", border=0, bg="#0052d0", fg="white", command=Select, font=("Verdana 15"))
btnSelect.place(x=201, y=490)

# bg = PhotoImage(file="clip-sign-up.png")
bg = PhotoImage(file='signup.png')
bg1 = Label(root, image=bg)

logo = PhotoImage(file='logo.png')
logo1 = Label(root, image=logo)




bg1.place(x=400, y=0)
logo1.place(x=180, y=100)


root.protocol("WM_DELETE_WINDOW", exit)
root.mainloop()