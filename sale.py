from tkinter import *
from tkinter import messagebox
from database import DB as dbh
from PIL import ImageTk, Image
db = dbh()
# selected_tuple = []
def customer():
    db.customer_add(customerid.get(),customername.get(),customercontact.get())
    new_window.destroy()

def sell():
    new_window=Tk()
    new_window.title("SELL THE BOOK")
    new_window.geometry("700x700")
    book_sell=selected_tuple[0]
    print(book_sell,"Sell")


    lbl_custname = Label(new_window, text="Name Of Customer")
    lbl_custnum = Label(new_window, text="ID of Customer")
    lbl_custcont = Label(new_window, text="Contact of Customer")

    customername = StringVar()
    entry_customername = Entry(new_window, textvariable=customername, bg="floral white")

    customerid = StringVar()
    entry_customerid = Entry(new_window, textvariable=customerid, bg="floral white")

    customercontact = StringVar()
    entry_customercontact = Entry(new_window, textvariable=customercontact, bg="floral white")

    btn_customeradd=Button(new_window,text="ADD CUSTOMER",bg="floral white",command=customer)
    btn_customeradd.grid(row=4,column=0)

    lbl_custname.grid(row=1,column=0)
    lbl_custnum.grid(row=2,column=0)
    lbl_custcont.grid(row=3,column=0)

    entry_customername.grid(row=1,column=1)
    entry_customerid.grid(row=2,column=1)
    entry_customercontact.grid(row=3,column=1)

    new_window.mainloop()