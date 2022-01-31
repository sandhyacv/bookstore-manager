from tkinter import *
from tkinter import ttk, messagebox

def goodBye():
    messagebox.showinfo("Bookstore Manager", "Thank You for Using BMS")
    root.quit()

def asAdmin():
    return

def asCustomer():
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
mainframe.grid(column=0, row=0)

bgtitle = PhotoImage(file=r"images\welcometitle.png")
Label(mainframe, image = bgtitle, bg="#FFFFFF").grid(row=0, column=0, columnspan=8)

bgimage = PhotoImage(file=r"images\welcomecloud.png")
Label(mainframe, image = bgimage, bg="#FFFFFF").grid(row=0, column=8, rowspan=6)

Label(mainframe, text = "Login As", font = ("Berlin Sans FB", 24), bg="#FFFFFF", fg="#2e2e2e").grid(row=1, column=0, sticky=(W), padx = 15)
Button(mainframe, text = "Admin", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asAdmin).grid(row=2, column=0, pady = 5)
Button(mainframe, text = "Customer", width = 20, bg="#2e2e2e", fg="#FFFFFF", font = ("Berlin Sans FB", 10), bd=2, cursor="hand2", relief=GROOVE, command = asCustomer).grid(row=3, column=0, pady = 5)

root.mainloop()