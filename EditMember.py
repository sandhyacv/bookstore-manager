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

def addMember():
    # clear all entries after adding
    return

def modMember():
    # clear all entries after modifying
    return

def delMember():
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
