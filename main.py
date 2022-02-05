from tkinter import *
from tkinter import ttk, messagebox

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    # root.quit() only removes the title strip image instead for some reason.
    root.destroy()

def loggedOut():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    welcomePage()

def welcomePage():
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
    mainframe.grid(column=0, row=0)

    bgtitle = PhotoImage(file=r"images\welcometitle.png")
    Label(mainframe, image = bgtitle, bg="#FFFFFF").grid(row=0, column=0, columnspan=8)
    bgimage = PhotoImage(file=r"images\welcomecloud.png")
    Label(mainframe, image = bgimage, bg="#FFFFFF").grid(row=0, column=8, rowspan=6)

    Label(mainframe, text = "Login As", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e").grid(row=1, column=0, sticky=(W), padx = 15)
    Button(mainframe, text = "Admin", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asAdmin).grid(row=2, column=0, pady = 5)
    Button(mainframe, text = "Customer", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asCustomer).grid(row=3, column=0, pady = 5)

    root.mainloop()

def Click(event):
    # cannot unbind. raises error.
    event.widget.configure(state=NORMAL)
    event.widget.delete(0, END)
    # event.widget.unbind('<Button-1>', clicked)


def asAdmin():
    global root
    global userEntry
    global pswdEntry
    global clicked

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

    user = StringVar()
    userEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=user, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userEntry.insert(0, " Enter Username")
    userEntry.grid(row=4, column=0, ipady=10, pady=10)
    clicked = userEntry.bind('<Button-1>', Click)

    pswd = StringVar()
    pswdEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswd, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdEntry.insert(0, " Enter Password")
    pswdEntry.grid(row=6, column=0, ipady=10, pady=10)
    clicked = pswdEntry.bind('<Button-1>', Click)

    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=7, column=0)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = adminLogin).grid(row=8, column=0, pady=10)
    root.bind("<Return>", adminLogin)

    Button(mainframe, text = "Go Back", pady=5, width = 20, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=welcomePage).grid(row=9, column=0, pady=10)

    root.mainloop()

def adminLogin(event=None):
    if userEntry.get() == "admin":
        if pswdEntry.get() == "123":
            homeAdmin()

def homeAdmin():
    # messagebox.showinfo(message="Successfully Logged In", title="Bookstore Manager")
    
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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=5, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = FLAT, cursor="hand2", command = loggedOut).grid(row=1, column=4)

    Button(mainframe, text = "Book Procured", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookProcured).grid(row=2, column=0, pady=10)
    Button(mainframe, text = "Reserve Book", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved).grid(row=2, column=1, pady=10)
    Button(mainframe, text = "Check Out", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = CheckOut).grid(row=2, column=2, pady=10)
    Button(mainframe, text = "Edit Books", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = editBook).grid(row=2, column=3, pady=10)
    Button(mainframe, text = "Edit Members", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = editMember).grid(row=2, column=4, pady=10)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=9, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre', 'Publisher')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=3, column=0, ipadx=4, ipady=3, pady=14)

    search = StringVar()
    searchEntry = Entry(mainframe, width=54, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=3, column=1, columnspan=4, ipadx=5, ipady=5, padx=10, pady=14)
    clicked = searchEntry.bind('<Button-1>', Click)

    Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=4, column=4, sticky=(E), padx=28)
    Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asAdmin).grid(row=5, column=4, sticky=(E), padx=28, pady=10)

    root.mainloop()


