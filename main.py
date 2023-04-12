import sqlite3
import json
import os.path
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#user created modules
import new_acc
import add_mon
import withd_mon
import check_bal
import acc_det
import rem_acc

#code
def log_sign():
    if(os.path.exists('info.json')):
        login_page()
    else:
        signup_page()

# call function when we click on entry box
# def click(*args):
#     usname.delete(0, 'end')
  


def acc_create(usname,pass1,pass2,window):
    if usname in ["username","USERNAME"]:
        tkinter.messagebox.showerror('ERROR','USE VALID USERNAME!')
    
    else:
        if pass1 == pass2:
            info_data = {"username":usname,"password":pass2}
            dbname = usname+".db"
            try:
                sqlcon = sqlite3.connect(dbname)
                cursor = sqlcon.cursor()
                query = '''CREATE TABLE BMS (ACCNO INT PRIMARY KEY NOT NULL,
                                            NAME TEXT NOT NULL,
                                            DOB INT NOT NULL,
                                            AADHAR INT NOT NULL,
                                            PAN TEXT NOT NULL,
                                            PHONE INT NOT NULL,
                                            EMAIL TEXT,
                                            PIN INT NOT NULL,
                                            AMNT INT NOT NULL
                                            );'''
                cursor.execute(query)
                file_json = open("info.json", "w")
                json.dump(info_data, file_json)
                file_json.close()
                #os.system('cls')
                #print("Sucessfully Created Account & Database!")
                cursor.close()
                sqlcon.close()
                tkinter.messagebox.showinfo('','PROFILE & DATABASE CREATED SUCCESSFULLY!',command=window.destroy())
                log_sign()
            except sqlite3.Error as error:
                #print(error)
                tkinter.messagebox.showerror('ERROR','SOMETHING WENT WRONG!')
                
        else:
            tkinter.messagebox.showerror('ERROR','PASSWORD DOES NOT MATCH')


def login(usname,passw,window):
    file_json = open('info.json', 'r')
    op_json = json.load(file_json)
    usname_json = op_json["username"]
    pass_json = op_json["password"]
    if (usname == usname_json and passw == pass_json):
        file_json.close()
        #tkinter.messagebox.showinfo('','LOGINED SUCCESSFULLY!',command=window.destroy())
        #print("Logined Successfully!")
        window.destroy()
        front(usname)
    else:
        tkinter.messagebox.showerror('USER NOT FOUND','WRONG USERNAME OR PASSWORD!')
        #print("Wrong username or password")
        file_json.close()
        window.destroy()
        log_sign()


def remove(usname,pass1,pass2,window):
    if pass1==pass2:
        file_json = open('info.json')
        op_json = json.load(file_json)
        usname_json = op_json["username"]
        pass_json = op_json["password"]
        if (usname == usname_json and pass1 == pass_json):
            file_json.close()
            cnfirm = tkinter.messagebox.askquestion("REMOVE?","ARE YOU SURE? THIS WILL DELETE YOUR DATABASE TOO!")
            if (cnfirm == "yes"):
                dbname = usname+".db"
                os.remove('info.json')
                os.remove('{}'.format(dbname))
                #os.system('cls')
                #print("Account & Database Removed Successfully!")
                tkinter.messagebox.showinfo("REMOVED","PROFILE & DATABASE REMOVED SUCCESSFULLY!")
                window.destroy()
                log_sign()
            else:
                window.destroy()
                log_sign()
        else:
            file_json.close()
            #print("")
            #print("USERNAME OR PASSWORD DOES NOT MATCH")
            tkinter.messagebox.showerror('USER NOT FOUND','WRONG USERNAME OR PASSWORD!')
            window.destroy()
            log_sign()
    else:
        tkinter.messagebox.showwarning("WARNING","USE VALID USERNAME & PASSWORD!")
        window.destroy()
        log_sign()

