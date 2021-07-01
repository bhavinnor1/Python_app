import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import tkinter.ttk as ttk
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from time import strftime

pagenum = 1
win = Tk()
win.title("Mystic OS")
win.minsize(100,150)
win.iconbitmap('D:/tabcc/tkinterapp/ci.ico')
bg = PhotoImage(file="manywoo.png")
bg2=PhotoImage(file="Op12.png")
tbbg = ImageTk.PhotoImage(file="background.png")
myfont=font.Font(family="alternate sans",size="10",weight="bold")

no=2
def evod():
    global no
    no+=1
    global show, passwordtxt, pentry

def sshowpwd(e):
        def sbind():
                text1=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7,  activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=shide)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)
                show.config(text=text1)
                evod()
        def shide():
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=sbind)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)
                evod()
        if no % 2==0:
                txt=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=shide)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)
                show.config(text=txt)
        else:
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=sbind)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)

def sbind():
        global show, passwordtxt, pwdentry
        show.config(text = passwordtxt.get())
        def sbind():
                text1=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7,  activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=shide)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)
                show.config(text=text1)
                evod()
        def shide():
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=sbind)
                Lb2.grid(row=13,column=0,sticky='e',padx=20)
                evod()
        pwdentry.bind("<KeyRelease>", sshowpwd)
        Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=shide)
        Lb2.grid(row=13,column=0,sticky='e',padx=20)

def showpwd(e):
        def bind():
                text1=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7,  activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=hide)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)
                show.config(text=text1)
                evod()
        def hide():
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=bind)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)
                evod()
        if no % 2==0:
                txt=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=hide)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)
                show.config(text=txt)
        else:
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=bind)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)

def bind():
        global show, passwordtxt, pentry
        show.config(text = passwordtxt.get())
        def bind():
                text1=passwordtxt.get()
                Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7,  activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=hide)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)
                show.config(text=text1)
                evod()
        def hide():
                show.config(text="")
                Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=bind)
                Lb2.grid(row=4,column=0,sticky='e',padx=20)
                evod()
        pentry.bind("<KeyRelease>", showpwd)
        Lb2=Button(win,text="Hide", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=hide)
        Lb2.grid(row=4,column=0,sticky='e',padx=20)

def forgotpwd():
        global usernamelist, passwordlist, userentryl, passwordtxt, usernamelist2, passwordlist2, usr12, emailentry5
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='userdata', port=3306)
        mycursor = conn.cursor()
        mycursor.execute("select * from udata")
        mdadata = mycursor.fetchall()
        print(mdadata)
        emaillist = []
        usernamelist2 = []
        passwordlist2 = []
        for i in mdadata:
                emln = emaillist.append(i[0])
                usrn = usernamelist2.append(i[2])
                pwdn = passwordlist2.append(i[3])
        ldno=0
        if emailentry5.get()=="":
                messagebox.showerror("Database", "Email not Entered.\nPlease Enter your Email :(")
        elif len(emailentry5.get())>1:
                emailfound = False
                for i in emaillist:
                        print(emailentry5.get() + '=' + i)
                        if emailentry5.get()==i:
                                lid = usernamelist2[ldno]
                                pwd = passwordlist2[ldno]
                                msgboxtxt = "Login Id: " + lid +"\nPassword: " + pwd
                                messagebox.showinfo("Details",msgboxtxt)
                                print("email found.")
                                emailfound=True
                                print(passwordlist[ldno])
                        ldno+=1
                if emailfound == False:
                        messagebox.showerror("Details","Email Not Found.")
                                
        else:
                messagebox.showerror("Database", "Invalid Email.\nPlease Enter a valid Email :(")
        

