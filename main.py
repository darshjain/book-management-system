from tkinter import *
from tkinter import messagebox
from database import DB as dbh

db = dbh()
selected_tuple=[]

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


window = Tk()

window.title("My Books")
bg = PhotoImage(file = "lib3.png")
window.configure(background="cornsilk2") #background color
window.geometry("600x600") #window size

def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)

lb1 = Label(window,text="  ", font=("Courier", 16, "italic"),bg= "Cornsilk2", fg="Black")
lb2 = Label(window,text="Book Management System", font=("Courier", 20, "italic"),bg= "Cornsilk2", fg="Black")
lb3 = Label(window,text="", font=("Courier", 16, "italic"),bg= "Cornsilk2", fg="Black")
lb4 = Label(window,text="", font=("Courier", 16, "italic"),bg= "Cornsilk2", fg="Black")
#heading

lbl_title = Label(window, text="Title" ,bg = "cornsilk2")
lbl_author = Label(window, text="Author", bg="cornsilk2")
lbl_isbn = Label(window, text="ISBN", bg="cornsilk2")

lb5 = Label(window,text="", font=("Courier", 15, "italic"),bg= "Cornsilk2", fg="Black")
#Space

title_text = StringVar()
entry_title = Entry(window, textvariable=title_text , bg="floral white")

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text, bg="floral white")

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text, bg="floral white")

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=2)
lb3.grid(row=2,column=0)
#lb4.grid(row=3,column=0)

lbl_title.grid(row=4, column=1)
entry_title.grid(row=4, column=2)
lbl_isbn.grid(row=5, column=1)
entry_isbn.grid(row=5, column=2)
lbl_author.grid(row=6, column=1)
entry_author.grid(row=6, column=2)

lb5.grid(row=7,column=1)

list_space = Listbox(window, height=25, width=65, bg="floral white")
list_space.grid(row=8, column=1, rowspan=8, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=8, column=3, rowspan=6)

list_space.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_space.yview)

list_space.bind('<<ListboxSelect>>', get_selected_row)

btn_view = Button(window, text="View all", width=12, command=view_command, bg="lavenderBlush2")
btn_view.grid(row=9, column=4)

btn_search = Button(window, text="Search entry",width=12, command=search_command, bg="lavenderBlush2")
btn_search.grid(row=10, column=4)

btn_add = Button(window, text="Add entry", width=12, command=add_command, bg="lavenderBlush2")
btn_add.grid(row=11, column=4)

btn_update = Button(window, text="Update selected",width=12, command=update_command,bg="lavenderBlush2")
btn_update.grid(row=12, column=4)

btn_delete = Button(window, text="Delete selected", width=12, command=delete_command, bg="lavenderBlush2")
btn_delete.grid(row=13, column=4)

btn_close = Button(window, text="Close", width=12, command=window.destroy, bg="lavenderBlush2")
btn_close.grid(row=14, column=4)

window.mainloop()
