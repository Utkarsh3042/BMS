import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox


def acc_create(acc_num,name,dob,aadhar,pan,phone,email,pin1,pin2,usname,left_frame):
    if len(pin1.get()) == 0:
        tkinter.messagebox.askretrycancel("PIN", "ENTER YOUR PIN!")
    elif len(pin2.get()) == 0:
        tkinter.messagebox.askretrycancel("PIN","ENTER YOUR PIN AGAIN!")
    elif pin1.get() != pin2.get():
        tkinter.messagebox.askretrycancel("FAILED", "PIN DOES NOT MATCH!")
    else:
        db_usname = usname+".db"
        try:
            sqlcon = sqlite3.connect('{}'.format(db_usname))
            cursor = sqlcon.cursor()
            query = '''INSERT INTO BMS VALUES({},'{}',{},{},'{}',{},'{}',{},0);'''.format(
                acc_num, name, dob, aadhar, pan, phone, email, pin1.get())
            cursor.execute(query)
            sqlcon.commit()
            cursor.close()
            sqlcon.close()
            tkinter.messagebox.showinfo("SUCCESS","ACCOUNT CREATED SUCCESSFULLY!")
            newacc(left_frame, usname)

        except sqlite3.Error as error:
            tkinter.messagebox.showerror("ERROR","SOMETHING WENT WRONG!")
            #print(error)

            
 


def pin_create(left_frame,name,dob,phone,aadhar,pan,email,usname):
    if len(name) == 0:
        tkinter.messagebox.askretrycancel("","ENTER NAME!")
    elif len(phone) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PHONE NUMBER!")
    elif len(aadhar) == 0:
        tkinter.messagebox.askretrycancel("","ENTER AADHAR!")
    elif len(pan) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PAN!")
    else:
        try:
            dob = dob.replace("/","") 
            acc_num = phone+dob
            acc_num = int(acc_num)
            #print(acc_num)
            dob = int(dob)
            phone = int(phone)
            aadhar = int(aadhar)
            for widgets in left_frame.winfo_children():
                widgets.destroy()
            lbl_nap = Label(left_frame,text="NEW ACCOUNT PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
            lbl_nap.place(relx=0.5,y=50,anchor=CENTER)
            lbl_accno = Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold"))
            lbl_accno.place(x=150,y=140)
            lbl_acc_num = Label(left_frame,text=acc_num,bg='#d9d9d9',font=("Arial",18))
            lbl_acc_num.place(x=450,y=140)
            lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
            lbl_pin.place(x=200,y=250)
            pin1 = Entry(left_frame,show="*",width=10,font=(20))
            pin1.place(x=450,y=250)
            lbl_pin_cnf = Label(left_frame,text="CONFIRM PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
            lbl_pin_cnf.place(x=150,y=310)
            pin2 = Entry(left_frame,show="*",width=10,font=(20))
            pin2.place(x=450,y=310)
            submit_btn = Button(left_frame,text="SUBMIT",height=3,width=14, font=("Arial",15,"bold"),command=lambda: acc_create(acc_num,name,dob,aadhar,pan,phone,email,pin1,pin2,usname,left_frame))
            submit_btn.place(x=350,y=550)
        except:
            tkinter.messagebox.showerror("ERROR","SOMETHING WENT WRONG!")

    





def newacc(left_frame,usname):
    for widgets in left_frame.winfo_children():    #to delete old widgets
        widgets.destroy()
    lbl_nap = Label(left_frame,text="NEW ACCOUNT PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_nap.place(relx=0.5,y=50,anchor=CENTER)
    lbl_name = Label(left_frame,text="NAME :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_name.place(x=150,y=140)
    name = Entry(left_frame,width=25,font=("Arial",18))
    name.place(x=330,y=140)
    lbl_dob = Label(left_frame,text="D.O.B :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_dob.place(x=150,y=200)
    dob = DateEntry(left_frame,date_pattern='dd/mm/yyyy', width= 15,font=("Arial",15))
    dob.place(x=330,y=205)
    lbl_numb = Label(left_frame,text="PHONE :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_numb.place(x=150,y=260)
    phone = Entry(left_frame,width=12,font=("Arial",18))
    phone.place(x=330,y=260)
    lbl_aadhar = Label(left_frame,text="AADHAR :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_aadhar.place(x=150,y=320)
    aadhar = Entry(left_frame,width=14,font=("Arial",18))
    aadhar.place(x=330,y=320)
    lbl_pan = Label(left_frame,text="PAN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_pan.place(x=150,y=380)
    pan = Entry(left_frame,width=15,font=("Arial",18))
    pan.place(x=330,y=380)
    lbl_email = Label(left_frame,text="EMAIL(OPT) :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_email.place(x=150,y=440)
    email = Entry(left_frame,width=25,font=("Arial",18))
    email.place(x=330,y=440)
    submit_btn = Button(left_frame,text="CREATE",height=3,width=14, font=("Arial",15,"bold"),command=lambda: pin_create(left_frame,name.get(),dob.get(),phone.get(),aadhar.get(),pan.get(),email.get(),usname))
    submit_btn.place(x=350,y=550)