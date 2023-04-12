import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def remacc(left_frame,usname,accno,pin,cnfrm):
    if len(accno) == 0:
        tkinter.messagebox.askretrycancel("","ENTER ACCOUNT NUMBER!")
    elif len(pin) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PIN!")
    elif cnfrm != "CONFIRM":
        tkinter.messagebox.askretrycancel("","PLEASE CONFIRM AUTHORIZATION!")
    else:
        db_usname = usname+".db"
        try:
            sqlcon = sqlite3.connect(db_usname)
            cursor = sqlcon.cursor()
            query1 = '''SELECT AMNT FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
            cursor.execute(query1)
            data = cursor.fetchall() #in the form of tuple inside list
            tup_data = data[0] #list to tuples
            amnt = tup_data[0] #tuple to int
            auth = tkinter.messagebox.askquestion("REMOVE?","ARE YOU SURE TO REMOVE YOUR ACCOUNT?")
            if auth == 'yes':
                try:
                    query2 = '''DELETE FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
                    cursor.execute(query2)
                    sqlcon.commit()
                    # print("")
                    # print("ACCOUNT REMOVED SUCCESSFULLY!")
                    # print("AMOUNT WITHDRAWN :₹",amnt)
                    for widgets in left_frame.winfo_children():   #to delete old widgets
                        widgets.destroy()
                    lbl_amp = Label(left_frame,text="ACCOUNT REMOVED SUCCESSFULLY!",bg='#d9d9d9',font=("Arial",32,"bold"))
                    lbl_amp.place(relx=0.5,y=50,anchor=CENTER)
                    lbl_accno = Label(left_frame,text="WITHDRAWN BALANCE:  ₹:",bg='#d9d9d9',font=("Arial",20,"bold"))
                    lbl_accno.place(x=130,y=140)
                    lbl_data = Label(left_frame,text=amnt,bg='#d9d9d9',font=("Arial",20,))
                    lbl_data.place(x=500,y=140)
                    #text to word converter
                    #time.sleep(3)
                    cursor.close()
                    sqlcon.close()
                    back_btn = Button(left_frame,text="BACK",height=3,width=14, font=("Arial",16,"bold"),command=lambda: remacc_page(left_frame, usname))
                    back_btn.place(x=350,y=550)
                    #time.sleep(3)
                except:
                    tkinter.messagebox.showerror("ERROR","SOMETHING WENT WRONG, TRY AGAIN?")
                    remacc_page(left_frame, usname)
                    #print(error)
            else:
                remacc_page(left_frame, usname)
        except:
            # print(error)
            tkinter.messagebox.showinfo("NOT FOUND","NO ACCOUNT FOUND!")
            remacc_page(left_frame, usname)


def remacc_page(left_frame,usname):
    for widgets in left_frame.winfo_children():   #to delete old widgets
        widgets.destroy()
    lbl_rem = Label(left_frame,text="REMOVE ACCOUNT PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_rem.place(relx=0.5,y=50,anchor=CENTER)
    lbl_accno = Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_accno.place(x=130,y=140)
    accno = Entry(left_frame,width=25,font=("Arial",18))
    accno.place(x=370,y=140)
    lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_pin.place(x=130,y=200)
    pin = Entry(left_frame,width=12,show="*",font=("Arial",18))
    pin.place(x=370,y=200)
    lbl_cnf = Label(left_frame,text="TYPE 'CONFIRM' :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_cnf.place(x=130,y=260)
    cnfrm = Entry(left_frame,width=10,font=("Arial",18))
    cnfrm.place(x=370,y=260)
    submit_btn = Button(left_frame,text="REMOVE",height=3,width=14, font=("Arial",16,"bold"),command=lambda:remacc(left_frame, usname, accno.get(), pin.get(), cnfrm.get()))
    submit_btn.place(x=350,y=550)