def loginchk123():
        global usernamelist, passwordlist, userentryl, passwordtxt, usernamelist, passwordlist, usr12
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='userdata', port=3306)
        mycursor = conn.cursor()
        mycursor.execute("select * from udata")
        mdadata = mycursor.fetchall()
        print(mdadata)
        usernamelist = []
        passwordlist = []
        for i in mdadata:
                usrn= usernamelist.append(i[2])
                pwdn = passwordlist.append(i[3])
        ldno = 0
        print(usernamelist)
        print(passwordlist)
        if userentryl.get()=="" or passwordtxt.get()=="":
                if userentryl.get()=="" and passwordtxt.get()=="":
                        messagebox.showerror("Database", "Nothing Entered.\nInputs Required.")
                elif userentryl.get()=="":
                        messagebox.showerror("Database", "Username not Entered.\nPlease Enter your Username :(")
                elif passwordtxt.get()=="":
                        messagebox.showerror("Database", "Password not Entered.\nPlease Enter your Password :(")
                else:
                        messagebox.showerror("Database", "Cant Understand the error.")
                
        elif len(userentryl.get())>3 and len(passwordtxt.get())>7:
                usrfound=False
                pwdfound=False
                for i in usernamelist:
                        print("for loop")
                        print(userentryl.get() + '=' + i)
                        
                        if userentryl.get()==i:
                                print("Username found.")
                                usrfound=True
                                print(passwordlist[ldno])
                                if passwordtxt.get()==passwordlist[ldno]:
                                        pwdfound=True
                                        print("Password Verified.")
                                        messagebox.showinfo("Database", "Login Successful.")
                                        usr12=userentryl.get()
                                        cpg7()
                                        break
                        ldno+=1
                if usrfound==False:
                        messagebox.showerror("Database", "Username Not found.")
                        print("Username Not found")
                elif pwdfound==False:
                        messagebox.showerror("Database", "Incorrect Password.")
                        print("Password Incorrect.")
                                
                        
        else:
                messagebox.showerror("Database", "Invalid Username or Password.")
        

def storename():
        global userentry, userentryl, pageno, usr12, pagenum
        usr12 = ""
        pagenum=3
        if pageno==2:
                usr12 = userentry.get()
                sizechk()

pageno = 1
        

def spacechk():
        global emailentry, nameentry, userentry, passwordtxt, pagenum
        eml = emailentry.get()
        name= nameentry.get()
        usr = userentry.get()
        usern = list(usr)
        print(usern)
        pwd = passwordtxt.get()
        nospace = True
        for i in eml:
                if i==" ":
                        nospace = False
                        messagebox.showinfo("Database", "Email should not contain spaces.")
                        break     
        for i in usern:
                if i==" ":
                        nospace = False
                        messagebox.showinfo("Database", "Username should not contain spaces.")    
        for i in pwd:
                if i==" ":
                        nospace = False
                        messagebox.showinfo("Database", "password should not contain spaces.")
                        break    
        if nospace==True:
                datae()
                        
def sizechk():
        global emailentry, nameentry, userentry, passwordtxt
        eml = emailentry.get()
        name= nameentry.get()
        usr = userentry.get()
        usern = list(usr)
        pwd = passwordtxt.get()
        if len(eml)<2:
                messagebox.showinfo("Database", "Email is too small.")
                print("email too small")
        elif len(name)<1:
                messagebox.showinfo("Database", "Name is too small.")
                print("name too small")
        elif len(usern)<4:
                messagebox.showinfo("Database", "Username is too small.\nit should be between 4 to 20 characters.")
                print("username is too small")
        elif len(pwd)<8:
                messagebox.showinfo("Database", "Password is too small.\nit should be between 8 to 20 characters.")
                print("password is too small")
        else:
                spacechk()
        
        
        
def datae():
        global emailentry, nameentry, userentry, passwordtxt
        eml = emailentry.get()
        name= nameentry.get()
        usr = userentry.get()
        pwd = passwordtxt.get() 
        try:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='userdata', port=3306)
                mycursor = conn.cursor()
                cmd= "insert into udata(email, name, userid, password) values (%s, %s, %s, %s)"
                val=(eml, name, usr, pwd)
                mycursor.execute(cmd, val)
                conn.commit()
                print("data entered")
                messagebox.showinfo("Database", "You are Registered")
                cpg7()
        except mysql.connector.Error as error:
                print("Failed to update record to database: {}".format(error))
                messagebox.showinfo("Database", "Registeration Failed! \ncheck your inputed data")
        finally:
                conn.close()

def cpg1():
        global pagenum
        pagenum=2
        changepage()

def cpg3():
    global pagenum
    pagenum=3
    changepage()

def cpg4():
    global pagenum
    pagenum=4
    changepage()

def cpg5():
    global pagenum
    pagenum=5
    changepage()

def cpg6():
    global pagenum
    pagenum=6
    changepage()

def cpg7():
        global pagenum
        pagenum=7
        changepage()

