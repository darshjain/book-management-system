from tkinter import *
from tkinter import messagebox
from database import DB as dbh
from PIL import ImageTk, Image
db = dbh()
selected_tuple = []


def get_selected_row(event):
    global selected_tuple
    index = list_space.curselection()[0]
    selected_tuple = list_space.get(index)
    entry_title.delete(0, END)
    entry_title.insert(END, selected_tuple[1])
    entry_author.delete(0, END)
    entry_author.insert(END, selected_tuple[2])
    entry_isbn.delete(0, END)
    entry_isbn.insert(END, selected_tuple[3])


def view_command():
    list_space.delete(0, END)
    for row in db.view():
        list_space.insert(END, row)


def search_command():
    list_space.delete(0, END)
    for row in db.search(title_text.get(), author_text.get()):
        list_space.insert(END, row)


def add_command():
    db.insert(title_text.get(), author_text.get(),
              isbn_text.get())
    list_space.delete(0, END)

    list_space.insert(
        END, (title_text.get(), author_text.get(), isbn_text.get()))


def delete_command():
    db.delete(selected_tuple[0])
    view_command()


def update_command():
    db.update(selected_tuple[0], title_text.get(), author_text.get())


def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd
# def customer():
#     global selected_tuple,customercontact,customername,customerid
#     db.customer_add(customerid.get(),customername.get(),customercontact.get())
    # sell.new_window.destroy()

def sell():
    # global selected_tuple,customercontact,customername,customerid
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
    
    x=lambda :db.customer_add(entry_customerid.get(),entry_customername.get(),entry_customercontact.get())

    btn_customeradd=Button(new_window,text="ADD CUSTOMER",bg="floral white",command=x)
    btn_customeradd.grid(row=4,column=0)

    lbl_custname.grid(row=1,column=0)
    lbl_custnum.grid(row=2,column=0)
    lbl_custcont.grid(row=3,column=0)

    entry_customername.grid(row=1,column=1)
    entry_customerid.grid(row=2,column=1)
    entry_customercontact.grid(row=3,column=1)

    new_window.mainloop()

window = Tk()

window.title("My Books")
# ================== CHANGES HERE START========================
canv = Canvas(window, width=700, height=700, bg='white')
canv.place(relx=0, rely=0, anchor=NW)
img = Image.open("lib3.png")
img = img.resize((700, 700), Image.ANTIALIAS)  # PIL solution
img_save = ImageTk.PhotoImage(img)
canv.create_image(0, 0, anchor=NW, image=img_save)
# ================== CHANGES HERE END ========================
window.geometry("700x700")  # window size

window.protocol("WM_DELETE_WINDOW", on_closing)

lb2 = Label(window, text="Book Management System",
            font=("Courier", 20, "italic"), fg="Black")


lbl_title = Label(window, text="Title")
lbl_author = Label(window, text="Author")
lbl_isbn = Label(window, text="ISBN")


title_text = StringVar()
entry_title = Entry(window, textvariable=title_text, bg="floral white")

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text, bg="floral white")

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text, bg="floral white")


lb2.grid(row=1, column=2, pady=30, padx=50, columnspan=4)

lbl_title.grid(row=4, column=1, padx=50)
entry_title.grid(row=4, column=2)
lbl_isbn.grid(row=5, column=1, padx=50)
entry_isbn.grid(row=5, column=2)
lbl_author.grid(row=6, column=1, padx=50)
entry_author.grid(row=6, column=2)


list_space = Listbox(window, height=25, width=65, bg="floral white")
list_space.grid(row=8, column=1, rowspan=8, columnspan=2, padx=50, pady=40)

scrollbar = Scrollbar(window)
scrollbar.grid(row=8, column=3, rowspan=6, padx=20)

list_space.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_space.yview)

list_space.bind('<<ListboxSelect>>', get_selected_row)

btn_view = Button(window, text="View all", width=12,
                  command=view_command, bg="lavenderBlush2")
btn_view.grid(row=9, column=4, padx=0)

btn_search = Button(window, text="Search entry", width=12,
                    command=search_command, bg="lavenderBlush2")
btn_search.grid(row=10, column=4, padx=0)

btn_add = Button(window, text="Add entry", width=12,
                 command=add_command, bg="lavenderBlush2")
btn_add.grid(row=11, column=4, padx=0)

btn_update = Button(window, text="Update selected", width=12,
                    command=update_command, bg="lavenderBlush2")
btn_update.grid(row=12, column=4, padx=0)

btn_delete = Button(window, text="Delete selected", width=12,
                    command=delete_command, bg="lavenderBlush2")
btn_delete.grid(row=13, column=4, padx=0)


btn_sell = Button(window, text="Sell Selected", width=12,
                  bg="lavenderBlush2",command=sell)
btn_sell.grid(row=14, column=4, padx=0)

btn_viewsale = Button(window, text="View Sales",
                      width=12, bg="lavenderBlush2")
btn_viewsale.grid(row=15, column=4, padx=0)


btn_close = Button(window, text="Close", width=12,
                   command=window.destroy, bg="lavenderBlush2")
btn_close.grid(row=16, column=4)

window.mainloop()
