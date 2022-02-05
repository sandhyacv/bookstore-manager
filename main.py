from tkinter import *
from tkinter import ttk, messagebox

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    # root.quit() only removes the title strip image instead for some reason.
    root.destroy()

def welcomePage():
    return

def loggedOut():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    welcomePage()


def asAdmin():
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0)
    Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=2, column=0, pady=30)

    global userEntry
    user = StringVar()
    userEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=user, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userEntry.insert(0, " Enter Username")
    userEntry.grid(row=4, column=0, ipady=10, pady=10)

    global pswdEntry
    pswd = StringVar()
    pswdEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswd, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdEntry.insert(0, " Enter Password")
    pswdEntry.grid(row=6, column=0, ipady=10, pady=10)

    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=7, column=0)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = adminLogin).grid(row=8, column=0, pady=10)
    root.bind("<Return>", adminLogin)

    root.mainloop()

def adminLogin(event=None):
    if userEntry.get() == "admin":
        if pswdEntry.get() == "123":
            homeAdmin()

def homeAdmin():
    messagebox.showinfo(message="Successfully Logged In", title="Bookstore Manager")
    
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
    logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = FLAT, cursor="hand2", command = loggedOut)

    bookProcuredB = Button(mainframe, text = "Book Procured", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookProcured)
    bookReservedB = Button(mainframe, text = "Reserve Book", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved)
    bookCheckOutB = Button(mainframe, text = "Check Out", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = CheckOut)
    editBooksB = Button(mainframe, text = "Edit Books", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = editBook)
    editMemberB = Button(mainframe, text = "Edit Members", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = editMember)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=9, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre', 'Publisher')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))

    search = StringVar()
    searchEntry = Entry(mainframe, width=54, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")

    clearBut = Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END))

    titleLbl.grid(row=0, column=0, columnspan=5, rowspan=2)
    logoutBut.grid(row=1, column=4)

    bookProcuredB.grid(row=2, column=0, pady=10)
    bookReservedB.grid(row=2, column=1, pady=10)
    bookCheckOutB.grid(row=2, column=2, pady=10)
    editBooksB.grid(row=2, column=3, pady=10)
    editMemberB.grid(row=2, column=4, pady=10)

    searchCtg.grid(row=3, column=0, ipadx=4, ipady=3, pady=14)
    searchEntry.grid(row=3, column=1, columnspan=4, ipadx=5, ipady=5, padx=10, pady=14)
    clearBut.grid(row=4, column=4, stick=(E), padx=28)

    root.mainloop()


def bookProcured():
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

    global root
    root.destroy()
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

def bookReserved():
    def addRes():
        # clear all entries after adding
        return

    def modRes():
        # clear all entries after modifying
        return

    def delRes():
        # clear all entries after removing
        return

    global root
    root.destroy()
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

def CheckOut():
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

    global root
    root.destroy()
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

