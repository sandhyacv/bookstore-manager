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

def addRes():
    # clear all entries after adding
    return

def modRes():
    # clear all entries after modifying
    return

def delRes():
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

reserveNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
addResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
modResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
delResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
reserveNBK.add(addResF, text='New Reservation', padding=40)
reserveNBK.add(modResF, text='Modify Reservation', padding=40)
reserveNBK.add(delResF, text='Remove Reservation', padding=40)

addResID = StringVar()
addResIDL = Label(addResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addResIDE = Entry(addResF, textvariable=addResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addCustID = StringVar()
addCustIDL = Label(addResF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addCustIDE = Entry(addResF, textvariable=addCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addBookID = StringVar()
addBookIDL = Label(addResF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
addBookIDE = Entry(addResF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
addButton = Button(addResF, text="Add", command=addRes, width=17, font = ("Berlin Sans FB", 12))

modResID = StringVar()
modResIDL = Label(modResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modResIDE = Entry(modResF, textvariable=modResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modCustID = StringVar()
modCustIDL = Label(modResF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modCustIDE = Entry(modResF, textvariable=modCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modBookID = StringVar()
modBookIDL = Label(modResF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
modBookIDE = Entry(modResF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
modButton = Button(modResF, text="Modify", command=modRes, width=17, font = ("Berlin Sans FB", 12))

delResID = StringVar()
delResIDL = Label(delResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
delResIDE = Entry(delResF, textvariable=delResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
delButton = Button(delResF, text="Remove", command=delRes, width=17, font = ("Berlin Sans FB", 12))

titleLbl.grid(row=0, column=0, columnspan=4, rowspan=2)
logoutBut.grid(row=1, column=3)
reserveNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

addResIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
addResIDE.grid(row=3, column=1, padx=10, pady=10)
addCustIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
addCustIDE.grid(row=4, column=1, padx=10, pady=10)
addBookIDL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
addBookIDE.grid(row=5, column=1, padx=10, pady=10)
addButton.grid(row=6, column=2, padx=20, pady=40)

modResIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
modResIDE.grid(row=3, column=1, padx=10, pady=10)
modCustIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
modCustIDE.grid(row=4, column=1, padx=10, pady=10)
modBookIDL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
modBookIDE.grid(row=5, column=1, padx=10, pady=10)
modButton.grid(row=6, column=2, padx=20, pady=40)

delResIDL.grid(row=3, column=0, padx=10, pady=10)
delResIDE.grid(row=3, column=1, padx=10, pady=10)
delButton.grid(row=4, column=2, padx=20, pady=40)

root.mainloop()