def page1(win):
        global userentryl, pageno, passwordtxt, show, pentry
        win.unbind("<KeyPress>") 
        myfont= font.Font(family="magic",size="15", weight="bold")
        myfontog= font.Font(family="magic",size="8", weight="bold")
        myfont1= font.Font(family="alternate sans",size="8",weight="bold")
        myfont2= font.Font(family="alternate sans",size="7")
        myfont3 = font.Font(family="alternate sans",size="7",weight="bold")
        Label(win,text="", bg="#ffffff",width=41, height=30).grid(row=0,column=0,rowspan=30)
        Tcc=Label(win,text="Mystic OS", font=myfont, bg="white")
        Tcc.grid(row=0, column=0, pady=50)
        userid = Label(win, text="Login ID", font=myfont1, bg="white")
        userid.grid(row=1, column=0, sticky="sw",padx=18)
        userentryl= Entry(win, width=37, font=myfontog, bg="#fafafa")
        userentryl.grid(row=2,column=0,ipady=11, ipadx=11)
        password = Label(win, text="Password", font=myfont1, bg="white")
        password.grid(row=3, column=0, sticky="sw", padx=18)
        passwordtxt = StringVar()
        pentry = Entry(win,textvariable=passwordtxt,show="★", font=myfontog, width=28, bg="#fafafa")
        pentry.grid(row=4, column=0, padx=21, ipady=11, ipadx=11, sticky="w")
        Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=bind)
        Lb2.grid(row=4,column=0,sticky='e',padx=20)
        show = Label(win, text="", font=myfont1, bg="white")
        show.grid(row=5, column=0, sticky="sw", padx=18)
        Lb=Button(win,text="Log In", bg="#3897f1",fg="white", activebackground="white",activeforeground="#3897f1",font=myfont1,width=35, height=2, command=loginchk123)
        Lb.grid(row=6,column=0)
        Gh= Button(win, text="Get help signing in.", font=myfont3,bg="white", activebackground="white", command=page5)
        Gh.grid(row=7,column=0, sticky="e",padx=40)
        Frgt= Label(win,text="Forgot your login details?",font=myfont2, bg="white")
        Frgt.grid(row=7,column=0,sticky="w",padx=33)
        Frgt= Label(win,text="—————————————OR—————————————",font=myfont3, bg="white", fg="grey")
        Frgt.grid(row=8,column=0)
        Gh= Button(win, text="Sign up.", font=myfont3,bg="white", activebackground="white",command=changepage)
        Gh.grid(row=9,column=0, sticky="e",padx=92)
        Frgt= Label(win,text="Dont have an account?",font=myfont2, bg="white")
        Frgt.grid(row=9,column=0,sticky="w",padx=40)
        pageno=1


def page2(win):
        global emailentry, nameentry, userentry, passwordtxt, pageno, show, pwdentry
        win.unbind("<KeyPress>")
        myfont= font.Font(family="alternate sans",size="18", weight="bold")
        myfont1= font.Font(family="alternate sans",size="11",weight="bold")
        myfont2= font.Font(family="alternate sans",size="7")
        myfont3 = font.Font(family="alternate sans",size="8",weight="bold")
        myfontog= font.Font(family="magic",size="9", weight="bold")
        myfontog2= font.Font(family="magic",size="8", weight="bold")
        Label(win,text="", bg="#ffffff", width=41, height=43).grid(row=0,column=0,rowspan=30)
        Tcc=Label(win,text="", font=myfont, bg="white")
        Tcc.grid(row=1, column=0)
        Tcc=Label(win,text="Mystic OS", font=myfont, bg="white")
        Tcc.grid(row=2, column=0)
        msg1=Label(win,text="Sign up to get tables and copy it \n for maths.", font=myfont1, bg="white", fg="grey")
        msg1.grid(row=3, column=0)
        Lb=Button(win,text="Go Back", bg="#3897f1",fg="white", activebackground="white",activeforeground="#3897f1",font=myfont3,width=35, height=2, command=changepage)
        Lb.grid(row=4, column=0,pady=10)
        Frgt= Label(win,text="———————————OR———————————",font=myfont3, bg="white", fg="grey")
        Frgt.grid(row=5,column=0)

        email = Label(win, text="Email", font=myfont3, bg="white")
        email.grid(row=6, column=0, sticky="sw",padx=15)
        emailentry= Entry(win, width=37, font=myfontog2, bg="#fafafa")
        emailentry.grid(row=7, column=0, ipady=11, ipadx=15)

        name = Label(win, text="Full Name", font=myfont3, bg="white")
        name.grid(row=8, column=0, sticky="sw",padx=15)
        nameentry= Entry(win, width=37, font=myfontog2, bg="#fafafa")
        nameentry.grid(row=9, column=0,ipady=11, ipadx=15)
        userid = Label(win, text="Username", font=myfont3, bg="white")
        userid.grid(row=10, column=0, sticky="sw",padx=15)
        userentry= Entry(win, width=37, font=myfontog2, bg="#fafafa")
        userentry.grid(row=11, column=0, ipady=11, ipadx=15)
        password = Label(win, text="Password", font=myfont3, bg="white")
        password.grid(row=12, column=0, sticky="sw",padx=15)
        passwordtxt = StringVar()
        pwdentry= Entry(win, width=28, font=myfontog2,textvariable=passwordtxt,show="★", bg="#fafafa")
        pwdentry.grid(row=13, column=0, padx=18, ipady=11, ipadx=15, sticky="w")
        
        Lb2=Button(win,text="Show", bg="#3897f1",fg="white", width=7, activebackground="white",activeforeground="#3897f1",font=(('arial'),8), height=2, command=sbind)
        Lb2.grid(row=13,column=0,sticky='e',padx=20)
        show = Label(win, text="", font=myfont3, bg="white")
        show.grid(row=14, column=0, padx=15, sticky="w")
        Lb=Button(win,text="Sign up", bg="#3897f1",fg="white", activebackground="white",activeforeground="#3897f1",font=myfont3,width=35, height=2,command=storename)
        Lb.grid(row=15, column=0,pady=10)
        userid = Label(win, text="By signing up, you agree to our", font=myfont3, bg="white", fg="grey")
        userid.grid(row=16, column=0)
        Gh= Button(win, text="Terms & privacy policy.", font=myfont3,bg="white", activebackground="white",activeforeground="grey",command=cpg4)
        Gh.grid(row=17, column=0)
        pageno=2


