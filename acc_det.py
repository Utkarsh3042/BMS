import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


# def hide_show_pin(pin_data,lbl_pin,btn_pin):
#     if btn_pin['text'] == "SHOW":
#         lbl_pin.config(text=pin_data)
#         btn.config(text="HIDE")
#     elif btn['text'] == 'HIDE':
#         pin.config(text="*****")
#         btn.config(text="SHOW")


def details_exract(left_frame,data,usname):
    data = tuple(data)
    data = data[0]
    accno = data[0]
    name = data[1]
    dob = str(data[2])
    dob = dob[:2]+'/'+dob[2:]
    dob = dob[:5]+'/'+dob[5:]
    aadhar = data[3]
    pan = data[4]
    phone = data[5]
    email = data[6]
    pin = data[7]
    amnt = data[8]
    #print(accno,name,dob,aadhar,pan,phone,email,pin,amnt)
    for widgets in left_frame.winfo_children():   #to delete old widgets
        widgets.destroy()
    lbl_det = Label(left_frame,text="ACCOUNT DETAILS PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_det.place(relx=0.5,y=50,anchor=CENTER)
    Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=120)
    Label(left_frame,text=accno,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=120)
    Label(left_frame,text="NAME :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=170)
    Label(left_frame,text=name,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=170)
    Label(left_frame,text="PHONE :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=220)
    Label(left_frame,text=phone,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=220)
    Label(left_frame,text="AADHAR :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=270)
    Label(left_frame,text=aadhar,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=270)
    Label(left_frame,text="PAN :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=320)
    Label(left_frame,text=pan,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=320)
    Label(left_frame,text="D.O.B :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=370)
    Label(left_frame,text=dob,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=370)
    Label(left_frame,text="EMAIL :",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=420)
    Label(left_frame,text=email,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=420)
    Label(left_frame,text="AMOUNT ₹:",bg='#d9d9d9',font=("Arial",20,"bold")).place(x=130,y=470)
    Label(left_frame,text=amnt,bg='#d9d9d9',font=("Arial",18)).place(x=370,y=470)
    #lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    #lbl_pin.place(x=130,y=520)
    # pin_data = Label(left_frame,text="******",bg='#d9d9d9',font=("Arial",18)).place(x=370,y=520)
    # btn_pin = Button(left_frame,text="SHOW",font=("Arial",10,"bold"),command=lambda :hide_show_pin(pin_data,btn_pin,pin))
    # btn_pin.place(x=450,y=520)

    back_btn = Button(left_frame,text="BACK",height=2,width=10, font=("Arial",16,"bold"),command=lambda:accdetails_page(left_frame,usname))
    back_btn.place(x=350,y=550)

    
def accdetails(left_frame,usname,accno,pin):
    if len(accno) == 0:
        tkinter.messagebox.askretrycancel("","ENTER ACCOUNT NUMBER")
    elif len(pin) == 0:
        tkinter.messagebox.askretrycancel("","ENTER PIN!")
    else:
        db_usname = usname+".db"
        try:
            sqlcon = sqlite3.connect(db_usname)
            cursor = sqlcon.cursor()
            query = '''SELECT * FROM BMS WHERE ACCNO={} AND PIN={};'''.format(accno,pin)
            cursor.execute(query)
            data = cursor.fetchall()
            details_exract(left_frame,data,usname)
                   
        except:
            tkinter.messagebox.showinfo("NOT FOUND","ACCOUNT NOT FOUND!")
def accdetails_page(left_frame,usname):
    for widgets in left_frame.winfo_children():   #to delete old widgets
        widgets.destroy()
    lbl_det = Label(left_frame,text="ACCOUNT DETAILS PAGE",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_det.place(relx=0.5,y=50,anchor=CENTER)
    lbl_accno = Label(left_frame,text="ACCOUNT NO :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_accno.place(x=130,y=140)
    accno = Entry(left_frame,width=25,font=("Arial",18))
    accno.place(x=370,y=140)
    lbl_pin = Label(left_frame,text="PIN :",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_pin.place(x=130,y=200)
    pin = Entry(left_frame,width=12,show="*",font=("Arial",18))
    pin.place(x=370,y=200)
    submit_btn = Button(left_frame,text="GET DETAILS",height=3,width=14, font=("Arial",16,"bold"),command=lambda:accdetails(left_frame, usname, accno.get(), pin.get()))
    submit_btn.place(x=350,y=550)
