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

def bookProcured():
    return

def bookReserved():
    return

def CheckOut():
    return

def editBook():
    return

def editMember():
    return

def searchBox(evt):
    searchCtg.selection_clear()
    searchCtg.current()
    searchCtg.get()
    return

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
