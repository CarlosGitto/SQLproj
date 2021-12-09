import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter.constants import CENTER
from tkinter.font import names
from typing import Text
import tables
from myengine import engine
from sqlalchemy.sql.expression import table
import mf


class Gui:
    def __init__(self, window):
        self.window = window
        self.window.title("DB Administrator")
       
        def get_table():
            table = self.combo.get()
            return mf.string_to_class(table)

        def call_select(event):
            records = self.tree.get_children()
            for record in records:
                self.tree.delete(record)

            table = get_table()
            s = mf.select(table)
            for i,row in enumerate(s):
                self.tree.insert("",tk.END, text = row[0], values = row[1:])

        def validation():
            return True 
        
        def call_newpay():
            if validation():
                table = get_table()
                mf.new_pay(table, self.name.get(), self.cost.get(), self.email.get())
            else :
                print("error :)")

        # Creating a frame Container
        frame = tk.LabelFrame(self.window, text = "Ingresar nuevo registro")
        frame.grid(row=0, column=0, columnspan=4, pady=20)

        #WHO input
        tk.Label(frame, text= "Who?: ").grid(row=1, column=0)
        self.name = tk.Entry(frame)
        self.name.grid(row=1,column=1)

        #email input
        tk.Label(frame, text= "email: ").grid(row=1, column=2)
        self.email = tk.Entry(frame)
        self.email.grid(row=1,column=3)

        #Cost input
        tk.Label(frame, text= "Cost: $").grid(row=2, column=0)
        self.cost = tk.Entry(frame)
        self.cost.grid(row=2,column=1)

        #Submmit button
        ttk.Button(frame, text="Agregar pago", command=call_newpay).grid(row=4, column=0,columnspan=4 , sticky= "WE")

        #combo
        values = ["Luz", "Agua", "Gas", "Internet"]
        self.combo = ttk.Combobox(frame, values=values, state="readonly")
        self.combo.grid(row=3, column=1)
        self.combo.current(0)
        tk.Button(frame, text = "-",).grid(row = 3, column=0)
        
        

        #event -> combo value change
        self.combolabel = tk.Label(text=self.combo.bind("<<ComboboxSelected>>",  call_select))
        self.combolabel.grid(row=4, column=0)
        
        #TABLE
        self.tree = ttk.Treeview(height= 10, columns=(1,2,3,4))
        self.tree.grid(row=5, column=0, columnspan=1)
        self.tree.heading("#0", text="Id")
        self.tree.heading("#1", text="Cost")
        self.tree.heading("#2", text="State")
        self.tree.heading("#3", text="Date")
        self.tree.heading("#4", text="Recibt")

        
        def show_table():
            #clean table
            
            
            
            return
if __name__ == "__main__":
    tables.Base.metadata.create_all(bind=engine)        
    window = tk.Tk()
    application = Gui(window)
    
    window.mainloop()









def get_txt():
    submitted_txt = txt_box1.get() +" "+ txt_box2.get() +" "+ txt_box3.get()
    label1["text"] = submitted_txt



