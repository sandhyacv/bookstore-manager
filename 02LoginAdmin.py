from tkinter import *
from tkinter import messagebox

def goodBye():
    messagebox.showinfo(message="Thank You for Using BMS", title="Bookstore Manager")
    root.quit()

def getUsername():
    return

def getPassword():
    return

def homeAdmin():
    return

root = Tk()
root.title("Bookstore Management System")
root.geometry('960x540')
root.iconbitmap(r"BookstoreMS\bms.ico")
root.attributes("-alpha", 0.95)
root.wm_protocol("WM_DELETE_WINDOW", goodBye)
root.resizable(FALSE,FALSE)

mainframe = Frame(root, bg="#FFFFFF")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

titleImg = PhotoImage(file = r"BookstoreMS\titlestrip.png").subsample(2,2)
titleLbl = Label(mainframe, image = titleImg, bg="#FFFFFF")

loginTxt = Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170")

user = StringVar()
userEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=user, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
userEntry.insert(0, " Enter Username")

pswd = StringVar()
pswdEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswd, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
pswdEntry.insert(0, " Enter Password")

space = Label(mainframe, text = " ", height=2, bg="#ffffff")
loginBut = Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief="groove", command = homeAdmin)

titleLbl.grid(row=0, column=0)

loginTxt.grid(row=2, column=0, pady=30)
userEntry.grid(row=4, column=0, ipady=10, pady=10)
pswdEntry.grid(row=6, column=0, ipady=10, pady=10)
space.grid(row=7, column=0)
loginBut.grid(row=8, column=0, pady=10)

root.mainloop()