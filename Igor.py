from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

def create_table():
    global conn, cursor
    conn = sqlite3.connect('students.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS TAB_SCHOOL (
                        id_student INTEGER PRIMARY KEY AUTOINCREMENT,
                        registration INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        address TEXT NOT NULL,
                        campus TEXT,
                        period INTEGER,
                        AV1 FLOAT,
                        AV2 FLOAT,
                        AVD FLOAT,
                        AV3 FLOAT,
                        AVDS FLOAT)''')
    except Exception as e:
        print("Error on the table creation: ", e)

def principalWindow():
    
    window = Tk()
    window.geometry("1280x768")
    window.title("Students Registration")
    global tree
    global SEARCH
    global registration,name,email,address,campus,period,AV1,AV2,AVD,AV3,AVDS
    SEARCH = StringVar()
    registration = StringVar()
    name = StringVar()
    email = StringVar()
    address = StringVar()
    campus = StringVar()
    period = StringVar()
    AV1 = StringVar()
    AV2 = StringVar()
    AVD = StringVar()
    AV3 = StringVar()
    AVDS = StringVar()

    TopViewForm = Frame(window, width="600", bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    LFrom = Frame(window, width="350", bg="grey")
    LFrom.pack(side=LEFT, fill=Y)

    LeftViewForm = Frame(window, width="500",bg="dark gray")
    LeftViewForm.pack(side=RIGHT, fill=Y)

    MidViewForm = Frame(window, width="600", bg="white")
    MidViewForm.pack(side=LEFT)

    lbl_text = Label(TopViewForm, text="Student registration management", font=('verdana', 18), width=1000,bg="yellow")
    lbl_text.pack(fill=X)

    Label(LFrom, text=" Fill in for new registration ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Label(LFrom, text="SSN (CPF for Brazilians)  ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri",10,"bold"),textvariable=registration).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Name ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"),textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Address ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Campus ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    campus.set("Campus selection")
    itensCampos = {"Hogwarts","Mordor","Nárnia","Gargantua","Praça Seca"}
    OptionMenu(LFrom, campus, *itensCampos).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Period ", font=("Calibri", 12), bg="grey", fg="black").pack(side=TOP)
    period.set("Select the period")
    itensperiod = {"1-First", "2-Second", "3-Third", "4-Fourth", "5-Fifth", "6-Sixth"}
    OptionMenu(LFrom, period, *itensperiod).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="AV1 ", font=("Calibri", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=AV1).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AV2 ", font=("Calibri", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=AV2).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AVD ", font=("Calibri", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=AVD).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AV3 ", font=("Calibri", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=AV3).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AVDS ", font=("Calibri", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"), textvariable=AVDS).pack(side=TOP, padx=10, fill=X)

    Button(LFrom, text="Register", font=("Arial Black", 12, "bold"), command=Register, bg="green", fg="black").pack(side=TOP, padx=10, pady=30, fill=X)

    lbl_Search = Label(LeftViewForm, text=" Type a name to Search ", font=('verdana', 10),bg="dark grey")
    lbl_Search.pack()

    Search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    Search.pack(side=TOP, padx=10, fill=X)

    btn_Search = Button(LeftViewForm, text="Search", command=Search,bg="light grey")
    btn_Search.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_view = Button(LeftViewForm, text="View all", command=view,bg="light grey")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_Clean = Button(LeftViewForm, text="Clean", command=Clean,bg="light grey")
    btn_Clean.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_delete = Button(LeftViewForm, text="Delete", command=delete,bg="red")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    btn_update = Button(LeftViewForm, text="Update", command=update,bg="green")
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("ID Student","registration","name","Email","address","Campus","Period","AV1","AV2","AVD","AV3","AVDS"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('ID Student', text="ID Student", anchor=W)
    tree.heading('registration', text="Registration", anchor=W)
    tree.heading('name', text="name", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('address', text="Address", anchor=W)
    tree.heading('Campus', text="Campus", anchor=W)
    tree.heading('Period', text="Period", anchor=W)
    tree.heading('AV1', text="AV1", anchor=W)
    tree.heading('AV2', text="AV2", anchor=W)
    tree.heading('AVD', text="AVD", anchor=W)
    tree.heading('AV3', text="AV3", anchor=W)
    tree.heading('AVDS', text="AVDS", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=2)
    tree.column('#1', stretch=NO, minwidth=0, width=60)
    tree.column('#2', stretch=NO, minwidth=0, width=70)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=150)
    tree.column('#6', stretch=NO, minwidth=0, width=60)
    tree.column('#7', stretch=NO, minwidth=0, width=60)
    tree.column('#8', stretch=NO, minwidth=0, width=30)
    tree.column('#9', stretch=NO, minwidth=0, width=30)
    tree.column('#11', stretch=NO, minwidth=0, width=30)
    tree.column('#10', stretch=NO, minwidth=0, width=30)
    tree.column('#11', stretch=NO, minwidth=0, width=30)
    tree.pack()
    view()

def update():
    create_table()
    registration1 = registration.get()
    name1 = name.get()
    email1 = email.get()
    address1 = address.get()
    campus1 = campus.get()
    period1 = period.get()
    AV11 = AV1.get()
    AV21 = AV2.get()
    AVD1 = AVD.get()
    AV31 = AV3.get()
    AVDS1 = AVDS.get()
    Actualitem = tree.focus()
    content = (tree.item(Actualitem))
    itemSelected = content['values']
    conn.execute("UPDATE TAB_SCHOOL SET registration=?,name=?,email=?,address=?,campus=?,period=?,AV1=?,AV2=?,AVD=?,AV3=?,AVDS=? WHERE id_Student = ?", (registration1,name1,email1,address1,campus1,period1,AV11,AV21,AVD1,AV31,AVDS1,itemSelected[0]))
    conn.commit()
    tkMessageBox.showinfo("Message: ", "Registration Updated successfully.")
    Clean()
    view()
    conn.close()

def Register():
    create_table()
    registration1=registration.get()
    name1=name.get()
    email1=email.get()
    address1=address.get()
    campus1=campus.get()
    period1=period.get()
    AV11=AV1.get()
    AV21=AV2.get()
    AV31=AV3.get()
    AVD1=AVD.get()
    AVDS1=AVDS.get()
    conn.execute("INSERT INTO TAB_SCHOOL (registration,name,email,address,campus,period,AV1,AV2,AVD,AV3,AVDS) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(registration1,name1,email1,address1,campus1,period1,AV11,AV21,AVD1,AV31,AVDS1));
    conn.commit()
    tkMessageBox.showinfo("Message: ", "Student registered successfully!")
    view()
    conn.close()

def Clean():
    tree.delete(*tree.get_children())
    view()
    SEARCH.set("")
    registration.set("")
    name.set("")
    email.set("")
    address.set("")
    campus.set("")
    period.set("")
    AV1.set("")
    AV2.set("")
    AVD.set("")
    AV3.set("")
    AVDS.set("")

def delete():
    create_table()
    if not tree.selection():
        tkMessageBox.showinfo("WARNING!", "No items was selected for exclusion")
    else:
        result = tkMessageBox.askquestion("WARNING!", "Are you sure that you want to delete this register?", icon="warning")
        if result == "yes":
            Actualitem = tree.focus()
            content = (tree.item(Actualitem))
            selectedItem = content['values']
            tree.delete(Actualitem)
            cursor = conn.execute("DELETE FROM TAB_SCHOOL WHERE id_Student = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()

def Search():
    create_table()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=conn.execute("SELECT * FROM TAB_SCHOOL WHERE name LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def view():
    create_table()
    tree.delete(*tree.get_children())
    cursor = conn.execute("SELECT * FROM TAB_SCHOOL")
    search = cursor.fetchall()
    for data in search:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",DoubleClick)
    cursor.close()
    conn.close()

def DoubleClick():
    Actualitem = tree.focus()
    content = (tree.item(Actualitem))
    selectedItem = content['values']

    registration.set(selectedItem[1])
    name.set(selectedItem[2])
    email.set(selectedItem[3])
    address.set(selectedItem[4])
    campus.set(selectedItem[5])
    period.set(selectedItem[6])
    AV1.set(selectedItem[7])
    AV2.set(selectedItem[8])
    AVD.set(selectedItem[9])
    AV3.set(selectedItem[10])
    AVDS.set(selectedItem[11])

principalWindow()

if __name__=='__main__':
    mainloop()