def remove_page():
    window = tk.Tk()
    window.title("REMOVE")
    window.geometry('350x300')
    window.configure(bg='#d9d9d9')
    window.resizable(False,False)
    lbl1 = Label(window,text="PROFILE REMOVE",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_blk = Label(window,text="",bg='#d9d9d9')
    usname = Entry(window,width=20,font=("Arial",16))
    usname.insert(0, 'username')
    #usname.bind("<Button-1>",click(usname))
    lbl_blk2 = Label(window,text="",bg='#d9d9d9')
    pass1 = Entry(window,width=20,font=("Arial",16))
    pass1.insert(0, 'password')
    #pass1.bind("<Button-1>",click(pass1))
    lbl_blk3 = Label(window,text="",bg='#d9d9d9')
    pass2 = Entry(window,width=20,font=("Arial",16))
    pass2.insert(0, 'password again')
    #pass2.bind("<Button-1>",click(pass2))
    lbl_blk4 = Label(window,text="",bg='#d9d9d9')
    lbl_blk5 = Label(window,text="",bg='#d9d9d9')
    btn = ttk.Button(window,text="REMOVE",width=15,command=lambda:remove(usname.get(),pass1.get(),pass2.get(),window))
    lbl1.pack()
    lbl_blk.pack()
    usname.pack()
    lbl_blk2.pack()
    pass1.pack()
    lbl_blk3.pack()
    pass2.pack()
    lbl_blk4.pack()
    lbl_blk5.pack()
    btn.pack()
    window.mainloop()


def front(usname):
    window = tk.Tk()
    window.title("BMS")
    window.geometry('1280x720')
    left_frame  =  Frame(window,  width=800, bg='#d9d9d9')
    left_frame.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)
    right_frame  =  Frame(window,  width=150,  bg='#d9d9d9')
    right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)
    lbl_bms = Label(left_frame,text="WELCOME TO BMS",bg='#d9d9d9',font=("Arial",32,"bold","underline"))
    lbl_bms.place(relx=0.5,y=50,anchor=CENTER)
    text_info = Label(left_frame,text="Made By Utkarsh Saraswat\nGithub : github.com/Utkarsh3042",bg='#d9d9d9',font=(15)).place(relx=0.5,y=200,anchor=CENTER)
    new_acc_btn = Button(right_frame,text="NEW ACCOUNT",font=("Arial",15,"bold"),command=lambda :new_acc.newacc(left_frame,usname)).pack(ipady=38,ipadx=70)
    add_mon_btn = Button(right_frame,text="ADD MONEY",font=("Arial",15,"bold"),command=lambda :add_mon.addmoney_page(left_frame, usname)).pack(ipady=38,ipadx=85)
    withd_mon_btn = Button(right_frame,text="WITHDRAW MONEY",font=("Arial",15,"bold"),command=lambda :withd_mon.withdraw_page(left_frame,usname)).pack(ipady=38,ipadx=50)
    check_bal_btn = Button(right_frame,text="CHECK BALANCE",font=("Arial",15,"bold"),command=lambda :check_bal.checkbal_page(left_frame,usname)).pack(ipady=38,ipadx=61)
    acc_det_btn = Button(right_frame,text="ACCOUNT DETAILS",font=("Arial",15,"bold"),command=lambda :acc_det.accdetails_page(left_frame,usname)).pack(ipady=38,ipadx=52)
    rem_acc_btn = Button(right_frame,text="REMOVE ACCOUNT",font=("Arial",15,"bold"),command=lambda :rem_acc.remacc_page(left_frame,usname)).pack(ipady=38,ipadx=51)
    #log_out_btn = Button(left_frame,text="LOG OUT",font=("Arial",10,"bold"),height=2,width=15,command=lambda : [window.destroy(),log_sign()])
    #log_out_btn.place(x=30,y=30)
    window.mainloop()

def login_page():
    window = tk.Tk()
    window.title("LOGIN")
    window.configure(bg='#d9d9d9')
    window.geometry('350x250')
    window.resizable(False,False)
    lbl1 = Label(window,text="BMS  LOGIN",font=("Arial",20,"bold"),bg='#d9d9d9')
    lbl_blk = Label(window,text="",bg='#d9d9d9')
    usname = Entry(window,width=20,font=("Arial",16))
    usname.insert(0, 'username')
    #usname.bind("<Button-1>",click)
    lbl_blk2 = Label(window,text="",bg='#d9d9d9')
    passw = Entry(window,width=20,font=("Arial",16))
    passw.insert(0, 'password')
    #passw.bind("<Button-1>",click)
    lbl_blk3 = Label(window,text="",bg='#d9d9d9')
    btn = ttk.Button(window,text="LOGIN",width=15,command=lambda:login(usname.get(),passw.get(),window))
    btn_rem = ttk.Button(window,text="PROFILE REMOVE",width=20,command=lambda:[window.destroy(),remove_page()])
    lbl1.pack()
    lbl_blk.pack()
    usname.pack()
    lbl_blk2.pack()
    passw.pack()
    lbl_blk3.pack()
    btn.pack()
    btn_rem.pack(side=BOTTOM)
    window.mainloop()

def signup_page():
    window = tk.Tk()
    window.title("SIGNUP")
    window.geometry('350x300')
    window.configure(bg='#d9d9d9')
    window.resizable(False,False)
    lbl1 = Label(window,text="BMS  SIGNUP",bg='#d9d9d9',font=("Arial",20,"bold"))
    lbl_blk = Label(window,text="",bg='#d9d9d9')
    usname = Entry(window,width=20,font=("Arial",16))
    usname.insert(0, 'username')
    #usname.bind("<Button-1>",click(usname))
    lbl_blk2 = Label(window,text="",bg='#d9d9d9')
    pass1 = Entry(window,width=20,font=("Arial",16))
    pass1.insert(0, 'password')
    #pass1.bind("<Button-1>",click(pass1))
    lbl_blk3 = Label(window,text="",bg='#d9d9d9')
    pass2 = Entry(window,width=20,font=("Arial",16))
    pass2.insert(0, 'password again')
    #pass2.bind("<Button-1>",click(pass2))
    lbl_blk4 = Label(window,text="",bg='#d9d9d9')
    lbl_blk5 = Label(window,text="",bg='#d9d9d9')
    btn = ttk.Button(window,text="SIGNUP",width=15,command=lambda: acc_create(usname.get(),pass1.get(),pass2.get(),window))
    lbl1.pack()
    lbl_blk.pack()
    usname.pack()
    lbl_blk2.pack()
    pass1.pack()
    lbl_blk3.pack()
    pass2.pack()
    lbl_blk4.pack()
    lbl_blk5.pack()
    btn.pack()
    window.mainloop()

log_sign()