def page3(win):
        global userentry, userentryl, pageno, usr12
        win.unbind("<KeyPress>")
        welc = "Welcome, " + usr12
        def rtf():
                entr = int(random.randrange(1,100))
                limit = entr*10+1
                m=1
                j=400
                table.delete("1.0","end")
                for i in range(entr,limit,entr):
                        ans =str(entr) +" × " +str(m)+ " = " +str(i)
                        noob=ans+"\n"
                        table.insert(INSERT,noob)
                        m+=1
        def tablefinder():
                try:
                        entr= int(enter.get())
                except:
                        messagebox.showinfo("Error","Entered value is not a number")
                else:
                        if entr==0:
                                messagebox.showinfo("Error","0 doesn't has a table")
                        else:
                                entr = int(enter.get())
                                limit = entr*10+1
                                m=1
                                j=400
                                table.delete("1.0","end")
                                for i in range(entr,limit,entr):
                                        ans =str(entr) +" × " +str(m)+ " = " +str(i)
                                        table.insert(INSERT,str(ans)+"\n")
                                        m += 1
        def Close():
                win.destroy()
        tk.Label(win, text="", image=tbbg).place(x=0,y=0)
        f1=Frame(win)
        f1.pack()
        textlogout = "[->"
        Label(f1,text=welc,font=myfont, bg= "red", fg="cyan").pack(side=LEFT)
        tk.Button(f1, text=textlogout, command=cpg7).pack(side=LEFT)
        f2=Frame(win)
        f2.pack()
        Label(win,text="Enter the number and get the table for it",font=myfont, bg= "cyan").pack()
        enter = Entry(win,bd=10)
        enter.pack()
        tk.Button(win,text="Calculate",command=tablefinder,bg="black",fg="#3897f1",font=myfont, bd="10").pack()
        answer = tk.Label(win,text="Check your table below",fg="yellow",bg="green")
        tk.Label(win,text="©Bhavin.All rights reserved.", font=myfont, bg="yellow").pack()
        answer.pack()
        table = Text(win,font=myfont,height=10,width=30)
        table.pack()
        tk.Label(win, text="select the whole text (Ctrl+A)", font=myfont, bg="cyan").pack()
        tk.Label(win, text="and Press Ctrl+C to Copy the table.", font=myfont, bg="cyan").pack()
        tk.Label(win, text="Use Ctrl+V to paste it elsewhere.", font=myfont, bg="cyan").pack()
        tk.Button(win,text="Generate Random Table",command=rtf,bg="black",fg="#3897f1",font=myfont,bd="10").pack()
        tk.Label(win,text="[From 1-100]", font=myfont, bg="cyan").pack()
        exit_button=Button(win,text="Exit",command=cpg7,bg="black",fg="red",font=myfont,bd="10").pack()

