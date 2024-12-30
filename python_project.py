from tkinter import *
from tkinter import ttk
import sqlite3

# Uncomment and run this code once to create the table with the new columns
'''conn = sqlite3.connect("Student.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER, NAME VARCHAR(20), AGE INTEGER, DOB VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20), GRADE VARCHAR(20), ATTENDENCE VARCHAR(20))")
conn.commit()
conn.close()
print("Table created")'''


class Student:
    def __init__(self, main):
        self.main = main
        self.T_Frame = Frame(self.main, height=50, width=1200, background="yellow", bd=2, relief=GROOVE)
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200, bg="yellow")
        self.Title.pack()
        
        self.Frame_1 = Frame(self.main, height=580, width=400, bd=2, relief=GROOVE, bg="yellow")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1, text="Student Details", background="yellow", font="arial 12 bold").place(x=20, y=20)
        
        self.Id = Label(self.Frame_1, text="Id", background="yellow", font="arial 11 bold")
        self.Id.place(x=40, y=60)
        self.Id_Entry = Entry(self.Frame_1, width=40)
        self.Id_Entry.place(x=150, y=60)
        
        self.Name = Label(self.Frame_1, text="Name", background="yellow", font="arial 11 bold")
        self.Name.place(x=40, y=100)
        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)

        self.Age = Label(self.Frame_1, text="Age", background="yellow", font="arial 11 bold")
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB", background="yellow", font="arial 11 bold")
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="Gender", background="yellow", font="arial 11 bold")
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)
 
        self.City = Label(self.Frame_1, text="City", background="yellow", font="arial 11 bold")
        self.City.place(x=40, y=260)
        self.City_Entry = Entry(self.Frame_1, width=40)
        self.City_Entry.place(x=150, y=260)

        self.Grade = Label(self.Frame_1, text="Grade", background="yellow", font="arial 11 bold")
        self.Grade.place(x=40, y=300)
        self.Grade_Entry = Entry(self.Frame_1, width=40)
        self.Grade_Entry.place(x=150, y=300)

        self.Attendence = Label(self.Frame_1, text="Attendence", background="yellow", font="arial 11 bold")
        self.Attendence.place(x=40, y=340)
        self.Attendence_Entry = Entry(self.Frame_1, width=40)
        self.Attendence_Entry.place(x=150, y=340)

        #===============BUTTONS===============#

        self.Button_Frame = Frame(self.Frame_1, height=250, width=250, relief=GROOVE, bd=2, background="yellow")
        self.Button_Frame.place(x=100, y=370)

        self.Add = Button(self.Button_Frame, text="Add", width=25, font="arial 11 bold", command=self.Add)
        self.Add.pack()
        
        self.Delete = Button(self.Button_Frame, text="Delete", width=25, font="arial 11 bold", command=self.Delete)
        self.Delete.pack()
        
        self.Update = Button(self.Button_Frame, text="Update", width=25, font="arial 11 bold", command=self.Update)
        self.Update.pack()

        self.Clear = Button(self.Button_Frame, text="Clear", width=25, font="arial 11 bold", command=self.clear)
        self.Clear.pack()

        self.Frame_2 = Frame(self.main, height=580, width=800, bd=2, relief=GROOVE, bg="yellow")
        self.Frame_2.pack(side=RIGHT)

        # Adding Scrollbars
        self.tree_scroll_y = Scrollbar(self.Frame_2, orient=VERTICAL)
        self.tree_scroll_y.pack(side=RIGHT, fill=Y)
        self.tree_scroll_x = Scrollbar(self.Frame_2, orient=HORIZONTAL)
        self.tree_scroll_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(self.Frame_2, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=25, yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)
        
        self.tree_scroll_y.config(command=self.tree.yview)
        self.tree_scroll_x.config(command=self.tree.xview)

        self.tree.column("#1", anchor=CENTER, width=40)
        self.tree.heading("#1", text="ID")
        
        self.tree.column("#2", anchor=CENTER, width=100)
        self.tree.heading("#2", text="Name")
        
        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=100)
        self.tree.heading("#4", text="Age")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="Address")
        
        self.tree.column("#7", anchor=CENTER)
        self.tree.heading("#7", text="Grade")

        self.tree.column("#8", anchor=CENTER)
        self.tree.heading("#8", text="Attendence")

        self.tree.insert("", index=0, value=(1, "vijay", 18, "12-2-2002", "male", "chennai", "A", "90%"))
        self.tree.insert("", index=1, value=(2, "dijay", 19, "06-2-2001", "male", "hyderabad", "B", "80%"))
        self.tree.insert("", index=2, value=(3, "jay", 18, "08-7-2002", "male", "vizag", "A+", "95%"))
        self.tree.insert("", index=3, value=(4, "vijji", 19, "12-9-2001", "female", "kurnool", "B", "85%"))
        self.tree.insert("", index=4, value=(5, "uday", 20, "11-3-2000", "male", "chennai", "A", "92%"))
        self.tree.insert("", index=5, value=(6, "ram", 17, "06-5-2003", "male", "guntur", "B", "78%"))
        
        self.tree.pack(fill=BOTH, expand=1)

    def Add(self):  
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        grade = self.Grade_Entry.get()
        attendence = self.Attendence_Entry.get() 
        c = sqlite3.connect("Student.db")
        curses = c.cursor()
        curses.execute("INSERT INTO Student(ID, NAME, AGE, DOB, GENDER, CITY ,GRADE, ATTENDENCE) VALUES(?,?,?,?,?,?,?,?)", (id, name, age, dob, gender, city ,grade, attendence))
        c.commit()
        c.close()
        print("Value Inserted")
        self.tree.insert("", "end", values=(id, name, age, dob, gender, city ,grade, attendence))

    def Delete(self):  
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        print(selected_item)
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID=?", (selected_item,))
        print("Value Deleted")
        c.commit()
        c.close()
        self.tree.delete(item)
  
    def Update(self):  
        if not self.tree.selection():
            print("No item selected")
            return

        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        grade = self.Grade_Entry.get()
        attendence = self.Attendence_Entry.get()
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=?, GRADE=?, ATTENDENCE=? WHERE ID=?", (id, name, age, dob, gender, city, grade, attendence, selected_item))
        c.commit()
        c.close()
        print("Values Updated")
        self.tree.item(item, values=(id, name, age, dob, gender, city, grade, attendence))

    def clear(self):
        '''This method will clear the entry fields'''
        self.Id_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.City_Entry.delete(0, END)
        self.Grade_Entry.delete(0, END)
        self.Attendence_Entry.delete(0, END)
        print("Entry Cleared")

main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")        

Student(main)
main.mainloop()
main.mainloop()
