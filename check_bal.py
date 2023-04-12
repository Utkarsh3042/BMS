import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
#import main

def checkbal(left_frame,usname,accno,pin):
    if len(accno) == 0:
        tkinter.messagebox.askretrycancel("","ENTER ACCOUNT NUMBER!")
    elif len(pin) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PIN!")
    else:
        db_usname = usname+".db"
        try:
            sqlcon = sqlite3.connect(db_usname)
            cursor = sqlcon.cursor()
            query = '''SELECT AMNT FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
            cursor.execute(query)
            data = cursor.fetchall() #in the form of tuple inside list
            tup_data = data[0] #list to tuples
            int_data = tup_data[0] #tuples to int
            # print("")
            # print("AVAILABLE BALANCE :₹{}".format(int_data))
            for widgets in left_frame.winfo_children():   #to delete old widgets
                widgets.destroy()
            lbl_amp = Label(left_frame,text="CHECK BALANCE PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
            lbl_amp.place(relx=0.5,y=50,anchor=CENTER)
            lbl_accno = Label(left_frame,text="AVAILABLE BALANCE:  ₹:",bg='#d9d9d9',font=("Arial",20,"bold"))
            lbl_accno.place(x=130,y=140)
            lbl_data = Label(left_frame,text=int_data,bg='#d9d9d9',font=("Arial",20,))
            lbl_data.place(x=500,y=140)
            #text to word converter
            #time.sleep(3)
            cursor.close()
            sqlcon.close()
            back_btn = Button(left_frame,text="BACK",height=3,width=14, font=("Arial",16,"bold"),command=lambda: checkbal_page(left_frame, usname))
            back_btn.place(x=350,y=550)
            #main.front(usname)
        except:
            tkinter.messagebox.showinfo("NOT FOUND","ACCOUNT NOT FOUND")
            checkbal_page(left_frame, usname)
            #print(error)
 
def checkbal_page(left_frame,usname):
    for widgets in left_frame.winfo_children():   #to delete old widgets
        widgets.destroy()
    lbl_amp = Label(left_frame,text="CHECK BALANCE PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_amp.place(relx=0.5,y=50,anchor=CENTER)
    lbl_accno = Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_accno.place(x=130,y=140)
    accno = Entry(left_frame,width=25,font=("Arial",18))
    accno.place(x=370,y=140)
    lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_pin.place(x=130,y=200)
    pin = Entry(left_frame,width=12,show="*",font=("Arial",18))
    pin.place(x=370,y=200)
    submit_btn = Button(left_frame,text="CHECK",height=3,width=14, font=("Arial",16,"bold"),command=lambda: checkbal(left_frame,usname,accno.get(),pin.get()))
    submit_btn.place(x=350,y=550)
