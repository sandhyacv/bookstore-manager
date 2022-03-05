from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import date

mode = ""
mycon = mysql.connector.connect(host = "localhost",user = "root", passwd = "ladybug04", database = "bookstore")

# todo: raise errors in update function: when id does not exist.
# todo: replace bookid (in new checkout) with bookname and bookauthor. more convenient.
# todo: replace vendor details (in new book procured) with just vendor name. more convenient. modifying vendor table can be moved to a separate function.
# todo: automatically fill entries in update functions: user can edit them to update records.

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    root.destroy()

def loggedOut():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    welcomePage()

def clearEntry(event):
    # clears entry widget when clicked inside.
    event.widget.configure(state=NORMAL)
    event.widget.delete(0, END)

def adminLogin(event=None):
    global mode
    if userEntry.get() == "admin":
        if pswdEntry.get() == "123":
            mode = "admin"
            homeAdmin()

def memberLogin(event=None):
    global mode
    global user
    mycursor = mycon.cursor()
    mycursor.execute(f"SELECT custid FROM customers WHERE name = '{userE.get()}' AND contact = '{pswdE.get()}' AND member = 'y'")
    users = mycursor.fetchall()
    if len(users) == 1:
        user = users[0][0]
        mode = "memb"
        homeMember()
    elif len(users) == 0:
        messagebox.showerror("Bookstore Manager","Please enter valid name and contact.")

def welcomePage():
    # root definitions and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)

    # background images.
    bgtitle = PhotoImage(file=r"images\welcometitle.png")
    Label(mainframe, image = bgtitle, bg="#FFFFFF").grid(row=0, column=0, columnspan=8)
    bgimage = PhotoImage(file=r"images\welcomecloud.png")
    Label(mainframe, image = bgimage, bg="#FFFFFF").grid(row=0, column=8, rowspan=6)

    # labels and admin mode button and customer mode button.
    Label(mainframe, text = "Login As", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e").grid(row=1, column=0, sticky=(W), padx = 15)
    Button(mainframe, text = "Admin", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asAdmin).grid(row=2, column=0, pady = 5)
    Button(mainframe, text = "Customer", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asCustomer).grid(row=3, column=0, pady = 5)

    root.mainloop()


def asAdmin():
    global root
    global userEntry
    global pswdEntry
    global clicked

    # root definition and configuration.
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0)
    Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=2, column=0, pady=30)

    # username entry widget.
    user = StringVar()
    userEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=user, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userEntry.insert(0, " Enter Username")
    userEntry.grid(row=4, column=0, ipady=10, pady=10)
    # remove default text when entry widget is clicked.
    clicked = userEntry.bind('<Button-1>', clearEntry)

    # password entry widget.
    pswd = StringVar()
    pswdEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswd, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdEntry.insert(0, " Enter Password")
    pswdEntry.grid(row=6, column=0, ipady=10, pady=10)
    # remove default text when entry widget is clicked.
    clicked = pswdEntry.bind('<Button-1>', clearEntry)

    # login button and go back button.
    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=7, column=0)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = adminLogin).grid(row=8, column=0, pady=10)
    root.bind("<Return>", adminLogin)
    Button(mainframe, text = "Go Back", pady=5, width = 20, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=welcomePage).grid(row=9, column=0, pady=10)

    root.mainloop()

def homeAdmin():
    # search results
    results = []

    def searchBox(evt):
        # removes results from previous search.
        for result in results:
            result.destroy()
        
        data = []
        columns = ('Book ID', 'Book Name', 'Author', 'Genre', 'Price')
        # coltxt = "{: <15} {: <40} {: <40} {: <30} {: <15}".format(*columns)
        # Label(mainframe, text = coltxt, bg = "#FFFFFF", font = ("Berlin Sans FB", 16)).grid(row=5, column=0, columnspan = 5, sticky=(W), padx=10, pady=10)
        data.append(columns)

        # get current category and search box entry.
        searchCtg.selection_clear()
        if searchCtg.current() == 0:
            pass
        elif searchCtg.current() == 1:
            ctg = "name"
        elif searchCtg.current() == 2:
            ctg = "author"
        elif searchCtg.current() == 3:
            ctg = "genre"
        elif searchCtg.current() == 4:
            ctg = "publisher"
        se = searchEntry.get()

        # retrieve data and display it.
        mycursor = mycon.cursor()
        mycursor.execute(f"SELECT bookid, name, author, genre, price FROM books WHERE {ctg} LIKE '%{se}%' ORDER BY {ctg}")
        data.extend(mycursor.fetchmany(8))

        # rown = 6
        rown = 5

        if len(data) == 1:
            empty = Label(mainframe, text = "   No Matching Records", bg = "#FFFFFF", font = ("Berlin Sans FB", 16))
            empty.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
            results.append(empty)
            rown = rown + 1

        else:
            for record in data:
                txt = "{: <9} {: <24} {: <24} {: <18} {: <14}".format(*record)
                # string formatting of this type requires monospaced fonts to print properly.
                rec = Label(mainframe, text = txt, bg = "#FFFFFF", font = ("Courier", 12))
                rec.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
                results.append(rec)
                rown = rown + 1

        goback = Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asAdmin)
        goback.grid(row=rown, column=4, sticky=(E), padx=28, pady=10)
        results.append(goback)

    
    # root definition and configuration.
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=5, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = FLAT, cursor="hand2", command = loggedOut).grid(row=1, column=4)

    # menu buttons.
    Button(mainframe, text = "Book Procured", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookProcured).grid(row=2, column=0, pady=10)
    Button(mainframe, text = "Reserve Book", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved).grid(row=2, column=1, pady=10)
    Button(mainframe, text = "Check Out", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = CheckOut).grid(row=2, column=2, pady=10)
    Button(mainframe, text = "Book Details", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookDetails).grid(row=2, column=3, pady=10)
    Button(mainframe, text = "Edit Members", width=14, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = editMember).grid(row=2, column=4, pady=10)

    # search category combobox. choose category to search in.
    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=9, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre', ' Publisher')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    # searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=3, column=0, ipadx=4, ipady=3, pady=14)

    # search entry box. enter what to search for.
    search = StringVar()
    searchEntry = Entry(mainframe, width=54, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=3, column=1, columnspan=4, ipadx=5, ipady=5, padx=10, pady=14)

    root.bind("<Return>", searchBox)
    clicked = searchEntry.bind('<Button-1>', clearEntry)

    # clear button and go back button.
    Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=4, column=4, sticky=(E), padx=28)
    gbk = Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asAdmin)
    gbk.grid(row=5, column=4, sticky=(E), padx=28, pady=10)
    results.append(gbk)

    root.mainloop()


