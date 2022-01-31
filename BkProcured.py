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

procureNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
addTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
modTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
delTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
procureNBK.add(addTransF, text='New Supplier Transaction', padding=5)
procureNBK.add(modTransF, text='Modify Supplier Transaction', padding=5)
procureNBK.add(delTransF, text='Remove Supplier Transaction', padding=5)

addTransID = StringVar()
addTransIDL = Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addTransIDE = Entry(addTransF, textvariable=addTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addSuppID = StringVar()
addSuppIDL = Label(addTransF, text="Supplier ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addSuppIDE = Entry(addTransF, textvariable=addSuppID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addSuppName = StringVar()
addSuppNameL = Label(addTransF, text="Supplier Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addSuppNameE = Entry(addTransF, textvariable=addSuppName, width=40, font = ("Berlin Sans FB", 12), bd=2)
addContact = StringVar()
addContactL = Label(addTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addContactE = Entry(addTransF, textvariable=addContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
addBookID = StringVar()
addBookIDL = Label(addTransF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addBookIDE = Entry(addTransF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addBookPrice = StringVar()
addBookPriceL = Label(addTransF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addBookPriceE = Entry(addTransF, textvariable=addBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
addCopies = StringVar()
addCopiesL = Label(addTransF, text="Number of Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addCopiesE = Entry(addTransF, textvariable=addCopies, width=10, font = ("Berlin Sans FB", 12), bd=2)
addTotalL = Label(addTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addButton = Button(addTransF, text="Add", command=addTrans, width=17, font = ("Berlin Sans FB", 12))

modTransID = StringVar()
modTransIDL = Label(modTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modTransIDE = Entry(modTransF, textvariable=modTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modSuppID = StringVar()
modSuppIDL = Label(modTransF, text="Supplier ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modSuppIDE = Entry(modTransF, textvariable=modSuppID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modSuppName = StringVar()
modSuppNameL = Label(modTransF, text="Supplier Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modSuppNameE = Entry(modTransF, textvariable=modSuppName, width=40, font = ("Berlin Sans FB", 12), bd=2)
modContact = StringVar()
modContactL = Label(modTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modContactE = Entry(modTransF, textvariable=modContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
modBookID = StringVar()
modBookIDL = Label(modTransF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modBookIDE = Entry(modTransF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modBookPrice = StringVar()
modBookPriceL = Label(modTransF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modBookPriceE = Entry(modTransF, textvariable=modBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
modCopies = StringVar()
modCopiesL = Label(modTransF, text="Number of Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modCopiesE = Entry(modTransF, textvariable=modCopies, width=10, font = ("Berlin Sans FB", 12), bd=2)
modTotalL = Label(modTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modButton = Button(modTransF, text="Modify", command=modTrans, width=17, font = ("Berlin Sans FB", 12))

delTransID = StringVar()
delTransIDL = Label(delTransF, text="             Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
delTransIDE = Entry(delTransF, textvariable=delTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
delButton = Button(delTransF, text="Remove", command=delTrans, width=17, font = ("Berlin Sans FB", 12))

titleLbl.grid(row=0, column=0, columnspan=6, rowspan=2)
logoutBut.grid(row=1, column=5)
procureNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

addTransIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
addTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
addSuppIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
addSuppIDE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
addSuppNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
addSuppNameE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
addContactL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
addContactE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
addBookIDL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
addBookIDE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
addBookPriceL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
addBookPriceE.grid(row=8, column=1, padx=10, pady=10)
addCopiesL.grid(row=8, column=2, sticky=(E), padx=10, pady=10)
addCopiesE.grid(row=8, column=3, padx=10, pady=10)
addTotalL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
addButton.grid(row=10, column=4, padx=20, pady=10)

modTransIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
modTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
modSuppIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
modSuppIDE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
modSuppNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
modSuppNameE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
modContactL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
modContactE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
modBookIDL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
modBookIDE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
modBookPriceL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
modBookPriceE.grid(row=8, column=1, padx=10, pady=10)
modCopiesL.grid(row=8, column=2, sticky=(E), padx=10, pady=10)
modCopiesE.grid(row=8, column=3, padx=10, pady=10)
modTotalL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
modButton.grid(row=10, column=4, padx=20, pady=10)

delTransIDL.grid(row=3, column=0, padx=10, pady=10)
delTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
delButton.grid(row=4, column=4, padx=20, pady=40)

root.mainloop()