def page4(win):
    global bg2
    myfont= font.Font(family="magic",size="12", weight="bold")
    myfont2= font.Font(family="alternate sans",size="8",weight="bold")
    myfont1= font.Font(family="alternate sans",size="8")
    myfont3 = font.Font(family="alternate sans",size="7",weight="bold")
    myfontd= font.Font(family="magic",size="23", weight="bold")
    myfonttou= font.Font(family="magic",size="20")
    myfontbt= font.Font(family="magic",size="15")
    Label(win,text="", bg="#ffffff", width=46,height=3).grid(row=0,column=0,columnspan=3)
    Label(win,text="", bg="#ffffff", width=46,height=8).grid(row=1,column=0,columnspan=3)
    Tcc=Label(win,text="Mystic OS", image=bg2, compound=LEFT, font=myfont, bg="white")
    Tcc.grid(row=1, column=0, pady=30, padx=15, columnspan=2)
    ln= Button(win, text="Log In", font=myfont3,fg="white", bg="#3897f1",activebackground="white", activeforeground="#3897f1",command=cpg1)
    ln.grid(row=1,column=2)
    f=Frame(win)
    f.grid(row=2,column=0,rowspan=30,columnspan=3)
    Label(f,text="", bg="#ffffff",width=46, height=56).grid(row=2,column=0,rowspan=150,columnspan=3)
    tou=Label(f,text="Terms of Use", font=myfonttou, bg="white")
    tou.grid(row=3,column=0,columnspan=2,padx=15,sticky="w",pady=30)
    ti=Label(f,text="We are updating our Terms of Use: Our updated\nTerms of Use will be effective on January 19,    \n2013                                                                            ", font=myfont2, bg="white")
    ti.grid(row=4,column=0,columnspan=3,padx=15,sticky="w")
    ti=Label(f,text="—————————————————————————–", font=myfont2, bg="white",fg="grey",anchor="e",height=1)
    ti.grid(row=5,column=0,columnspan=3)
    ti=Label(f,text="By using the Table calculator app and Table               \nCalculator service you are agreeing to be                    \nbound by the following terms and conditions              \n(''Terms of Use'').                                                              ", font=myfont2, bg="white")
    ti.grid(row=6,column=0,padx=15,columnspan=3)
    tou=Label(f,text="Basic terms", font=myfontbt, bg="white")
    tou.grid(row=7,column=0,columnspan=2,sticky="w",padx=15,pady=30)
    one=Label(f,text="1.", font=myfont3, bg="white")
    one.grid(row=8,column=0,sticky="ne")
    onec=Label(f,text="You must be 1 year or older to use this \napp.                                                  ", font=myfont3, bg="white")
    onec.grid(row=8,column=1,sticky="nw",columnspan=2)
    two=Label(f,text="2.", font=myfont3, bg="white")
    two.grid(row=9, column=0,sticky="ne")
    twoc=Label(f,text="You are responsible for any activity that \noccurs under your screen name.          ", font=myfont3, bg="white")
    twoc.grid(row=9,column=1,sticky="nw",columnspan=2)
    three=Label(f,text="3.", font=myfont3, bg="white")
    three.grid(row=10, column=0,sticky="ne")
    threec=Label(f,text="You are responsible for keeping your \npassword secure.                            ", font=myfont3, bg="white")
    threec.grid(row=10,column=1,sticky="nw",columnspan=2)
    four=Label(f,text="4.", font=myfont3, bg="white")
    four.grid(row=11, column=0,sticky="ne")
    fourc=Label(f,text="You may not use the TableCalc service for  \nany illegal or unauthorized purpose.              \nInternational users agree to comply with all \nlocal laws regarding online conduct and       \nacceptable content.                                          ", font=myfont3, bg="white")
    fourc.grid(row=11,column=1,sticky="nw",columnspan=2)
    five=Label(f,text="5.", font=myfont3, bg="white")
    five.grid(row=12, column=0,sticky="ne")
    fivec=Label(f,text="You must not modify, adapt or hack            \nTableCalc or modify another app so as       \nto falsely imply that it is associated with    \nTable Calculator.                                             ", font=myfont3, bg="white")
    fivec.grid(row=12,column=1,sticky="nw",columnspan=2)