def asCustomer():

    #root definition and configuration.
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2)
    Label(mainframe, text = "MEMBER LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=1, column=0, pady=15, columnspan=2)

    # username entry widget.
    global userE
    userV = StringVar()
    userE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=userV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    userE.insert(0, " Enter Name")
    userE.grid(row=2, column=0, ipady=10, pady=10, columnspan=2)
    # clear default text when entry widget is clicked.
    clicked = userE.bind('<Button-1>', clearEntry)

    # password entry widget.
    global pswdE
    pswdV = StringVar()
    pswdE = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswdV, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    pswdE.insert(0, " Enter Contact Number")
    pswdE.grid(row=3, column=0, ipady=10, pady=10, columnspan=2)
    # clear default text when entry widget is clicked.
    clicked = pswdE.bind('<Button-1>', clearEntry)

    # login button and guest button.
    Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=4, column=0, columnspan=2)
    Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = memberLogin).grid(row=5, column=0, pady=10, columnspan=2)
    Label(mainframe, text = "OR", font = ("Berlin Sans FB", 16), bg="#FFFFFF", fg="#2e5170").grid(row=6, column=0, pady=10, columnspan=2)
    Button(mainframe, text = "Continue as Guest", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = homeGuest).grid(row=7, column=0, pady=10, columnspan=2)
    # enter/return key bound to call memberLogin.
    root.bind("<Return>", memberLogin)
    # go back button.
    Button(mainframe, text = "Go Back", pady=5, width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=welcomePage).grid(row=7, column=1, pady=10, sticky=(E), padx=25)

    root.mainloop()

def homeMember():

    # search results
    results = []

    def searchBox(evt):
        # removes results from previous search.
        for result in results:
            result.destroy()
        
        data = []
        columns = ('Book ID', 'Book Name', 'Author', 'Genre', 'Price')
        # coltxt = "{: <15} {: <40} {: <40} {: <30} {: <15}".format(*columns)
        # Label(mainframe, text = coltxt, bg = "#FFFFFF", font = ("Berlin Sans FB", 16)).grid(row=4, column=0, columnspan = 5, sticky=(W), padx=10, pady=10)
        data.append(columns)

        # get current category and search box entry.
        searchCtg.selection_clear()
        if searchCtg.current() == 0:
            pass
        elif searchCtg.current() == 1:
            ctg = "name"
        elif searchCtg.current() == 2:
            ctg = "author"
        elif searchCtg.current() == 3:
            ctg = "genre"
        elif searchCtg.current() == 4:
            ctg = "publisher"
        se = searchEntry.get()

        # retrieve data and display it.
        mycursor = mycon.cursor()
        mycursor.execute(f"SELECT bookid, name, author, genre, price FROM books WHERE {ctg} LIKE '%{se}%' ORDER BY {ctg}")
        data.extend(mycursor.fetchmany(8))

        # rown = 5
        rown = 4

        if len(data) == 1:
            empty = Label(mainframe, text = "   No Matching Records", bg = "#FFFFFF", font = ("Berlin Sans FB", 16))
            empty.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
            results.append(empty)
            rown = rown + 1

        else:
            for record in data:
                txt = "{: <10} {: <25} {: <25} {: <20} {: <15}".format(*record)
                # string formatting of this type requires monospaced fonts to print properly.
                rec = Label(mainframe, text = txt, bg = "#FFFFFF", font = ("Courier", 12))
                rec.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
                results.append(rec)
                rown = rown + 1
        
        goback = Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer)
        goback.grid(row=rown, column=1, sticky=(E), padx=28, pady=10)
        results.append(goback)

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=1, sticky=(E), padx=45)

    # menu button.
    Button(mainframe, text = "Reserve Book", width=18, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = bookReserved).grid(row=3, column=0)

    # search category combobox. choose category to search in.
    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre', ' Publisher')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    # searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)

    # search entry box. enter what to search for.
    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)

    root.bind("<Return>", searchBox)
    clicked = searchEntry.bind('<Button-1>', clearEntry)

    # clear and go back buttons.
    Button(mainframe, text = "Clear", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=3, column=1, sticky=(E), padx=28)
    gbk = Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer)
    gbk.grid(row=4, column=1, sticky=(E), padx=28, pady=10)
    results.append(gbk)

    root.mainloop()

