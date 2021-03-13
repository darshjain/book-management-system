from tkinter import *
from tkinter import messagebox
from database import DB as dbh

db=dbh()
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


def update_command():
    db.update(selected_tuple[0], title_text.get(), author_text.get())


window = Tk()

window.title("My Books")


def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)

lbl_title = Label(window, text="Title")

lbl_author = Label(window, text="Author")

lbl_isbn = Label(window, text="ISBN")

title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)

lbl_title.grid(row=0, column=0)
entry_title.grid(row=0, column=1)
lbl_isbn.grid(row=1, column=0)
entry_isbn.grid(row=1, column=1)
lbl_author.grid(row=2, column=0)
entry_author.grid(row=2, column=1)

list_space = Listbox(window, height=25, width=65)
list_space.grid(row=3, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=2, rowspan=6)

list_space.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_space.yview)

list_space.bind('<<ListboxSelect>>', get_selected_row)

btn_view = Button(window, text="View all", width=12, command=view_command)
btn_view.grid(row=2, column=3)

btn_search = Button(window, text="Search entry",
                    width=12, command=search_command)
btn_search.grid(row=3, column=3)

btn_add = Button(window, text="Add entry", width=12, command=add_command)
btn_add.grid(row=4, column=3)

btn_update = Button(window, text="Update selected",
                    width=12, command=update_command)
btn_update.grid(row=5, column=3)

btn_delete = Button(window, text="Delete selected",
                    width=12, command=delete_command)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text="Close", width=12, command=window.destroy)
btn_close.grid(row=7, column=3)

window.mainloop()
