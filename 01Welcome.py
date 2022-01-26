from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def goodBye():
    messagebox.showinfo(message="Thank You for Using BMS", title="Bookstore Manager")
    root.quit()

def asAdmin():
    return

def asCustomer():
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
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

framebg1 = PhotoImage(file=r"BookstoreMS\welcometitle.png")
bglabel1 = Label(mainframe, image = framebg1, bg="#FFFFFF")

framebg2 = PhotoImage(file=r"BookstoreMS\welcomecloud.png")
bglabel2 = Label(mainframe, image = framebg2, bg="#FFFFFF")

login = Label(mainframe, text = "Login As     ", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e")

logAdmin = Button(mainframe, text = "Admin", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief="groove", command = asAdmin)
logCustomer = Button(mainframe, text = "Customer", pady = 5, width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief="groove", command = asCustomer)

bglabel1.grid(row=0, column=0, columnspan=8)
bglabel2.grid(row=0, column=8, rowspan=6)
login.grid(row=1, column=0)
logAdmin.grid(row=2, column=0)
logCustomer.grid(row=3, column=0)

root.mainloop()