def homeGuest():
    
    # search results
    results = []

    def searchBox(evt):
        # removes results from previous search.
        for result in results:
            result.destroy()
        
        data = []
        columns = ('Book ID', 'Book Name', 'Author', 'Genre', 'Price')
        # coltxt = "{: <15} {: <40} {: <40} {: <30} {: <15}".format(*columns)
        # Label(mainframe, text = coltxt, bg = "#FFFFFF", font = ("Berlin Sans FB", 16)).grid(row=4, column=0, columnspan = 5, sticky=(W), padx=10, pady=10)
        data.append(columns)

        # get current category and search box entry.
        searchCtg.selection_clear()
        if searchCtg.current() == 0:
            pass
        elif searchCtg.current() == 1:
            ctg = "name"
        elif searchCtg.current() == 2:
            ctg = "author"
        elif searchCtg.current() == 3:
            ctg = "genre"
        elif searchCtg.current() == 4:
            ctg = "publisher"
        se = searchEntry.get()

        # retrieve data and display it.
        mycursor = mycon.cursor()
        mycursor.execute(f"SELECT bookid, name, author, genre, price FROM books WHERE {ctg} LIKE '%{se}%' ORDER BY {ctg}")
        data.extend(mycursor.fetchmany(8))

        # rown = 5
        rown = 4

        if len(data) == 1:
            empty = Label(mainframe, text = "   No Matching Records", bg = "#FFFFFF", font = ("Berlin Sans FB", 16))
            empty.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
            results.append(empty)
            rown = rown + 1

        else:
            for record in data:
                txt = "{: <10} {: <25} {: <25} {: <20} {: <15}".format(*record)
                # string formatting of this type requires monospaced fonts to print properly.
                rec = Label(mainframe, text = txt, bg = "#FFFFFF", font = ("Courier", 12))
                rec.grid(row=rown, column=0, columnspan = 5, sticky=(W), padx=10, pady=5)
                results.append(rec)
                rown = rown + 1

        goback = Button(mainframe, text = "Go Back", pady=3, width = 12, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer)
        goback.grid(row=rown, column=1, sticky=(E), padx=28, pady=10)
        results.append(goback)

    # root definition and configuration.
    global root
    root.destroy() 
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # frame definition and configuration.
    sty = ttk.Style()
    sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=2, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=1, sticky=(E), padx=45)

    # search category combobox. choose category to search in.
    global searchCtg
    searchVar = StringVar()
    searchCtg = ttk.Combobox(mainframe, textvariable = searchVar, font=("Berlin Sans FB", 16), width=12, foreground="#2e2e2e", background="#FFFFFF")
    searchCtg['values'] = (' Search By', ' Book Name', ' Author', ' Genre', ' Publisher')
    searchCtg.current(0)
    searchCtg.state(["readonly"])
    # searchCtg.bind('<<ComboboxSelected>>', searchBox)
    mainframe.option_add('*TCombobox*Listbox.font', ("Berlin Sans FB", 16))
    searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)

    # search entry box. enter what to search for.
    search = StringVar()
    searchEntry = Entry(mainframe, width=50, font=("Berlin Sans FB", 16), textvariable=search, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
    searchEntry.insert(0, " Enter Search Query")
    searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)

    root.bind("<Return>", searchBox)
    clicked = searchEntry.bind('<Button-1>', clearEntry)

    # clear and go back buttons.
    Button(mainframe, text = "Clear", width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command = lambda: searchEntry.delete(0, END)).grid(row=3, column=1, sticky=(E), padx=28)
    gbk = Button(mainframe, text = "Go Back", pady=3, width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief=GROOVE, command=asCustomer)
    gbk.grid(row=4, column=1, sticky=(E), padx=28, pady=10)
    results.append(gbk)

    root.mainloop()


