from tkinter import *
from tkinter import ttk, messagebox

def welcomePage():
    return

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    root.quit()

def loggedOut():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    welcomePage()

def addTrans():
    addTotal = Label(addTransF, text="tot", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addTotal.grid(row=9, column=1)
    # clear all entries after adding
    return

def modTrans():
    modTotal = Label(modTransF, text="tot", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modTotal.grid(row=9, column=1)
    # clear all entries after modifying
    return

def delTrans():
    # clear all entries after removing
    return

root = Tk()
root.title("Bookstore Management System")
root.geometry('960x540')
root.iconbitmap(r"images\bms.ico")
root.attributes("-alpha", 0.95)
root.wm_protocol("WM_DELETE_WINDOW", goodBye)
root.resizable(FALSE,FALSE)

sty1 = ttk.Style()
sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)

sty2 = ttk.Style()
sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10, tabmargins=2)

sty3 = ttk.Style()
sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

mainframe = ttk.Frame(root, style="Bookstore.TFrame")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut)

checkOutNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
addTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
modTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
delTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
checkOutNBK.add(addTransF, text='New Check Out')
checkOutNBK.add(modTransF, text='Modify Check Out')
checkOutNBK.add(delTransF, text='Remove Check Out')

addTransID = StringVar()
addTransIDL = Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addTransIDE = Entry(addTransF, textvariable=addTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addCustID = StringVar()
addCustIDL = Label(addTransF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addCustIDE = Entry(addTransF, textvariable=addCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addCustFName = StringVar()
addCustFNameL = Label(addTransF, text="Customer First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addCustFnameE = Entry(addTransF, textvariable=addCustFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
addCustLName = StringVar()
addCustLNameL = Label(addTransF, text="Customer Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addCustLNameE = Entry(addTransF, textvariable=addCustLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
addContact = StringVar()
addContactL = Label(addTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addContactE = Entry(addTransF, textvariable=addContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
addBookID = StringVar()
addBookIDL = Label(addTransF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addBookIDE = Entry(addTransF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addTotalL = Label(addTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addButton = Button(addTransF, text="Add", command=addTrans, width=17, font = ("Berlin Sans FB", 12))

modTransID = StringVar()
modTransIDL = Label(modTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modTransIDE = Entry(modTransF, textvariable=modTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modCustID = StringVar()
modCustIDL = Label(modTransF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modCustIDE = Entry(modTransF, textvariable=modCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modCustFName = StringVar()
modCustFNameL = Label(modTransF, text="Customer First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modCustFnameE = Entry(modTransF, textvariable=modCustFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
modCustLName = StringVar()
modCustLNameL = Label(modTransF, text="Customer Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modCustLNameE = Entry(modTransF, textvariable=modCustLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
modContact = StringVar()
modContactL = Label(modTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modContactE = Entry(modTransF, textvariable=modContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
modBookID = StringVar()
modBookIDL = Label(modTransF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modBookIDE = Entry(modTransF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modTotalL = Label(modTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modButton = Button(modTransF, text="Modify", command=modTrans, width=17, font = ("Berlin Sans FB", 12))

delTransID = StringVar()
delTransIDL = Label(delTransF, text="             Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
delTransIDE = Entry(delTransF, textvariable=delTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
delButton = Button(delTransF, text="Remove", command=delTrans, width=17, font = ("Berlin Sans FB", 12))

titleLbl.grid(row=0, column=0, columnspan=4, rowspan=2)
logoutBut.grid(row=1, column=3)
checkOutNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

addTransIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
addTransIDE.grid(row=3, column=1, padx=10, pady=10)
addCustIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
addCustIDE.grid(row=4, column=1, padx=10, pady=10)
addCustFNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
addCustFnameE.grid(row=5, column=1, padx=10, pady=10)
addCustLNameL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
addCustLNameE.grid(row=6, column=1, padx=10, pady=10)
addContactL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
addContactE.grid(row=7, column=1, padx=10, pady=10)
addBookIDL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
addBookIDE.grid(row=8, column=1, padx=10, pady=10)
addTotalL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
addButton.grid(row=10, column=2, padx=20, pady=40)

modTransIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
modTransIDE.grid(row=3, column=1, padx=10, pady=10)
modCustIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
modCustIDE.grid(row=4, column=1, padx=10, pady=10)
modCustFNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
modCustFnameE.grid(row=5, column=1, padx=10, pady=10)
modCustLNameL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
modCustLNameE.grid(row=6, column=1, padx=10, pady=10)
modContactL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
modContactE.grid(row=7, column=1, padx=10, pady=10)
modBookIDL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
modBookIDE.grid(row=8, column=1, padx=10, pady=10)
modTotalL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
modButton.grid(row=10, column=2, padx=20, pady=40)

delTransIDL.grid(row=3, column=0, padx=10, pady=10)
delTransIDE.grid(row=3, column=1, padx=10, pady=10)
delButton.grid(row=4, column=2, padx=20, pady=40)

root.mainloop()