def searchBox(evt):
    searchCtg.selection_clear()
    searchCtg.current()
    searchCtg.get()

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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=6, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=5)

    procureNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    modTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    delTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    procureNBK.add(addTransF, text='New Supplier Transaction', padding=5)
    procureNBK.add(modTransF, text='Modify Supplier Transaction', padding=5)
    procureNBK.add(delTransF, text='Remove Supplier Transaction', padding=5)
    procureNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

    addTransID = StringVar()
    Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addTransIDE = Entry(addTransF, textvariable=addTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    addSuppID = StringVar()
    Label(addTransF, text="Supplier ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addSuppIDE = Entry(addTransF, textvariable=addSuppID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addSuppIDE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    addSuppName = StringVar()
    Label(addTransF, text="Supplier Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addSuppNameE = Entry(addTransF, textvariable=addSuppName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addSuppNameE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    addContact = StringVar()
    Label(addTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addContactE = Entry(addTransF, textvariable=addContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addContactE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    addBookID = StringVar()
    Label(addTransF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE = Entry(addTransF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookIDE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    addBookPrice = StringVar()
    Label(addTransF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    addBookPriceE = Entry(addTransF, textvariable=addBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
    addBookPriceE.grid(row=8, column=1, padx=10, pady=10)
    addCopies = StringVar()
    Label(addTransF, text="Number of Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=2, sticky=(E), padx=10, pady=10)
    addCopiesE = Entry(addTransF, textvariable=addCopies, width=10, font = ("Berlin Sans FB", 12), bd=2)
    addCopiesE.grid(row=8, column=3, padx=10, pady=10)
    Label(addTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    Button(addTransF, text="Add", command=addTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=10, column=4, padx=20, pady=10)
    Button(addTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=5, sticky=(E), padx=15, pady=10)

    modTransID = StringVar()
    Label(modTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modTransIDE = Entry(modTransF, textvariable=modTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    modSuppID = StringVar()
    Label(modTransF, text="Supplier ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modSuppIDE = Entry(modTransF, textvariable=modSuppID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modSuppIDE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    modSuppName = StringVar()
    Label(modTransF, text="Supplier Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modSuppNameE = Entry(modTransF, textvariable=modSuppName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modSuppNameE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    modContact = StringVar()
    Label(modTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modContactE = Entry(modTransF, textvariable=modContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modContactE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    modBookID = StringVar()
    Label(modTransF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    modBookIDE = Entry(modTransF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookIDE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    modBookPrice = StringVar()
    Label(modTransF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    modBookPriceE = Entry(modTransF, textvariable=modBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
    modBookPriceE.grid(row=8, column=1, padx=10, pady=10)
    modCopies = StringVar()
    Label(modTransF, text="Number of Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=2, sticky=(E), padx=10, pady=10)
    modCopiesE = Entry(modTransF, textvariable=modCopies, width=10, font = ("Berlin Sans FB", 12), bd=2)
    modCopiesE.grid(row=8, column=3, padx=10, pady=10)
    Label(modTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    Button(modTransF, text="Modify", command=modTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=10, column=4, padx=20, pady=10)
    Button(modTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=5, sticky=(E), padx=15, pady=10)

    delTransID = StringVar()
    Label(delTransF, text="             Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delTransIDE = Entry(delTransF, textvariable=delTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    Button(delTransF, text="Remove", command=delTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=4, column=4, padx=20, pady=40)
    Button(delTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=4, column=5, sticky=(E), padx=15, pady=10)

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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    reserveNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    modResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    delResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    reserveNBK.add(addResF, text='New Reservation', padding=40)
    reserveNBK.add(modResF, text='Modify Reservation', padding=40)
    reserveNBK.add(delResF, text='Remove Reservation', padding=40)
    reserveNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    addResID = StringVar()
    Label(addResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addResIDE = Entry(addResF, textvariable=addResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addResIDE.grid(row=3, column=1, padx=10, pady=10)
    addCustID = StringVar()
    Label(addResF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addCustIDE = Entry(addResF, textvariable=addCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCustIDE.grid(row=4, column=1, padx=10, pady=10)
    addBookID = StringVar()
    Label(addResF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE = Entry(addResF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookIDE.grid(row=5, column=1, padx=10, pady=10)
    Button(addResF, text="Add", command=addRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=6, column=2, padx=20, pady=40)
    # fix button cmd. to homeMember/homeAdmin.
    Button(addResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=6, column=3, sticky=(E), padx=5, pady=10)


    modResID = StringVar()
    Label(modResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modResIDE = Entry(modResF, textvariable=modResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modResIDE.grid(row=3, column=1, padx=10, pady=10)
    modCustID = StringVar()
    Label(modResF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modCustIDE = Entry(modResF, textvariable=modCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modCustIDE.grid(row=4, column=1, padx=10, pady=10)
    modBookID = StringVar()
    Label(modResF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modBookIDE = Entry(modResF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookIDE.grid(row=5, column=1, padx=10, pady=10)
    Button(modResF, text="Modify", command=modRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=6, column=2, padx=20, pady=40)
    Button(modResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=6, column=3, sticky=(E), padx=5, pady=10)


    delResID = StringVar()
    Label(delResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delResIDE = Entry(delResF, textvariable=delResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delResIDE.grid(row=3, column=1, padx=10, pady=10)
    Button(delResF, text="Remove", command=delRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=4, column=2, padx=20, pady=40)
    Button(delResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=4, column=3, sticky=(E), padx=5, pady=10)

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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    checkOutNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
    modTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
    delTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
    checkOutNBK.add(addTransF, text='New Check Out')
    checkOutNBK.add(modTransF, text='Modify Check Out')
    checkOutNBK.add(delTransF, text='Remove Check Out')
    checkOutNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    addTransID = StringVar()
    Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addTransIDE = Entry(addTransF, textvariable=addTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addTransIDE.grid(row=3, column=1, padx=10, pady=10)
    addCustID = StringVar()
    Label(addTransF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addCustIDE = Entry(addTransF, textvariable=addCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCustIDE.grid(row=4, column=1, padx=10, pady=10)
    addCustFName = StringVar()
    Label(addTransF, text="Customer First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addCustFnameE = Entry(addTransF, textvariable=addCustFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCustFnameE.grid(row=5, column=1, padx=10, pady=10)
    addCustLName = StringVar()
    Label(addTransF, text="Customer Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addCustLNameE = Entry(addTransF, textvariable=addCustLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCustLNameE.grid(row=6, column=1, padx=10, pady=10)
    addContact = StringVar()
    Label(addTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    addContactE = Entry(addTransF, textvariable=addContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addContactE.grid(row=7, column=1, padx=10, pady=10)
    addBookID = StringVar()
    Label(addTransF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE = Entry(addTransF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookIDE.grid(row=8, column=1, padx=10, pady=10)
    Label(addTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    Button(addTransF, text="Add", command=addTrans, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=2, padx=20, pady=40)
    Button(addTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=3, sticky=(E), padx=15, pady=10)

    modTransID = StringVar()
    modTransIDL = Label(modTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modTransIDE = Entry(modTransF, textvariable=modTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modTransIDL.grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modTransIDE.grid(row=3, column=1, padx=10, pady=10)
    modCustID = StringVar()
    modCustIDL = Label(modTransF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modCustIDE = Entry(modTransF, textvariable=modCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modCustIDL.grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modCustIDE.grid(row=4, column=1, padx=10, pady=10)
    modCustFName = StringVar()
    modCustFNameL = Label(modTransF, text="Customer First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modCustFnameE = Entry(modTransF, textvariable=modCustFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modCustFNameL.grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modCustFnameE.grid(row=5, column=1, padx=10, pady=10)
    modCustLName = StringVar()
    modCustLNameL = Label(modTransF, text="Customer Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modCustLNameE = Entry(modTransF, textvariable=modCustLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modCustLNameL.grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modCustLNameE.grid(row=6, column=1, padx=10, pady=10)
    modContact = StringVar()
    modContactL = Label(modTransF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modContactE = Entry(modTransF, textvariable=modContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modContactL.grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    modContactE.grid(row=7, column=1, padx=10, pady=10)
    modBookID = StringVar()
    modBookIDL = Label(modTransF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    modBookIDE = Entry(modTransF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookIDL.grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    modBookIDE.grid(row=8, column=1, padx=10, pady=10) 
    Label(modTransF, text="Total Cost:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    Button(modTransF, text="Modify", command=modTrans, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=2, padx=20, pady=40)
    Button(modTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=3, sticky=(E), padx=15, pady=10)

    delTransID = StringVar()
    Label(delTransF, text="             Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delTransIDE = Entry(delTransF, textvariable=delTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delTransIDE.grid(row=3, column=1, padx=10, pady=10)
    Button(delTransF, text="Remove", command=delTrans, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=4, column=2, padx=20, pady=40)
    Button(delTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=4, column=3, sticky=(E), padx=15, pady=10)

    root.mainloop()

def editBook():
    def addBook():
        # clear all entries after adding
        return

    def modBook():
        # clear all entries after modifying
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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=6, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=5)

    BookNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    modBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    BookNBK.add(addBookF, text='Add Book', padding = 5)
    BookNBK.add(modBookF, text='Modify Book', padding = 5)
    BookNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

    addBookID = StringVar()
    Label(addBookF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE = Entry(addBookF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    addBookName = StringVar()
    Label(addBookF, text="Book Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addBookNameE = Entry(addBookF, textvariable=addBookName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookNameE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    addBookAuth = StringVar()
    Label(addBookF, text="Author:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addBookAuthE = Entry(addBookF, textvariable=addBookAuth, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookAuthE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    addBookGenre = StringVar()
    Label(addBookF, text="Genre:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addBookGenreE = Entry(addBookF, textvariable=addBookGenre, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookGenreE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    addBookPub = StringVar()
    Label(addBookF, text="Publisher:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    addBookPubE = Entry(addBookF, textvariable=addBookPub, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookPubE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    addBookYoP = StringVar()
    Label(addBookF, text="Year of Publication:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    addBookYoPE = Entry(addBookF, textvariable=addBookYoP, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookYoPE.grid(row=8, column=1, padx=10, pady=10, columnspan=3)
    addBookNew = StringVar()
    Label(addBookF, text="New Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    addBookNewE = Entry(addBookF, textvariable=addBookNew, width=10, font = ("Berlin Sans FB", 12), bd=2)
    addBookNewE.grid(row=9, column=1, padx=10, pady=10)
    addBookSec = StringVar()
    Label(addBookF, text="Second Hand Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=2, sticky=(E), padx=10, pady=10)
    addBookSecE = Entry(addBookF, textvariable=addBookSec, width=10, font = ("Berlin Sans FB", 12), bd=2)
    addBookSecE.grid(row=9, column=3, padx=10, pady=10)
    addBookPrice = StringVar()
    Label(addBookF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=10, column=0, sticky=(E), padx=10, pady=10)
    addBookPriceE = Entry(addBookF, textvariable=addBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
    addBookPriceE.grid(row=10, column=1, padx=10, pady=10)
    Button(addBookF, text="Add", command=addBook, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=5, padx=20, pady=10)
    Button(addBookF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=6, sticky=(E), padx=15, pady=10)

    modBookID = StringVar()
    Label(modBookF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modBookIDE = Entry(modBookF, textvariable=modBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    modBookName = StringVar()
    Label(modBookF, text="Book Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modBookNameE = Entry(modBookF, textvariable=modBookName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookNameE.grid(row=4, column=1, padx=10, pady=10, columnspan=3)
    modBookAuth = StringVar()
    Label(modBookF, text="Author:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modBookAuthE = Entry(modBookF, textvariable=modBookAuth, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookAuthE.grid(row=5, column=1, padx=10, pady=10, columnspan=3)
    modBookGenre = StringVar()
    Label(modBookF, text="Genre:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modBookGenreE = Entry(modBookF, textvariable=modBookGenre, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookGenreE.grid(row=6, column=1, padx=10, pady=10, columnspan=3)
    modBookPub = StringVar()
    Label(modBookF, text="Publisher:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    modBookPubE = Entry(modBookF, textvariable=modBookPub, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookPubE.grid(row=7, column=1, padx=10, pady=10, columnspan=3)
    modBookYoP = StringVar()
    Label(modBookF, text="Year of Publication:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    modBookYoPE = Entry(modBookF, textvariable=modBookYoP, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modBookYoPE.grid(row=8, column=1, padx=10, pady=10, columnspan=3)
    modBookNew = StringVar()
    Label(modBookF, text="New Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    modBookNewE = Entry(modBookF, textvariable=modBookNew, width=10, font = ("Berlin Sans FB", 12), bd=2)
    modBookNewE.grid(row=9, column=1, padx=10, pady=10)
    modBookSec = StringVar()
    Label(modBookF, text="Second Hand Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=2, sticky=(E), padx=10, pady=10)
    modBookSecE = Entry(modBookF, textvariable=modBookSec, width=10, font = ("Berlin Sans FB", 12), bd=2)
    modBookSecE.grid(row=9, column=3, padx=10, pady=10)
    modBookPrice = StringVar()
    Label(modBookF, text="Book Price:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=10, column=0, sticky=(E), padx=10, pady=10)
    modBookPriceE = Entry(modBookF, textvariable=modBookPrice, width=10, font = ("Berlin Sans FB", 12), bd=2)
    modBookPriceE.grid(row=10, column=1, padx=10, pady=10)
    Button(modBookF, text="Modify", command=modBook, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=5, padx=20, pady=10)
    Button(modBookF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=6, sticky=(E), padx=15, pady=10)

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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    memberNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    modMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    delMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    memberNBK.add(addMemberF, text='Add Member', padding=47)
    memberNBK.add(modMemberF, text='Modify Member', padding=47)
    memberNBK.add(delMemberF, text='Remove Member', padding=47)
    memberNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    addMemberID = StringVar()
    Label(addMemberF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    addMemberIDE = Entry(addMemberF, textvariable=addMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberIDE.grid(row=3, column=1, padx=10, pady=10)    
    addMemberFName = StringVar()
    Label(addMemberF, text="First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    addMemberFNameE = Entry(addMemberF, textvariable=addMemberFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberFNameE.grid(row=4, column=1, padx=10, pady=10)
    addMemberLName = StringVar()
    Label(addMemberF, text="Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addMemberLNameE = Entry(addMemberF, textvariable=addMemberLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberLNameE.grid(row=5, column=1, padx=10, pady=10)
    addMemberContact = StringVar()
    Label(addMemberF, text="        Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addMemberContactE = Entry(addMemberF, textvariable=addMemberContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addMemberContactE.grid(row=6, column=1, padx=10, pady=10)
    Button(addMemberF, text="Add", command=addMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=7, column=2, padx=20, pady=20)
    Button(addMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=8, column=2, sticky=(E), padx=15, pady=10)

    modMemberID = StringVar()
    Label(modMemberF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    modMemberIDE = Entry(modMemberF, textvariable=modMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    modMemberFName = StringVar()
    Label(modMemberF, text="New First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    modMemberFNameE = Entry(modMemberF, textvariable=modMemberFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberFNameE.grid(row=4, column=1, padx=10, pady=10)
    modMemberLName = StringVar()
    Label(modMemberF, text="New Last Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    modMemberLNameE = Entry(modMemberF, textvariable=modMemberLName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberLNameE.grid(row=5, column=1, padx=10, pady=10)
    modMemberContact = StringVar()
    Label(modMemberF, text="New Phone Number:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modMemberContactE = Entry(modMemberF, textvariable=modMemberContact, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modMemberContactE.grid(row=6, column=1, padx=10, pady=10)
    Button(modMemberF, text="Modify", command=modMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=7, column=2, padx=20, pady=20)
    Button(modMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=8, column=2, sticky=(E), padx=15, pady=10)

    delMemberID = StringVar()
    Label(delMemberF, text="             Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delMemberIDE = Entry(delMemberF, textvariable=delMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    Button(delMemberF, text="Remove", command=delMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=4, column=2, padx=20, pady=20)
    Button(delMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=5, column=2, sticky=(E), padx=15, pady=10)

    root.mainloop()


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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2)

    Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=1, column=0, pady=15, columnspan=2)

    global userE
    userV = StringVar()
    userE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=userV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userE.insert(0, " Enter Username")
    userE.grid(row=2, column=0, ipady=10, pady=10, columnspan=2)
    clicked = userE.bind('<Button-1>', Click)

    global pswdE
    pswdV = StringVar()
    pswdE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswdV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdE.insert(0, " Enter Password")
    pswdE.grid(row=3, column=0, ipady=10, pady=10, columnspan=2)
    clicked = pswdE.bind('<Button-1>', Click)

    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=4, column=0, columnspan=2)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = memberLogin).grid(row=5, column=0, pady=10, columnspan=2)
    Label(mainframe, text = "OR", font = ("Berlin Sans FB", 16), bg="#FFFFFF", fg="#2e5170").grid(row=6, column=0, pady=10, columnspan=2)
    Button(mainframe, text = "Continue as Guest", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = homeGuest).grid(row=7, column=0, pady=10, columnspan=2)
    root.bind("<Return>", memberLogin)

    Button(mainframe, text = "Go Back", pady=5, width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=welcomePage).grid(row=7, column=1, pady=10, sticky=(E), padx=25)

    root.mainloop()

def memberLogin(event=None):
    if userE.get() == "neha":
        if pswdE.get() == "bird":
            homeMember()

def homeMember():
    # messagebox.showinfo("Bookstore Manager", "Successfully Logged In")

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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=1, sticky=(E), padx=45)

    Button(mainframe, text = "Reserve Book", width=18, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved).grid(row=3, column=0)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)

    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)
    clicked = searchEntry.bind('<Button-1>', Click)

    Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=3, column=1, sticky=(E), padx=28)
    Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer).grid(row=4, column=1, sticky=(E), padx=28, pady=10)

    root.mainloop()

def homeGuest():
    # messagebox.showinfo("Bookstore Manager", "Logged in as Guest")
    
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
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=1, sticky=(E), padx=45)

    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)

    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)
    clicked = searchEntry.bind('<Button-1>', Click)

    Button(mainframe, text = "Clear", width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=3, column=1, sticky=(E), padx=28)
    Button(mainframe, text = "Go Back", pady=3, width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer).grid(row=4, column=1, sticky=(E), padx=28, pady=10)

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