''' six=Label(f,text="6.", font=myfont3, bg="white")
    six.grid(row=13, column=0,sticky="ne",padx=30)
    sixc=Label(f,text="You must not access TableCalc's private            \nAPI by any other means other than the                \nTable Calculator application itself.                       ", font=myfont3, bg="white")
    sixc.grid(row=13,column=1,sticky="nw",padx=30,columnspan=2)
    seven=Label(f,text="7.", font=myfont3, bg="white")
    seven.grid(row=14, column=0,sticky="ne",padx=30)
    sevenc=Label(f,text="You are solely responsible for your conduct  \nand any data, text, information, screen           \nnames, graphics, photos, profiles, audio and \nvideo clips, links (''Content'') that you              \nsubmit, post, and display on the TableCalc     \nservice.                                                                  ", font=myfont3, bg="white")
    sevenc.grid(row=14,column=1,sticky="nw",padx=30,columnspan=2)
    eight=Label(f,text="8.", font=myfont3,bg="white")
    eight.grid(row=15, column=0,sticky="ne",padx=30)
    eightc=Label(f,text="You must not transmit any worms or viruses\nor any code of a destructive nature.                ", font=myfont3, bg="white")
    eightc.grid(row=15,column=1,sticky="nw",padx=30,columnspan=2)
    nine=Label(f,text="9.", font=myfont3, bg="white")
    nine.grid(row=16, column=0,sticky="ne",padx=30)
    ninec=Label(f,text="You must not, in the use of TableCalc,\nviolate any laws in your jurisdiction      \n(including but not limited to copyright \nlaws).                                                         ", font=myfont3, bg="white")
    ninec.grid(row=16,column=1,sticky="nw",padx=30,columnspan=2)
    ten=Label(f,text="10.", font=myfont3, bg="white")
    ten.grid(row=17, column=0,sticky="ne",padx=30)
    tenc=Label(f,text="Violation of any of these agreements will     \nresult in the termination of your TableCalc  \naccount. While TableCalc prohibits such      \nconduct and content on its app, you              \nunderstand and agree that TableCalc            \ncannot be responsible for the Content          \nposted on its app and you nonetheless         \nmay be exposed to such materials and that  \nyou use the TableCalc service at your own   \nrisk.                                                                      ", font=myfont3, bg="white")
    tenc.grid(row=17,column=1,sticky="nw",padx=30,columnspan=2)'''

def page5():
        global emailentry5, win1
        win1=Toplevel(win)
        myfont3 = font.Font(family="alternate sans",size="8",weight="bold")
        myfontog2= font.Font(family="magic",size="8", weight="bold")
        Label(win, text="",font=myfont3, bg="white").grid(row=0, column=0, rowspan=3)
        email=Label(win1, text="Enter your Email",font=myfont3, bg="white")
        email.grid(row=0, column=0, sticky="sw",padx=15)
        emailentry5= Entry(win1, width=37, font=myfontog2, bg="#fafafa")
        emailentry5.grid(row=1, column=0, ipady=11, ipadx=15)
        Lb=Button(win1,text="Send", bg="#3897f1",fg="white", activebackground="white",activeforeground="#3897f1",font=myfont3,width=35, height=2,command=forgotpwd)
        Lb.grid(row=3, column=0,pady=10)

bg34=PhotoImage(file="mhp.png")
bgmp=PhotoImage(file="mmp1.png")
num=0
dis=""
def gui(win):
        global ent,mcode
        win.minsize(300, 493)
        Label(win, text="", image=bgmp).place(x=0, y=0)
        ent = Text(win,height=4, width=27, bg="#b8b5ff", borderwidth=0, font=('Product sans', 10, 'bold'))
        ent.place(x=53, y=100)
        encr=Button(win,text="Convert", bg="#b8b5ff", font=('Alternate sans', 8, 'bold'),  command=morsecode)
        encr.place(x=115, y=194)
        mcode=Text(win,height=3, width=21, bg="#b8b5ff", borderwidth=0, font=('Product sans', 13, 'bold'))
        mcode.place(x=53, y=341)
        dcr=Button(win,text="Convert", bg="#b8b5ff",font=('Alternate sans', 8, 'bold'), command=dcrypt)
        dcr.place(x=115, y=428)
        dcr=Button(win,text="Back", bg="#b8b5ff",font=('Alternate sans', 8, 'bold'), command=cpg7)
        dcr.place(x=125, y=470)

