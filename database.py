import sqlite3
from tkinter import *
from tkinter import messagebox


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("mybooks.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)",
                         (title, author, isbn,))
        self.conn.commit()
        self.view()

    def update(self, id, title, author):
        self.cur.execute(
            "UPDATE book SET title=?, author=? WHERE id=?", (title, author, id,))
        self.conn.commit()
        self.view()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    def search(self, title="", author=""):
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=?", (title, author))
        rows = self.cur.fetchall()
        return rows

    def customer_add(self, customerid, customername, customercontact):
        print(customercontact)
        print(customername)
        self.cur.execute("INSERT INTO customer VALUES (NULL,?,?)",(customername, customercontact))
        self.conn.commit()
        
    def sell(self, bookid, customerid, date, price):
        print("SELL FUNCTION")
        self.cur.execute("INSERT INTO sale VALUES (NULL,?,?,?,?)",(bookid,customerid,date,price))
        self.conn.commit()
        self.view()

    def viewsales(self, issueid, bookid, customerid, date, price):
        print("view sales")
        self.conn.commit()
        self.view()
