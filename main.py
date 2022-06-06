################################################################################
# Importing tkinter and Pillow libraries used for the GUI                      #
# Importing oracledb for the SQL CRUD Operations                               #
# Importing OS for operating system operations making it more cross - platform #
################################################################################

# add error check for lenghths of text fields implement on both input text fields (if statements), create unit tests, insert data to DB, create button functions, check if i can add loops, db initliazing and db creating if statements

from ctypes.wintypes import SIZE
from curses import window
from re import M, S
import tkinter as tk
from tkinter import E, N, W, ttk
import tkinter
from PIL import Image, ImageTk
import sqlite3
import os

from oracledb import Cursor
################################################################################
#                                                                              #
# Main GUI Windows definition                                                  #
################################################################################
root = tk.Tk()
root.title("Skynet")
root.geometry('1025x1255+400+5')
#canvas = tk.Canvas(root, width=600, height=600)
#canvas.grid(columnspan=3, rowspan=3)
#root.configure(bg='white')

#DB
with sqlite3.connect("database.db") as db:
    cursor_visitor = db.cursor()
    cursor_subcontracting_company = db.cursor()
    cursor_employee  = db.cursor()

cursor_visitor.execute(""" CREATE TABLE IF NOT EXISTS visitor(visitor_id integer PRIMARY KEY AUTOINCREMENT, visitor_name text NOT NULL, visit_date Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, company_name text, FOREIGN KEY(company_name) REFERENCES subcontracting_company(company_name));""")

cursor_subcontracting_company.execute(""" CREATE TABLE IF NOT EXISTS subcontracting_company(company_name text PRIMARY KEY, department_contractors text NOT NULL, FOREIGN KEY(department_contractors) REFERENCES employee(department_employee));""")

cursor_employee.execute(""" CREATE TABLE IF NOT EXISTS employee(employee_ID integer PRIMARY KEY AUTOINCREMENT, employee_name text NOT NULL, department_employee text NOT NULL);""")

################################################################################
#                                                                              #
# Logo Create                                                                  #
#################################################################################                                                                     
logo_welcome = Image.open("logo_welcome.png")                                               
logo_welcome = ImageTk.PhotoImage(logo_welcome)                                               
logo_label_welcome = tk.Label(image=logo_welcome)                                             
logo_label_welcome.image = logo_welcome                                                      
logo_label_welcome.grid(column=1, row=0)  

logo1 = Image.open("logo_create.png")                                               
logo1 = ImageTk.PhotoImage(logo1)                                               
logo_label1 = tk.Label(image=logo1)                                             
logo_label1.image = logo1                                                       
logo_label1.grid(column=0, row=0, sticky=W)                                             

logo2 = Image.open("logo_read.png")                                               
logo2 = ImageTk.PhotoImage(logo2)                                               
logo_label2 = tk.Label(image=logo2)                                             
logo_label2.image = logo2                                                      
logo_label2.grid(column=0, row=4,sticky=W)          

logo3 = Image.open("logo_update.png")                                               
logo3 = ImageTk.PhotoImage(logo3)                                               
logo_label3 = tk.Label(image=logo3)                                             
logo_label3.image = logo3                                                      
logo_label3.grid(column=0, row=7,sticky=W)   

logo4 = Image.open("logo_delete.png")                                             
logo4 = ImageTk.PhotoImage(logo4)                                               
logo_label4 = tk.Label(image=logo4)                                             
logo_label4.image = logo4                                                      
logo_label4.grid(column=0, row=11,sticky=W) 

# sample data untill sql connection
employee_list=("Mike", "John")
company_list=("Tesla", "Yamaha")
    

#text field defs
create_visitor_name_input = tkinter.Entry(root)
create_visitor_name_input.grid(column=1, row=1)

create_emp_name_dropdown_txt = tkinter.StringVar()
create_emp_name_dropdown_txt.set("Select Employee Name")
create_emp_name_dropdown = tkinter.OptionMenu(root, create_emp_name_dropdown_txt, *employee_list)
create_emp_name_dropdown.grid(column=1, row=2)

create_company_name_dropdown_txt = tkinter.StringVar()
create_company_name_dropdown_txt.set("Select Company Name")
create_company_name_dropdown = tkinter.OptionMenu(root, create_company_name_dropdown_txt, *company_list)
create_company_name_dropdown.grid(column=1, row=3)

read_visitor_output_text = tkinter.StringVar()
read_visitor_output_text = set("Visits of all representatives from selected company")
read_visitor_output = tkinter.Text(root, height=5)
read_visitor_output.grid(column=1, row=6)

query_company_name_dropdown_txt = tkinter.StringVar()
query_company_name_dropdown_txt.set("Select Company Name")
query_company_name_dropdown = tkinter.OptionMenu(root, query_company_name_dropdown_txt, *company_list)
query_company_name_dropdown.grid(column=1, row=5)


update_company_name_dropdown_txt = tkinter.StringVar()
update_company_name_dropdown_txt.set("Select Company Name")
update_company_name_dropdown = tkinter.OptionMenu(root, update_company_name_dropdown_txt, *company_list)
update_company_name_dropdown.grid(column=1, row=9)

update_company_name_input = tkinter.Entry(root)
update_company_name_input.grid(column=1, row=10)

#button defs

create_button_text = tk.StringVar()
create_button = tk.Button(root, textvariable=create_button_text, font="Railway", height=3, width=10)
create_button_text.set("Add record")
create_button.grid(column=3, row=2,)

read_button_text = tk.StringVar()
read_button = tk.Button(root, textvariable=read_button_text, font="Railway", height=3, width=10)
read_button_text.set("Query record")
read_button.grid(column=3, row=5)

update_button_text = tk.StringVar()
update_button = tk.Button(root, textvariable=update_button_text, font="Railway", height=3, width=10)
update_button_text.set("Update record")
update_button.grid(column=3, row=10)

delete_button_text = tk.StringVar()
delete_button = tk.Button(root, textvariable=delete_button_text, font="Railway", height=3, width=10)
delete_button_text.set("Delete record")
delete_button.grid(column=3, row=12)

# Labels Create Record

create_vis_name = tk.Label(root, text="Please input visitor name", font="Raleway")
create_vis_name.grid(columnspan=1, column=0, row=1, sticky=W)

create_emp_name = tk.Label(root, text="Please select employee name", font="Raleway")
create_emp_name.grid(columnspan=1, column=0, row=2, sticky=W)

create_comp_name = tk.Label(root, text="Please select company name", font="Raleway")
create_comp_name.grid(columnspan=1, column=0, row=3,sticky=W)

# Labels Read Record

read_comp_name = tk.Label(root, text="Please select company name to query", font="Raleway")
read_comp_name.grid(columnspan=1, column=0, row=5, sticky=W)

# Labels Update Record

update_comp_name = tk.Label(root, text="Please select company to rename", font="Raleway")
update_comp_name.grid(columnspan=1, column=0, row=9, sticky=W)

update_comp_name_new = tk.Label(root, text="Please type the new name", font="Raleway")
update_comp_name_new.grid(columnspan=1, column=0, row=10, sticky=W)

# Labels Delete Record

delete_last_visitor = tk.Label(root, text="This button deletes the last visitor", font="Raleway")
delete_last_visitor.grid(columnspan=1, column=0, row=12, sticky=W)

root.mainloop()