def morsecode():
                global ent,mcode
                fgt = ent.get("1.0", END)
                words = list(fgt)
                Separate = []
                e =[]
                for a in words:
                        Separate.append(a)
                m = []
                for a in Separate:
                        if a == " ":
                                m.append("/" + " ")
                        elif a == "a" or a == "A":
                                m.append(".-" + " ")
                        elif a == "b" or a== "B":
                                m.append("-..." + " ")
                        elif a == "c" or a == "C":
                                m.append("-.-." + " ")
                        elif a == "d" or a== "D":
                                m.append("-.." + " ")
                        elif a == "e" or a == "E":
                                m.append("." + " ")
                        elif a == "f" or a== "F":
                                m.append("..-." + " ")
                        elif a== "g" or a== "G":
                                m.append("--." + " ")
                        elif a == "h" or a == "H":
                                m.append("...." + " ")
                        elif a == "i" or a == "I":
                                m.append(".." + " ")
                        elif a == "j" or a== "J":
                                m.append(".---" + " ")
                        elif a == "k" or a== "K":
                                m.append("-.-" + " ")
                        elif a == "l" or a == "L":
                                m.append(".-.." + " ")
                        elif a == "m" or a== "M":
                                m.append("--" + " ")
                        elif a == "n" or a == "N":
                                m.append("-." + " ")
                        elif a == "o" or a== "O":
                                m.append("---" + " ")
                        elif a == "p" or a == "P":
                                m.append(".--." + " ")
                        elif a == "q" or a== "Q":
                                m.append("--.-" + " ")
                        elif a == "r" or a == "R":
                                m.append(".-." + " ")
                        elif a == "s" or a== "S":
                                m.append("..." + " ")
                        elif a == "t" or a == "T":
                                m.append("-" + " ")
                        elif a == "u" or a== "U":
                                m.append("..-" + " ")
                        elif a == "v" or a == "V":
                                m.append("...-" + " ")
                        elif a == "w" or a== "W":
                                m.append(".--" + " ")
                        elif a == "x" or a== "X":
                                m.append("-..-" + " ")
                        elif a == "y" or a == "Y":
                                m.append("-.--" + " ")
                        elif a == "z" or a== "Z":
                                m.append("--.." + " ")
                        elif a == "1":
                                m.append(".----" + " ")
                        elif a == "2":
                                m.append("..---" + " ")
                        elif a == "3":
                                m.append("...--" + " ")
                        elif a == "4":
                                m.append("....-" + " ")
                        elif a == "5":
                                m.append("....." + " ")
                        elif a == "6":
                                m.append("-...." + " ")
                        elif a == "7":
                                m.append("--..." + " ")
                        elif a == "8":
                                m.append("---.." + " ")
                        elif a == "9":
                                m.append("----." + " ")
                        elif a == "0":
                                m.append("-----" + " ")
                        else:
                                e.append(a)
                if len(e)>1:
                        api=str(e)+'\nis/are not a number nor an\n alphabet so it \nwill not be converted\n sorry.'
                        messagebox.showinfo("error", api)
                Morsecode =""
                for i in m:
                        Morsecode = Morsecode +i
                mcode.delete("1.0", END)
                mcode.insert(INSERT,Morsecode)
       
def dcrypt():
                global ent,mcode
                Input = mcode.get("1.0", END)
                '''liat = list(Input)
                b=""
                dl=[]'''
                Split = Input.split()
                print(Split)
                m = []
                err=[]
                for a in Split:
                        if a == "/":
                                m.append(" ")
                        elif a == ".-":
                                m.append("A")
                        elif a == "-...":
                                m.append("B")
                        elif a == "-.-.":
                                m.append("C")
                        elif a == "-..":
                                m.append("D")
                        elif a == ".":
                                m.append("E")
                        elif a == "..-.":
                                m.append("F")
                        elif a== "--.":
                                m.append("G")
                        elif a == "....":
                                m.append("H")
                        elif a == "..":
                                m.append("I")
                        elif a == ".---":
                                m.append("J")
                        elif a == "-.-":
                                m.append("K")
                        elif a == ".-..":
                                m.append("L")
                        elif a == "--":
                                m.append("M")
                        elif a == "-.":
                                m.append("N")
                        elif a == "---":
                                m.append("O")
                        elif a == ".--.":
                                m.append("P")
                        elif a == "--.-":
                                m.append("Q")
                        elif a == ".-.":
                                m.append("R")
                        elif a == "...":
                                m.append("S")
                        elif a == "-":
                                m.append("T")
                        elif a == "..-":
                                m.append("U")
                        elif a == "...-":
                                m.append("V")
                        elif a == ".--":
                                m.append("W")
                        elif a == "-..-":
                                m.append("X")
                        elif a == "-.--":
                                m.append("Y")
                        elif a == "--..":
                                m.append("Z")
                        elif a == ".----":
                                m.append("1")
                        elif a == "..---":
                                m.append("2")
                        elif a == "...--":
                                m.append("3")
                        elif a == "....-":
                                m.append("4")
                        elif a == ".....":
                                m.append("5")
                        elif a == "-....":
                                m.append("6")
                        elif a == "--...":
                                m.append("7")
                        elif a == "---..":
                                m.append("8")
                        elif a == "----.":
                                m.append("9")
                        elif a == "-----":
                                m.append("0")
                        else:
                            err.append(a)
                if len(err)>0:
                    prob= str(err)+ ' is not understable I guess its not a morse code please input morse code. Sorry.'
                    messagebox.showinfo("Info", prob)
                dtxt = ""
                for t in m:
                        dtxt = dtxt+t
                ent.delete("1.0", END)
                ent.insert(INSERT, dtxt)


