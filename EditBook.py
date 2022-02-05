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

def addBook():
    # clear all entries after adding
    return

def modBook():
    # clear all entries after modifying
    return

def delBook():
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