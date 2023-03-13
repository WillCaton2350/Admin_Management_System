# (OLD FILE | ADMIN.PY) is the latest update


import tkinter
import customtkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import END
import sqlite3

root = tkinter.Tk()
root.resizable(False, False)
root.title("Data Entry Form")
frame = ttk.Frame(root)
frame.pack()

def clearData():
    fNE.delete(0,END)
    lNE.delete(0,END)
    hCB.set('')
    nCB.set('')
    var = tkinter.IntVar(root)
    varTwo = tkinter.IntVar(root)   
    varThree = tkinter.IntVar(root)
    var.set(18)
    varTwo.set(0)
    varThree.set(0)
    ageSb.config(textvariable=var)
    numCSpin.config(textvariable=varTwo)
    numSemSpin.config(textvariable=varThree)
    rCheck.deselect()
    termsCheck.deselect()

def enterData():
    agreedTC = agreed.get()
    if agreedTC == "Agreed":
        first = fNE.get()
        last = lNE.get()
        if first and last:
            title = hCB.get()
            age = ageSb.get()
            nat = nCB.get()
            numC = numCSpin.get()
            numS = numSemSpin.get()
            regi = rCheck.get()
            print("\n","First name: ",first,"Last name: ",last,"\n",
                    "Title: ",title,"Age: ",age,"Nationality: ",nat,"\n",
                    "Number of courses: ",numC,"\n",
                    "Number of semesters: ",numS,"\n","Registration Status: ",regi)
            print("______________________________________________________________")
        else:
            messagebox.showwarning(title="Error", message="Please enter all required fields")
    else:
        messagebox.showwarning(title="Error", message="Terms & Conditions are required")
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    table_create_query = ''' CREATE TABLE IF NOT EXISTS Student_Data
                            (first_Name TEXT,last_Name TEXT, title TEXT, age INT,nationality, number_of_courses INT, number_of_semesters INT ,registration_Status TEXT)
                        '''
    cursor.execute(table_create_query)
    cursor.execute("INSERT INTO Student_Data VALUES(?,?,?,?,?,?,?,?)", (fNE.get(), lNE.get(), hCB.get(), int(ageSb.get()), nCB.get(), int(numCSpin.get()), int(numSemSpin.get()),
    rCheck.get()))
    conn.commit()
    conn.close()
    
uIF = tkinter.LabelFrame(frame, text="User Information")
uIF.grid(row=0, column=0, padx=20,pady=10)


fN = customtkinter.CTkLabel(uIF, text="First Name")
fN.grid(row=0, column=0)
lN = customtkinter.CTkLabel(uIF, text="Last Name")
lN.grid(row=0, column=1)

fNE = customtkinter.CTkEntry(uIF)
fNE.grid(row=1, column=0) 
lNE = customtkinter.CTkEntry(uIF)
lNE.grid(row=1, column=1)

hL = customtkinter.CTkLabel(uIF, text="Title")
hCB = customtkinter.CTkComboBox(uIF,values=["","Mr","Mrs"])
hL.grid(row=0, column=2)
hCB.grid(row=1, column=2)

ageL = customtkinter.CTkLabel(uIF, text="Age")
ageSb = tkinter.Spinbox(uIF, from_=18, to=100)
ageL.grid(row=2, column=0)
ageSb.grid(row=3, column=0)

nL = tkinter.Label(uIF, text="Nationality")
nCB = customtkinter.CTkComboBox(uIF,values=["","Indian","African-American","Caribbean-American","Hispanic","Chinese"])
nL.grid(row=2, column=1)
nCB.grid(row=3, column=1)

for widget in uIF.winfo_children():
    widget.grid_configure(padx=25, pady=15)

courseF = tkinter.LabelFrame(frame, text="Registration Status")
courseF.grid(row=1, column=0,sticky="news",padx=20,pady=10)
regL = tkinter.Label(courseF)
cVar = tkinter.StringVar()
rCheck = customtkinter.CTkCheckBox(courseF, text="currently registered",variable=cVar,onvalue="Registered",offvalue="Unregistered")
regL.grid(row=0, column=0)
rCheck.grid(row=1, column=0)

numCo = customtkinter.CTkLabel(courseF, text="Number of courses completed")
numCSpin = tkinter.Spinbox(courseF, from_=0, to='infinity')
numCo.grid(row=0, column=1)
numCSpin.grid(row=1, column=1)

numSem = customtkinter.CTkLabel(courseF, text="Number of courses completed semesters")
numSemSpin = tkinter.Spinbox(courseF, from_=0, to='infinity')
numSem.grid(row=0, column=2)
numSemSpin.grid(row=1, column=2)

for widget in courseF.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms.grid(row=2, column=0,sticky="news",padx=20, pady=20)
termsL = customtkinter.CTkLabel(terms, text="Terms & Conditions")
agreed = tkinter.StringVar()
termsCheck = customtkinter.CTkCheckBox(terms,text=" I accept the Terms & Conditions", variable=agreed,onvalue="Agreed",offvalue="N/A")
termsCheck.grid(row=0, column=0)

bTN = customtkinter.CTkButton(frame, text="Enter Data",command=enterData )
bTN.grid(row=3, column=0,sticky="news",padx=10, pady=10)

ClearBTN = customtkinter.CTkButton(frame, text="Clear",command=clearData)
ClearBTN.grid(row=4, column=0,sticky="news",padx=10, pady=10)



root.mainloop()