def loading():
    global num, dis, s
    mc=".-.. --- .- -.. .. -. --."
    list1 = list(mc)
    run()
    if num==0:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==1:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==2:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==3:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==4:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==5:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==6:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==7:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==8:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==9:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==10:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==11:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==12:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==13:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==14:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==15:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==16:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==17:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==18:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==19:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==20:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==21:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==22:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==23:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==24:
        dis =dis + list1[num]
        s.config(text=dis)
        num+=1
    elif num==25:
        dis=""
        s.config(text="")
        for i in win.winfo_children():
                i.destroy()
        gui(win)
    

def run():
        global s
        stop1=s.after(150, loading)
                
def page6(win):
        global s
        myfonti = font.Font(family="Courier", size=13, weight="bold")
        myfontf = font.Font(family="Courier", size=7, weight="bold")
        Label(win, image=bg34).grid(row=0,column=0,rowspan=4)
        s= Label(win,text="L  o  a  d  i  n  g", fg="cyan",bg="black",font=myfonti)
        s.grid(row=2, column=0)
        s= Label(win,text="", fg="cyan",bg="black",font=myfonti)
        s.grid(row=2, column=0)
        fact=Label(win, text="Fact:\n... --- ... = SOS\nwhich means Save Our SHIP", fg="white",bg="black", font=myfonti)
        fact.grid(row=3, column=0, sticky='s', pady=10)
        loading()
        win.unbind("<KeyPress>")
        


num1=0
wp=PhotoImage(file="1.png")
wp1=PhotoImage(file="9.png")
wp2=PhotoImage(file="2.png")
wp3=PhotoImage(file="3.png")
wp4=PhotoImage(file="4.png")
wp5=PhotoImage(file="5.png")
wp6=PhotoImage(file="6.png")
wp7=PhotoImage(file="7.png")
wp8=PhotoImage(file="8.png")
wp9=PhotoImage(file="9.png")
bgtabc=PhotoImage(file="Op12.png")
bgmcod=PhotoImage(file="logo.png")

def Tapbutton():
        for i in win.winfo_children():
                i.destroy()

        page3(win)
def mcoder():
        for i in win.winfo_children():
                i.destroy()
        page6(win)
def time():
        global timeup
        timestring= strftime('%H:%M:%S')
        timeup.config(text=timestring)
        timeup.after(1000, time)
        
def page7(win):
        global wp, wp1, num1, timeup, usr12, num, s
        num=0
        myfontos1=font.Font(family="alternate sans", size=6, weight="bold")
        Label(win, text="", image=wp).grid(row=0, column=0,rowspan=6,columnspan=4)
        timeup= Label(win,font=('Courier', 9, 'bold'))
        timeup.grid(row=0, column=0,sticky='nw')
        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
        time()
        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
        Tc.grid(row=0, column=0, padx=5)
        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
        mcod.grid(row=0, column=1)
        win.bind("<KeyPress>", changewp)                    
                        


def changewp(e):
                global num1, timeup
                myfontos1=font.Font(family="alternate sans", size=6, weight="bold")
                if num1==0:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp1).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)

                        
                elif num1==1:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp2).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)
                elif num1==2:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        
                        Label(win, text="", image=wp3).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()            
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)

                elif num1==3:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()

                        Label(win, text="", image=wp4).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)
                elif num1==4:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp5).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)

                        
                elif num1==5:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp6).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)
                        
                elif num1==6:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp7).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)
                elif num1==7:
                        num1+=1
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp8).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)
                else:
                        num1=0
                        for i in win.winfo_children():
                                i.destroy()
                        Label(win, text="", image=wp).grid(row=0, column=0,rowspan=6,columnspan=4)
                        timeup= Label(win,font=('Courier', 9, 'bold'))
                        timeup.grid(row=0, column=0,sticky='nw')
                        tk.Button(win, text="[->", font=('Courier', 9, 'bold'), command=cpg1).grid(row=0, column=3, sticky='ne')
                        time()
                        Tc = Button(win, text="Table Calculator",image=bgtabc,compound=TOP ,font=myfontos1, command=Tapbutton)
                        Tc.grid(row=0, column=0, padx=5)
                        mcod = Button(win, text="Morse code",image=bgmcod,compound=TOP ,font=myfontos1, command=mcoder)
                        mcod.grid(row=0, column=1)

def changepage():
        global pagenum, win
        for widget in win.winfo_children():
                widget.destroy()
        if pagenum == 1:
                page2(win)
                pagenum = 2
        elif pagenum==2:
                page1(win)
                pagenum = 1
        elif pagenum==3:
                page3(win)
                pagenum=2
        elif pagenum==4:
                page4(win)
                pagenum=2
        elif pagenum==5:
                page5(win)
                pagenum=2
        elif pagenum==6:
                page6(win)
                pagenum=2
        elif pagenum==7:
                page7(win)
                pagenum=2

        
page1(win)
win.mainloop()