def bookProcured():
    def addTrans():
        # ADD button is clicked.

        # bill total.
        Atotal = float(addBookPriceE.get())*int(addCopiesE.get())
        # Label(addTransF, text="total: ", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=1)
        Label(addTransF, text=str(Atotal), bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=1)

        # adding records to "fromven" table.
        mycursor = mycon.cursor()
        mycursor.execute(f"INSERT INTO fromven(vendid,bookid,copies,cost) VALUES ({int(addSuppIDE.get())},{int(addBookIDE.get())},{int(addCopiesE.get())},{Atotal})")
        mycon.commit()
        # mycursor.execute(f"INSERT INTO vendors(vendid,name,contact) VALUES ({int(addSuppIDE.get())},'{addSuppNameE.get()}','{addContactE.get()}') ON DUPLICATE KEY UPDATE")
        mycon.commit()

        # clear all entries after adding
        addBookPriceE.delete(0, END)
        addBookIDE.delete(0, END)
        addContactE.delete(0, END)
        addSuppNameE.delete(0, END)
        addCopiesE.delete(0, END)
        addSuppIDE.delete(0, END)

        tid.destroy()
        mycursor = mycon.cursor()
        mycursor.execute("SELECT transid FROM fromven ORDER BY transid DESC LIMIT 1")
        transid = mycursor.fetchone()
        transactionid = transid[0]+1
        trid = Label(addTransF, text=transactionid, bg="#FFFFFF", font = ("Berlin Sans FB", 12))
        trid.grid(row=3, column=1, sticky=(W), padx=10, pady=10)
        return

    def modTrans():
        # MODIFY button is clicked.

        # new bill total.
        Mtotal = int(modBookPriceE.get())*int(modCopiesE.get())
        # Label(modTransF, text="total: ", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=1)
        Label(addTransF, text=str(Mtotal), bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=1)

        # update records in "fromven" table.
        mycursor = mycon.cursor()
        mycursor.execute(f"UPDATE fromven SET vendid = {int(modSuppIDE.get())}, bookid = {int(modBookIDE.get())}, copies = {int(modCopiesE.get())}, cost = {Mtotal} WHERE transid = {int(modTransIDE.get())}")
        mycon.commit()

        # clear all entries after adding
        modBookPriceE.delete(0, END)
        modBookIDE.delete(0, END)
        modContactE.delete(0, END)
        modSuppNameE.delete(0, END)
        modCopiesE.delete(0, END)
        modSuppIDE.delete(0, END)
        modTransIDE.delete(0, END)
        return

    def delTrans():
        # REMOVE button is clicked.
        # remove records from "fromven" table.
        mycursor = mycon.cursor()
        mycursor.execute(f"DELETE FROM fromven WHERE transid = {int(delTransIDE.get())}")
        mycon.commit()

        # clear all entries after removing
        delTransIDE.delete(0, END)
        return

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # styles.
    sty1 = ttk.Style()
    sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    sty2 = ttk.Style()
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10, tabmargins=2)
    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    # mainframe definition and configuration.
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=6, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=5)

    # notebook and frames definition.
    procureNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    modTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    delTransF = ttk.Frame(procureNBK, style="Bookstore.TFrame")
    procureNBK.add(addTransF, text='New Supplier Transaction', padding=5)
    procureNBK.add(modTransF, text='Modify Supplier Transaction', padding=5)
    procureNBK.add(delTransF, text='Remove Supplier Transaction', padding=5)
    procureNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

    # add transaction frame.
    # transaction id is auto incremented.
    Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    mycursor = mycon.cursor()
    mycursor.execute("SELECT transid FROM fromven ORDER BY transid DESC LIMIT 1")
    transid = mycursor.fetchone()
    transactionid = transid[0]+1
    tid = Label(addTransF, text=transactionid, bg="#FFFFFF", font = ("Berlin Sans FB", 12))
    tid.grid(row=3, column=1, sticky=(W), padx=10, pady=10)
    # labels and entry widgets for transaction details.
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
    # add and go back button.
    Button(addTransF, text="Add", command=addTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=10, column=4, padx=20, pady=10)
    Button(addTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=5, sticky=(E), padx=15, pady=10)


    # modify transaction frame.
    # labels and entry widgets for transaction details.
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
    # modify and go back button.
    Button(modTransF, text="Modify", command=modTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=10, column=4, padx=20, pady=10)
    Button(modTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=5, sticky=(E), padx=15, pady=10)

    # remove transaction frame.
    delTransID = StringVar()
    Label(delTransF, text="             Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delTransIDE = Entry(delTransF, textvariable=delTransID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delTransIDE.grid(row=3, column=1, padx=10, pady=10, columnspan=3)
    # remove and go back button.
    Button(delTransF, text="Remove", command=delTrans, width=17, cursor="hand2", font = ("Berlin Sans FB", 12)).grid(row=4, column=4, padx=20, pady=40)
    Button(delTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=4, column=5, sticky=(E), padx=15, pady=10)

    root.mainloop()

def bookReserved():
    def addRes():
        # add button clicked.
        # adding record to "reserved" table.
        mycursor = mycon.cursor()
        # mycursor.execute(f"INSERT INTO reserved(custid, bookid, copies, date, fulfilled) VALUES ({int(addCustIDE.get())},{int(addBookIDE.get())},{int(addCopiesE.get())},{addDateE.get()},{addFulfilledE.get()})")
        if mode == "memb":
            mycursor.execute(f"INSERT INTO reserved(custid, bookid, copies, date) VALUES ({int(user)},{int(addBookIDE.get())},{int(addCopiesE.get())},'{str(date.today())}')")
            mycon.commit()
        elif mode == "admin":
            mycursor.execute(f"INSERT INTO reserved(custid, bookid, copies, date) VALUES ({int(addCustIDE.get())},{int(addBookIDE.get())},{int(addCopiesE.get())},'{str(date.today())}')")
            mycon.commit()
            addCustIDE.delete(0, END)

        # clear all entries after adding
        addBookIDE.delete(0, END)
        addCopiesE.delete(0, END)
        # addDateE.delete(0, END)
        # addFulfilledE.delete(0, END)

        return

    def modRes():
        # modify button clicked.
        # updating record in "reserved" table.
        mycursor  = mycon.cursor()
        mycursor.execute(f"UPDATE reserved SET custid = {int(modCustIDE.get())}, bookid = {int(modBookIDE.get())}, copies = {int(modCopiesE.get())}, date = '{modDateE.get()}', fulfilled = '{modFulfilledE.get()}' WHERE resid = {int(modResIDE.get())}")
        mycon.commit()

        # clear all entries after modifying
        modResIDE.delete(0, END)
        modCustIDE.delete(0, END)
        modBookIDE.delete(0, END)
        return

    def delRes():
        # remove button clicked.
        # deleting record from "reserved" table.
        mycursor =  mycon.cursor()
        mycursor.execute(f"DELETE FROM reserved WHERE resid = {int(delResIDE.get())}")
        mycon.commit()

        # clear all entries after removing
        delResIDE.delete(0, END)
        return

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # styles.
    sty1 = ttk.Style()
    sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    sty2 = ttk.Style()
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10, tabmargins=2)
    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    # mainframe definition and configuration.
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    # notebook and frames definition.
    reserveNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    modResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    delResF = ttk.Frame(reserveNBK, style="Bookstore.TFrame")
    reserveNBK.add(addResF, text='New Reservation', padding=40)
    reserveNBK.add(modResF, text='Modify Reservation', padding=40)
    reserveNBK.add(delResF, text='Remove Reservation', padding=40)
    reserveNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    # add reservation frame.
    # reservation id is auto-incremented.
    Label(addResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    mycursor = mycon.cursor()
    mycursor.execute("SELECT resid FROM reserved ORDER BY resid DESC LIMIT 1")
    resid = mycursor.fetchone()
    reservationid = resid[0]+1
    Label(addResF, text=reservationid, bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=1, sticky=(W), padx=10, pady=10)
    # labels and entry widgets for reservation details.
    addCustID = StringVar()
    Label(addResF, text="Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=0, sticky=(E), padx=10, pady=10)
    if mode == "memb":
        # user id automatically displayed for members.
        Label(addResF, text=user, bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=4, column=1, sticky=(W), padx=10, pady=10)
    elif mode == "admin":
        addCustIDE = Entry(addResF, textvariable=addCustID, width=40, font = ("Berlin Sans FB", 12), bd=2)
        addCustIDE.grid(row=4, column=1, padx=10, pady=10)
    addBookID = StringVar()
    Label(addResF, text="Book IDs:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addBookIDE = Entry(addResF, textvariable=addBookID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addBookIDE.grid(row=5, column=1, padx=10, pady=10)
    addCopies = StringVar()
    Label(addResF, text="Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    addCopiesE = Entry(addResF, textvariable=addCopies, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCopiesE.grid(row=6, column=1, padx=10, pady=10)
    # addDate = StringVar()
    Label(addResF, text="Date:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    Label(addResF, text = str(date.today()), bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=1, sticky=(W), padx=10, pady=10)
    # addDateE = Entry(addResF, textvariable=addDate, width=40, font = ("Berlin Sans FB", 12), bd=2)
    # addDateE.grid(row=7, column=1, padx=10, pady=10)
    # new reservations would anyways be unfulfilled?
    # addFulfilled = StringVar()
    # Label(addResF, text="Fulfilled(y/n):", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    # addFulfilledE = Entry(addResF, textvariable=addFulfilled, width=40, font = ("Berlin Sans FB", 12), bd=2)
    # addFulfilledE.grid(row=8, column=1, padx=10, pady=10)
    # add button.
    Button(addResF, text="Add", command=addRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=9, column=2, padx=20, pady=40)
    # go back button.
    if mode == "admin":
        Button(addResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=9, column=3, sticky=(E), padx=5, pady=10)
    elif mode == "memb":
        Button(addResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeMember).grid(row=9, column=3, sticky=(E), padx=5, pady=10)

    # modify reservation frame.
    # labels and entry widgets for reservation details.
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
    modCopies = StringVar()
    Label(modResF, text="Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=6, column=0, sticky=(E), padx=10, pady=10)
    modCopiesE = Entry(modResF, textvariable=modCopies, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modCopiesE.grid(row=6, column=1, padx=10, pady=10)
    modDate = StringVar()
    Label(modResF, text="Date:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=7, column=0, sticky=(E), padx=10, pady=10)
    modDateE = Entry(modResF, textvariable=modDate, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modDateE.grid(row=7, column=1, padx=10, pady=10)
    modFulfilled = StringVar()
    Label(modResF, text="Fulfilled(y/n):", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=8, column=0, sticky=(E), padx=10, pady=10)
    modFulfilledE = Entry(modResF, textvariable=modFulfilled, width=40, font = ("Berlin Sans FB", 12), bd=2)
    modFulfilledE.grid(row=8, column=1, padx=10, pady=10)
    # modify button.
    Button(modResF, text="Modify", command=modRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=9, column=2, padx=20, pady=10)
    # go back button.
    if mode == "admin":
        Button(modResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=9, column=3, sticky=(E), padx=5, pady=10)
    elif mode == "memb":
        Button(modResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeMember).grid(row=9, column=3, sticky=(E), padx=5, pady=10)
    
    # delete transaction frame.
    delResID = StringVar()
    Label(delResF, text="Reservation ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delResIDE = Entry(delResF, textvariable=delResID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delResIDE.grid(row=3, column=1, padx=10, pady=10)
    # remove button.
    Button(delResF, text="Remove", command=delRes, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=4, column=2, padx=20, pady=40)
    # go back button.
    if mode == "admin":
        Button(delResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=4, column=3, sticky=(E), padx=5, pady=10)
    elif mode == "memb":
        Button(delResF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeMember).grid(row=4, column=3, sticky=(E), padx=5, pady=10)

    root.mainloop()

def CheckOut():
    def addTrans():
        # check if customer already exists in "customers" table.
        name = addCustFNameE.get() + " " + addCustLNameE.get()
        mycursor  =  mycon.cursor()
        mycursor.execute(f"SELECT custid FROM customers WHERE name = '{name}' AND contact = '{addContactE.get()}'")
        custid = mycursor.fetchone()
        if custid == None:
            # if new customer, create record in "customers" table.
            mycursor.execute(f"INSERT INTO customers(name, contact) VALUES ('{name}', '{addContactE.get()}')")
            mycon.commit()

        # retrieve customer id from "customers" table.
        mycursor.execute(f"SELECT custid FROM customers WHERE name = '{name}' AND contact = '{addContactE.get()}'")
        custid = mycursor.fetchone()
        customerid = custid[0]
        # retrieve book price from "books" table.
        mycursor.execute(f"SELECT price FROM books WHERE bookid = {int(addBookIDE.get())}")
        price  = mycursor.fetchone()
        pricebook = price[0]
        # retrieve member status from "customers" table.
        mycursor.execute(f"SELECT member FROM customers WHERE custid = {customerid}")
        memberstatus = mycursor.fetchone()
        memberstatusstr = memberstatus[0]

        # check if customer is a member. if member apply discount.
        if memberstatusstr == "y":
            discount = 0.1
        else:
            discount = 0
        
        totalnodiscount  = pricebook * int(addCopies.get())
        total = totalnodiscount - (discount)*totalnodiscount
        
        # displays bill details.
        messagebox.showinfo("Bookstore Manager", f"Total Cost    : ₹{totalnodiscount} \nDiscount      : {discount*100}% \nAmount Payable: ₹{total}")

        # create new transaction in "checkout" table.
        mycursor.execute(f"INSERT INTO checkout(custid,bookid,copies,price,discounted) VALUES ({customerid}, {int(addBookIDE.get())}, {int(addCopiesE.get())}, {totalnodiscount}, {total})")
        mycon.commit()

        # update copies available in "books" table.
        if addNorUE.get() == "n":
            mycursor.execute(f"UPDATE books SET new = new - {int(addCopiesE.get())} WHERE bookid = {int(addBookIDE.get())}")
        elif addNorUE.get() == "u":
            mycursor.execute(f"UPDATE books SET used = used - {int(addCopiesE.get())} WHERE bookid = {int(addBookIDE.get())}")
        mycon.commit()

        # clear all entries after adding
        addBookIDE.delete(0, END)
        addContactE.delete(0, END)
        addCopiesE.delete(0, END)
        addCustFNameE.delete(0, END)
        addCustLNameE.delete(0, END)
        addNorUE.delete(0, END)
        return

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # styles.
    sty1 = ttk.Style()
    sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    sty2 = ttk.Style()
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10, tabmargins=2)
    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    # maninframe definition and configuration.
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    # notebook and frames definition.
    checkOutNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addTransF = ttk.Frame(checkOutNBK, style="Bookstore.TFrame")
    checkOutNBK.add(addTransF, text='New Check Out')
    checkOutNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    # add transaction frame.
    # transaction id is auto incremented.
    Label(addTransF, text="Transaction ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    mycursor = mycon.cursor()
    mycursor.execute("SELECT transid FROM checkout ORDER BY transid DESC LIMIT 1")
    transid = mycursor.fetchone()
    transactionid = transid[0]+1
    Label(addTransF, text=transactionid, bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=1, sticky=(W), padx=10, pady=10)
    # labels and entries for checkout details.
    addCustFName = StringVar()
    Label(addTransF, text="Customer First Name:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=5, column=0, sticky=(E), padx=10, pady=10)
    addCustFNameE = Entry(addTransF, textvariable=addCustFName, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCustFNameE.grid(row=5, column=1, padx=10, pady=10)
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
    addCopies = StringVar()
    Label(addTransF, text="Copies:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=9, column=0, sticky=(E), padx=10, pady=10)
    addCopiesE = Entry(addTransF, textvariable=addCopies, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addCopiesE.grid(row=9, column=1, padx=10, pady=10)
    addNorU = StringVar()
    Label(addTransF, text="New or Used (n/u): ", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=10, column=0, sticky=(E), padx=10, pady=10)
    addNorUE = Entry(addTransF, textvariable=addNorU, width=40, font = ("Berlin Sans FB", 12), bd=2)
    addNorUE.grid(row=10, column=1, padx=10, pady=10)

    # add and go back button.
    Button(addTransF, text="Add", command=addTrans, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=11, column=2, padx=20, pady=30)
    Button(addTransF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=11, column=3, sticky=(E), padx=15, pady=10)

    root.mainloop()

def bookDetails():
    def addBook():
        # add button clicked.
        # create new record in "books" table.
        mycursor =  mycon.cursor()
        mycursor.execute(f"INSERT INTO books(name,author,genre,publisher,yop,price,new,used) VALUES ('{addBookNameE.get()}','{addBookAuthE.get()}','{addBookGenreE.get()}','{addBookPubE.get()}','{addBookYoPE.get()}',{float(addBookPriceE.get())},{int(addBookNewE.get())},{int(addBookSecE.get())})")
        mycon.commit()

        # clear all entries after adding
        addBookAuthE.delete(0, END)
        addBookGenreE.delete(0, END)
        addBookNameE.delete(0, END)
        addBookNewE.delete(0, END)
        addBookPriceE.delete(0, END)
        addBookPubE.delete(0, END)
        addBookSecE.delete(0, END)
        addBookYoPE.delete(0, END)
        return

    def modBook():
        # modify button clicked.
        # update record in "books" table.
        mycursor = mycon.cursor()
        mycursor.execute(f"UPDATE books SET name = '{modBookNameE.get()}', author = '{modBookAuthE.get()}', genre = '{modBookGenreE.get()}', publisher = '{modBookPubE.get()}', yop = '{modBookYoPE.get()}', price = {float(modBookPriceE.get())}, new = {int(modBookNewE.get())}, used = {int(modBookSecE.get())} WHERE bookID = {int(modBookIDE.get())}")
        mycon.commit()

        # clear all entries after modifying
        modBookAuthE.delete(0, END)
        modBookGenreE.delete(0, END)
        modBookIDE.delete(0, END)
        modBookNameE.delete(0, END)
        modBookNewE.delete(0, END)
        modBookPriceE.delete(0, END)
        modBookPubE.delete(0, END)
        modBookSecE.delete(0, END)
        modBookYoPE.delete(0, END)
        return

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # styles.
    sty1 = ttk.Style()
    sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    sty2 = ttk.Style()
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10)
    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    # mainframe definition and configuration.
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=6, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=5)

    # notebook and frames defintion.
    BookNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    modBookF = ttk.Frame(BookNBK, style="Bookstore.TFrame")
    BookNBK.add(addBookF, text='Add Book', padding = 5)
    BookNBK.add(modBookF, text='Modify Book', padding = 5)
    BookNBK.grid(row=2, column=0, columnspan=6, sticky=(W))

    # add book frame.
    # book id is auto incremented.
    Label(addBookF, text="Book ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, sticky=(E), padx=10, pady=10)
    mycursor = mycon.cursor()
    mycursor.execute("SELECT bookid FROM books ORDER BY bookid DESC LIMIT 1")
    bookid = mycursor.fetchone()
    bid = bookid[0]+1
    Label(addBookF, text=bid, bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=1, sticky=(W), padx=10, pady=10)
    # labels and entry widgets for book details.
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
    # add button and go back button.
    Button(addBookF, text="Add", command=addBook, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=5, padx=20, pady=10)
    Button(addBookF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=6, sticky=(E), padx=15, pady=10)

    # modify book frame.
    # labels and entry widgets for book details.
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
    # modify and go back button.
    Button(modBookF, text="Modify", command=modBook, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=10, column=5, padx=20, pady=10)
    Button(modBookF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=10, column=6, sticky=(E), padx=15, pady=10)
    
    root.mainloop()

def editMember():
    def addMember():
        # todo: if customer does not already exist?
        # add button clicked.
        # update member status of existing customer to 'y'.
        membername = addMemberFNameE.get() + " " + addMemberLNameE.get()
        mycursor = mycon.cursor()
        mycursor.execute(f"UPDATE customers SET member = 'y' WHERE name LIKE '{membername}' AND contact LIKE '{addMemberContactE.get()}'" )
        mycon.commit()

        # display member id.
        mycursor.execute(f"SELECT custid FROM customers WHERE name LIKE '{membername}' AND contact LIKE '{addMemberContactE.get()}'")
        customerid  = mycursor.fetchone()
        displayMemberID = 0 
        displayMemberID = customerid[0]
        messagebox.showinfo("Bookstore Manager", f"Your Member ID Is: {displayMemberID}")

        # clear all entries after adding
        addMemberFNameE.delete(0, END)
        addMemberLNameE.delete(0, END)
        addMemberContactE.delete(0, END)
        return

    def modMember():
        # modify button clicked.
        # update record in "customers" table.
        membername =  modMemberFNameE.get() + " " + modMemberLNameE.get()

        mycursor=mycon.cursor()
        mycursor.execute(f"UPDATE customers SET name = '{membername}', contact = '{modMemberContactE.get()}' WHERE custid = {int(modMemberIDE.get())}")
        mycon.commit()

        # clear all entries after modifying
        modMemberContactE.delete(0, END)
        modMemberFNameE.delete(0, END)
        modMemberLNameE.delete(0, END)
        modMemberIDE.delete(0, END)
        return

    def delMember():
        # remove button clicked.
        # set member status of existing member to 'n'.
        mycursor = mycon.cursor()
        mycursor.execute(f"UPDATE customers SET member = 'n' WHERE  custid = {delMemberIDE.get()}")
        mycon.commit()

        # clear all entries after removing
        delMemberIDE.delete(0, END)
        return

    # root definition and configuration.
    global root
    root.destroy()
    root = Tk()
    root.title("Bookstore Management System")
    root.geometry('960x540')
    root.iconbitmap(r"images\bms.ico")
    root.attributes("-alpha", 0.95)
    root.wm_protocol("WM_DELETE_WINDOW", goodBye)
    root.resizable(FALSE,FALSE)

    # styles.
    sty1 = ttk.Style()
    sty1.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
    sty2 = ttk.Style()
    sty2.configure("Bookstore.TNotebook", background="#FFFFFF", padding=10, tabmargins=2)
    sty3 = ttk.Style()
    sty3.configure("Bookstore.TNotebook.Tab", font=("Berlin Sans FB", 12), padding=5)

    # mainframe definition and configuration.
    mainframe = ttk.Frame(root, style="Bookstore.TFrame")
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # background image.
    titleImg = PhotoImage(file = r"images\titlestrip.png").subsample(2,2)
    Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0, columnspan=4, rowspan=2)
    Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 12), relief = "flat", cursor="hand2", command = loggedOut).grid(row=1, column=3)

    # notebook and frames definition.
    memberNBK = ttk.Notebook(mainframe, width=940, height=390, style="Bookstore.TNotebook")
    addMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    modMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    delMemberF = ttk.Frame(memberNBK, style="Bookstore.TFrame")
    memberNBK.add(addMemberF, text='Add Member', padding=47)
    memberNBK.add(modMemberF, text='Modify Member', padding=47)
    memberNBK.add(delMemberF, text='Remove Member', padding=47)
    memberNBK.grid(row=2, column=0, columnspan=4, sticky=(W))

    # add member frame.
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
    # add and go back button.
    Button(addMemberF, text="Add", command=addMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=7, column=2, padx=20, pady=20)
    Button(addMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=8, column=2, sticky=(E), padx=15, pady=10)

    # modify member frame.
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
    # modify and go back button.
    Button(modMemberF, text="Modify", command=modMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=7, column=2, padx=20, pady=20)
    Button(modMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=8, column=2, sticky=(E), padx=15, pady=10)

    # delete member frame.
    delMemberID = StringVar()
    Label(delMemberF, text="             Customer ID:", bg="#FFFFFF", font = ("Berlin Sans FB", 12)).grid(row=3, column=0, padx=10, pady=10)
    delMemberIDE = Entry(delMemberF, textvariable=delMemberID, width=40, font = ("Berlin Sans FB", 12), bd=2)
    delMemberIDE.grid(row=3, column=1, padx=10, pady=10)
    # remove and go back button.
    Button(delMemberF, text="Remove", command=delMember, cursor="hand2", width=17, font = ("Berlin Sans FB", 12)).grid(row=4, column=2, padx=20, pady=20)
    Button(delMemberF, text = "Go Back", width = 10, pady=2, font = ("Berlin Sans FB", 12), cursor="hand2", command=homeAdmin).grid(row=5, column=2, sticky=(E), padx=15, pady=10)

    root.mainloop()


# main.
# root definition and configuration.
root = Tk()
root.title("Bookstore Management System")
root.geometry('960x540')
root.iconbitmap(r"images\bms.ico")
root.attributes("-alpha", 0.95)
root.wm_protocol("WM_DELETE_WINDOW", goodBye)
root.resizable(FALSE,FALSE)

# mainframe definition and configuration.
sty = ttk.Style()
sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief=FLAT)
mainframe = ttk.Frame(root, style="Bookstore.TFrame")
mainframe.grid(column=0, row=0)

# background image.
bgtitle = PhotoImage(file=r"images\welcometitle.png")
Label(mainframe, image = bgtitle, bg="#FFFFFF").grid(row=0, column=0, columnspan=8)
bgimage = PhotoImage(file=r"images\welcomecloud.png")
Label(mainframe, image = bgimage, bg="#FFFFFF").grid(row=0, column=8, rowspan=6)

# login mode buttons.
Label(mainframe, text = "Login As", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e").grid(row=1, column=0, sticky=(W), padx = 15)
Button(mainframe, text = "Admin", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asAdmin).grid(row=2, column=0, pady = 5)
Button(mainframe, text = "Customer", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asCustomer).grid(row=3, column=0, pady = 5)

root.mainloop()
mycon.close()
