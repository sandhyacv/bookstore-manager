from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def welcomePage():
    return

def goodBye():
    messagebox.showinfo(message="Thank You for Using BMS", title="Bookstore Manager")
    root.quit()

def loggedOut():
    messagebox.showinfo(message="Thank You for Using BMS", title="Bookstore Manager")
    welcomePage()

def searchBox(evt):
    searchCtg.selection_clear()
    searchCtg.current()
    searchCtg.get()
    return

root = Tk()
root.title("Bookstore Management System")
root.geometry('960x540')
root.iconbitmap(r"BookstoreMS\bms.ico")
root.attributes("-alpha", 0.95)
root.wm_protocol("WM_DELETE_WINDOW", goodBye)
root.resizable(FALSE,FALSE)

sty = ttk.Style()
sty.configure("Bookstore.TFrame", background="#FFFFFF", borderwidth=5, relief="flat")

mainframe = ttk.Frame(root, style="Bookstore.TFrame")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

titleImg = PhotoImage(file = r"BookstoreMS\titlestrip.png").subsample(2,2)
titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")
logoutBut = Button(mainframe, text = "LOGOUT", width = 12, bg = "#41404A", fg = "#FFFFFF", font = ("Berlin Sans FB", 14), relief = "flat", command = loggedOut)

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

clearBut = Button(mainframe, text = "Clear", width = 15, bg="#9e9e9e", fg="#2e5170", font = ("Berlin Sans FB", 14), cursor="hand2", relief="groove", command = lambda: searchEntry.delete(0, END))

titleLbl.grid(row=0, column=0, columnspan=2, rowspan=2)
logoutBut.grid(row=1, column=1, sticky=(E), padx=45)
searchCtg.grid(row=2, column=0, ipadx=4, ipady=3)
searchEntry.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)
clearBut.grid(row=3, column=1, sticky=(E), padx=28)

root.mainloop()