from tkinter import *
from tkinter import ttk, messagebox

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    root.quit()

def adminLogin(event=None):
    if userEntry.get() == "admin":
        if pswdEntry.get() == "123":
            homeAdmin()
    return

def homeAdmin():
    messagebox.showinfo(message="Successfully Logged In", title="Bookstore Manager")
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
Label(mainframe, image = titleImg, bg="#FFFFFF").grid(row=0, column=0)

Label(mainframe, text = "LOGIN", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e5170").grid(row=2, column=0, pady=30)

user = StringVar()
userEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=user, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
userEntry.insert(0, " Enter Username")
userEntry.grid(row=4, column=0, ipady=10, pady=10)

pswd = StringVar()
pswdEntry = Entry(mainframe, width=40, font=("Berlin Sans FB", 14), textvariable=pswd, fg="#2e2e2e", bg="#FFFFFF", borderwidth=1)
pswdEntry.insert(0, " Enter Password")
pswdEntry.grid(row=6, column=0, ipady=10, pady=10)

Label(mainframe, text = " ", height=2, bg="#ffffff").grid(row=7, column=0)
Button(mainframe, text = "Login", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 14), bd=2, cursor="hand2", relief=GROOVE, command = adminLogin).grid(row=8, column=0, pady=10)
root.bind("<Return>", adminLogin)

root.mainloop()