def editBook():
    def addBook():
        # clear all entries after adding
        return

    def modBook():
        # clear all entries after modifying
        return

    def delBook():
        # clear all entries after removing
        return

    global root
    root.destroy()
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
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10)

    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
    logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut)

    BookNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    modBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    BookNBK.add(addBookF, text='Add Book', padding = 5)
    BookNBK.add(modBookF, text='Modify Book', padding = 5)

    addBookID = StringVar()
    addBookIDL = Label(addBookF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookIDE = Entry(addBookF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookName = StringVar()
    addBookNameL = Label(addBookF, text="Book Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookNameE = Entry(addBookF, textvariable=addBookName, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookAuth = StringVar()
    addBookAuthL = Label(addBookF, text="Author:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookAuthE = Entry(addBookF, textvariable=addBookAuth, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookGenre = StringVar()
    addBookGenreL = Label(addBookF, text="Genre:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookGenreE = Entry(addBookF, textvariable=addBookGenre, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookPub = StringVar()
    addBookPubL = Label(addBookF, text="Publisher:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookPubE = Entry(addBookF, textvariable=addBookPub, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookYoP = StringVar()
    addBookYoPL = Label(addBookF, text="Year of Publication:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookYoPE = Entry(addBookF, textvariable=addBookYoP, width=40, font = ("Berlin Sans FB", 12), bd=2)

    addBookNew = StringVar()
    addBookNewL = Label(addBookF, text="New Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookNewE = Entry(addBookF, textvariable=addBookNew, width=10, font = ("Berlin Sans FB", 12), bd=2)

    addBookSec = StringVar()
    addBookSecL = Label(addBookF, text="Second Hand Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookSecE = Entry(addBookF, textvariable=addBookSec, width=10, font = ("Berlin Sans FB", 12), bd=2)

    addBookPrice = StringVar()
    addBookPriceL = Label(addBookF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addBookPriceE = Entry(addBookF, textvariable=addBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)

    addButton = Button(addBookF, text="Add", command=addBook, width=17, font = ("Berlin Sans FB", 12))


    modBookID = StringVar()
    modBookIDL = Label(modBookF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookIDE = Entry(modBookF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookName = StringVar()
    modBookNameL = Label(modBookF, text="Book Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookNameE = Entry(modBookF, textvariable=modBookName, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookAuth = StringVar()
    modBookAuthL = Label(modBookF, text="Author:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookAuthE = Entry(modBookF, textvariable=modBookAuth, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookGenre = StringVar()
    modBookGenreL = Label(modBookF, text="Genre:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookGenreE = Entry(modBookF, textvariable=modBookGenre, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookPub = StringVar()
    modBookPubL = Label(modBookF, text="Publisher:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookPubE = Entry(modBookF, textvariable=modBookGenre, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookYoP = StringVar()
    modBookYoPL = Label(modBookF, text="Year of Publication:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookYoPE = Entry(modBookF, textvariable=modBookYoP, width=40, font = ("Berlin Sans FB", 12), bd=2)

    modBookNew = StringVar()
    modBookNewL = Label(modBookF, text="New Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookNewE = Entry(modBookF, textvariable=modBookNew, width=10, font = ("Berlin Sans FB", 12), bd=2)

    modBookSec = StringVar()
    modBookSecL = Label(modBookF, text="Second Hand Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookSecE = Entry(modBookF, textvariable=modBookSec, width=10, font = ("Berlin Sans FB", 12), bd=2)

    modBookPrice = StringVar()
    modBookPriceL = Label(modBookF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookPriceE = Entry(modBookF, textvariable=modBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)

    modButton = Button(modBookF, text="Modify", command=modBook, width=17, font = ("Berlin Sans FB", 12))

    titleLbl.grid(row=0, column=0, columnspan=6, rowspan=2)
    logoutBut.grid(row=1, column=5)
    BookNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

    addBookIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    addBookNameL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addBookNameE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    addBookAuthL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addBookAuthE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    addBookGenreL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addBookGenreE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    addBookPubL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    addBookPubE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    addBookYoPL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    addBookYoPE.grid(row=8, column=1, padx=10, pady=10, columnspan=3)
    addBookNewL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    addBookNewE.grid(row=9, column=1, padx=10, pady=10)
    addBookSecL.grid(row=9, column=2, sticky=(E), padx=10, pady=10)
    addBookSecE.grid(row=9, column=3, padx=10, pady=10)
    addBookPriceL.grid(row=10, column=0, sticky=(E), padx=10, pady=10)
    addBookPriceE.grid(row=10, column=1, padx=10, pady=10)
    addButton.grid(row=10, column=5, padx=20, pady=10)

    modBookIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modBookIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    modBookNameL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modBookNameE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    modBookAuthL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modBookAuthE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    modBookGenreL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modBookGenreE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    modBookPubL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    modBookPubE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    modBookYoPL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    modBookYoPE.grid(row=8, column=1, padx=10, pady=10, columnspan=3)
    modBookNewL.grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    modBookNewE.grid(row=9, column=1, padx=10, pady=10)
    modBookSecL.grid(row=9, column=2, sticky=(E), padx=10, pady=10)
    modBookSecE.grid(row=9, column=3, padx=10, pady=10)
    modBookPriceL.grid(row=10, column=0, sticky=(E), padx=10, pady=10)
    modBookPriceE.grid(row=10, column=1, padx=10, pady=10)
    modButton.grid(row=10, column=5, padx=20, pady=10)

    root.mainloop()

def editMember():
    def addMember():
        # clear all entries after adding
        return

    def modMember():
        # clear all entries after modifying
        return

    def delMember():
        # clear all entries after removing
        return

    global root
    root.destroy()
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

    memberNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    modMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    delMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    memberNBK.add(addMemberF, text='Add Member', padding=70)
    memberNBK.add(modMemberF, text='Modify Member', padding=67)
    memberNBK.add(delMemberF, text='Remove Member', padding=70)

    addMemberID = StringVar()
    addMemberIDL = Label(addMemberF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addMemberIDE = Entry(addMemberF, textvariable=addMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberFName = StringVar()
    addMemberFNameL = Label(addMemberF, text="First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addMemberFNameE = Entry(addMemberF, textvariable=addMemberFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberLName = StringVar()
    addMemberLNameL = Label(addMemberF, text="Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addMemberLNameE = Entry(addMemberF, textvariable=addMemberLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberContact = StringVar()
    addMemberContactL = Label(addMemberF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    addMemberContactE = Entry(addMemberF, textvariable=addMemberContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addButton = Button(addMemberF, text="Add", command=addMember, width=17, font = ("Berlin Sans FB", 12))

    modMemberID = StringVar()
    modMemberIDL = Label(modMemberF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modMemberIDE = Entry(modMemberF, textvariable=modMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberFName = StringVar()
    modMemberFNameL = Label(modMemberF, text="New First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modMemberFNameE = Entry(modMemberF, textvariable=modMemberFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberLName = StringVar()
    modMemberLNameL = Label(modMemberF, text="New Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modMemberLNameE = Entry(modMemberF, textvariable=modMemberLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberContact = StringVar()
    modMemberContactL = Label(modMemberF, text="New Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modMemberContactE = Entry(modMemberF, textvariable=modMemberContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modButton = Button(modMemberF, text="Modify", command=modMember, width=17, font = ("Berlin Sans FB", 12))

    delMemberID = StringVar()
    delMemberIDL = Label(delMemberF, text="             Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    delMemberIDE = Entry(delMemberF, textvariable=delMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delButton = Button(delMemberF, text="Remove", command=delMember, width=17, font = ("Berlin Sans FB", 12))

    titleLbl.grid(row=0, column=0, columnspan=4, rowspan=2)
    logoutBut.grid(row=1, column=3)
    memberNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    addMemberIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    addMemberFNameL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addMemberFNameE.grid(row=4, column=1, padx=10, pady=10)
    addMemberLNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addMemberLNameE.grid(row=5, column=1, padx=10, pady=10)
    addMemberContactL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addMemberContactE.grid(row=6, column=1, padx=10, pady=10)
    addButton.grid(row=7, column=2, padx=20, pady=40)

    modMemberIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    modMemberFNameL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modMemberFNameE.grid(row=4, column=1, padx=10, pady=10)
    modMemberLNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modMemberLNameE.grid(row=5, column=1, padx=10, pady=10)
    modMemberContactL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modMemberContactE.grid(row=6, column=1, padx=10, pady=10)
    modButton.grid(row=7, column=2, padx=20, pady=40)

    delMemberIDL.grid(row=3, column=0, padx=10, pady=10)
    delMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    delButton.grid(row=4, column=2, padx=20, pady=40)

    root.mainloop()



def searchBox(evt):
    searchCtg.selection_clear()
    searchCtg.current()
    searchCtg.get()

def asCustomer():
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0)

    Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=1, column=0, pady=15)

    global userE
    userV = StringVar()
    userE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=userV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userE.insert(0, " Enter Username")
    userE.grid(row=2, column=0, ipady=10, pady=10)

    global pswdE
    pswdV = StringVar()
    pswdE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswdV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdE.insert(0, " Enter Password")
    pswdE.grid(row=3, column=0, ipady=10, pady=10)

    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=4, column=0)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = memberLogin).grid(row=5, column=0, pady=10)
    Label(mainframe, text = "OR", font = ("Berlin Sans FB", 16), bg="#FFFFFF", fg="#2e5170").grid(row=6, column=0, pady=10)
    Button(mainframe, text = "Continue as Guest", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = homeGuest).grid(row=7, column=0, pady=10)
    root.bind("<Return>", memberLogin)

    root.mainloop()

def memberLogin(event=None):
    if userE.get() == "neha":
        if pswdE.get() == "bird":
            homeMember()

def homeMember():
    messagebox.showinfo("Bookstore Manager", "Successfully Logged In")
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)

    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
    logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut)

    bookReservedBut = Button(mainframe, text = "Reserve Book", width=18, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))

    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")

    clearBut = Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END))

    titleLbl.grid(row=0, column=0, columnspan=2, rowspan=2)
    logoutBut.grid(row=1, column=1, sticky=(E), padx=45)
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)
    bookReservedBut.grid(row=3, column=0)
    clearBut.grid(row=3, column=1, sticky=(E), padx=28)

    root.mainloop()

def homeGuest():
    messagebox.showinfo("Bookstore Manager", "Logged in as Guest")
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
    logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))

    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")

    clearBut = Button(mainframe, text = "Clear", width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END))

    titleLbl.grid(row=0, column=0, columnspan=2, rowspan=2)
    logoutBut.grid(row=1, column=1, sticky=(E), padx=45)
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)
    clearBut.grid(row=3, column=1, sticky=(E), padx=28)

    root.mainloop()



root = Tk()
root.title("Bookstore Management System")
root.geometry('960x540')
root.iconbitmap(r"images\bms.ico")
root.attributes("-alpha", 0.95)
root.wm_protocol("WM_DELETE_WINDOW", goodBye)
root.resizable(FALSE,FALSE)

sty = ttk.Style()
sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
mainframe = ttk.Frame(root, style="Bookstore.TFrame")
mainframe.grid(column=0, row=0)

bgtitle = PhotoImage(file=r"images\welcometitle.png")
Label(mainframe, image = bgtitle, bg="#FFFFFF").grid(row=0, column=0, columnspan=8)
bgimage = PhotoImage(file=r"images\welcomecloud.png")
Label(mainframe, image = bgimage, bg="#FFFFFF").grid(row=0, column=8, rowspan=6)

Label(mainframe, text = "Login As", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e").grid(row=1, column=0, sticky=(W), padx = 15)
Button(mainframe, text = "Admin", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asAdmin).grid(row=2, column=0, pady = 5)
Button(mainframe, text = "Customer", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asCustomer).grid(row=3, column=0, pady = 5)

root.mainloop()
