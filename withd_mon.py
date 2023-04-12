import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def withdraw(left_frame,usname,accno,amnt,pin):
    #print("HI")
    if len(accno) == 0:
        tkinter.messagebox.askretrycancel("","ENTER ACCOUNT NUMBER!")
    elif len(amnt) == 0:
        tkinter.messagebox.askretrycancel("","ENTER AMOUNT!")
    elif len(pin) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PIN!")
    else:
        amnt = int(amnt)
        db_usname = usname+".db"
        try:
            sqlcon = sqlite3.connect(db_usname)
            cursor = sqlcon.cursor()
            query = '''SELECT AMNT FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
            cursor.execute(query)
            data = cursor.fetchall() #in the form of tuple inside list
            tup_data = data[0] #list to tuples
            amnt_db = tup_data[0] #tuples to int
            if(amnt_db>=amnt):
                new_amnt = amnt_db-amnt
                try:
                    query2 = '''UPDATE BMS SET AMNT = {} WHERE ACCNO = {} AND PIN = {};'''.format(new_amnt,accno,pin)
                    cursor.execute(query2)
                    sqlcon.commit()
                    show_bal = tkinter.messagebox.askquestion("WITHDRAWN","AMOUNT WITHDRAWN SUCCESSFULLY, WANT TO SHOW BALANCE?")
                    #print("")
                    #print("ACCOUNT UPDATED")
                    #display_amnt = str(input("WANT TO SHOW THE BALANCE? (Y/N) :"))
                    if show_bal == 'yes':
                        query3 = '''SELECT AMNT FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
                        cursor.execute(query3)
                        data = cursor.fetchall() #in the form of tuple inside list
                        tup_data = data[0] #list to tuples
                        int_data = tup_data[0] #tuples to int
                        #print("")
                        #print("AVAILABLE BALANCE :₹{}".format(int_data))
                        for widgets in left_frame.winfo_children():   #to delete old widgets
                            widgets.destroy()
                        lbl_wid = Label(left_frame,text="MONEY WITHDRAW PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
                        lbl_wid.place(relx=0.5,y=50,anchor=CENTER)
                        lbl_accno = Label(left_frame,text="AVAILABLE BALANCE:  ₹:",bg='#d9d9d9',font=("Arial",20,"bold"))
                        lbl_accno.place(x=130,y=140)
                        lbl_data = Label(left_frame,text=int_data,bg='#d9d9d9',font=("Arial",20,))
                        lbl_data.place(x=500,y=140)
                        cursor.close()
                        sqlcon.close()
                        back_btn = Button(left_frame,text="BACK",height=3,width=14, font=("Arial",16,"bold"),command=lambda: withdraw_page(left_frame, usname))
                        back_btn.place(x=350,y=550)
                        #time.sleep(5)
                        #addmoney_page(left_frame, usname)
                        #main.front(usname)
                    elif show_bal == 'no':
                        cursor.close()
                        sqlcon.close()
                        withdraw_page(left_frame, usname)
                except:
                    tkinter.messagebox.showerror("ERROR","SOMETHING WENT WRONG, TRY AGAIN!")
                    #print(error)
            else:
                tkinter.messagebox.showinfo("","INSUFFICIENT BALANCE!")
                #print("INSUFFICIENT BALANCE!")
                withdraw_page(left_frame, usname)
        except:
            tkinter.messagebox.showinfo("NOT FOUND","ACCOUNT NOT FOUND!")
            #print("Error")
            #time.sleep(2)
            withdraw_page(left_frame, usname)



def withdraw_page(left_frame,usname):
    for widgets in left_frame.winfo_children():   #to delete old widgets
        widgets.destroy()
    lbl_amp = Label(left_frame,text="MONEY WITHDRAW PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_amp.place(relx=0.5,y=50,anchor=CENTER)
    lbl_accno = Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_accno.place(x=130,y=140)
    accno = Entry(left_frame,width=25,font=("Arial",18))
    accno.place(x=370,y=140)
    lbl_amnt = Label(left_frame,text="AMOUNT : ₹",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_amnt.place(x=130,y=200)
    amnt = Entry(left_frame, width= 15,font=("Arial",18))
    amnt.place(x=370,y=205)
    lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_pin.place(x=130,y=260)
    pin = Entry(left_frame,width=12,show="*",font=("Arial",18))
    pin.place(x=370,y=260)
    submit_btn = Button(left_frame,text="WITHDRAW",height=3,width=14, font=("Arial",16,"bold"),command=lambda: withdraw(left_frame,usname,accno.get(),amnt.get(),pin.get()))
    submit_btn.place(x=350,y=550)
