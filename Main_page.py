from tkinter import *
import datetime
import os
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import json
import tkinter.ttk as ttk
import tkinter.font as tkfont


date = datetime.datetime.now().date()
date = str(date)

with open('theme.json', 'r') as file:
    json_data = json.load(file)
    main_bg_color = json_data['theme']['main_bg_color']
    bg_color = json_data['theme']['bg_color']
    fg_color = json_data['theme']['fg_color']
    title_bar_color = json_data['theme']['title_bar_color']

with open('database_info.json', 'r') as file:
    json_database = json.load(file)
    database_host = json_database['database_info']['host']
    database_port = json_database['database_info']['port']
    database_username = json_database['database_info']['username']
    database_password = json_database['database_info']['password']
    database_name01 = json_database['database_info']['database01']


def return_text_size(txt, family="arial", size=15, weight="bold"):
    font = tkfont.Font(family=family, size=size, weight=weight)
    size = font.measure(txt)

    return int(size)


class Main:
    def __init__(self):
        self.main_gui()
        # self.Admin()

    def main_gui(self):
        self.master = Tk()
        winsize = (self.master.winfo_screenwidth(),
                   self.master.winfo_screenheight())
        self.master.geometry(
            f"600x580+{int(winsize[0]/2)-300}+{int(winsize[1]/2)-290}")
        self.master.resizable(height=0, width=0)

        self.top = Frame(self.master, height=140, bg=title_bar_color)
        self.top.pack(fill=X)

        self.bottom = Frame(self.master, height=530, bg=main_bg_color)
        self.bottom.pack(fill=X)

        # top Frame design
        self.top_image = PhotoImage(file='icon/money.png')
        self.top_image_lable = Label(
            self.top, image=self.top_image, bg=bg_color)
        self.top_image_lable.place(x=70, y=15)
        self.top_image2 = PhotoImage(file='icon/money.png')
        self.top_image2_lable = Label(
            self.top, image=self.top_image, bg=bg_color)
        self.top_image2_lable.place(x=480, y=15)
        self.heading = Label(
            self.top, text="Bank Management System", font="arial 15 bold", bg=bg_color)
        self.heading.place(x=180, y=30)
        self.heading = Label(self.top, text="LOGIN",
                             font="arial 19 bold", bg=bg_color)
        self.heading.place(x=270, y=90)
        self.date_lbl = Label(
            self.bottom, text="Date : "+date, bg=main_bg_color)
        self.date_lbl.place(x=500, y=20)

        # Lable and Enteries
        self.user_lbl = Label(self.bottom, text="Username : ",
                              bg=main_bg_color, font="arial 15 bold")
        self.user_lbl.place(x=90, y=100)
        self.pass_lbl = Label(self.bottom, text="Password : ",
                              bg=main_bg_color, font="arial 15 bold")
        self.pass_lbl.place(x=90, y=180)
        self.e_user = Entry(self.bottom, width="40")
        self.e_user.place(x=240, y=105)
        self.e_pass = Entry(self.bottom, width="40", show="*")
        self.e_pass.place(x=240, y=185)
        self.i = StringVar()
        self.i.set("1")
        Radiobutton(self.bottom, text="Administrator",  value="1",
                    bg=main_bg_color, variable=self.i).place(x=125, y=260)
        Radiobutton(self.bottom, text="Bank Staff",  value="2",
                    bg=main_bg_color, variable=self.i).place(x=255, y=260)
        Radiobutton(self.bottom, text="Customer",  value="3",
                    bg=main_bg_color, variable=self.i).place(x=375, y=260)
        # submit
        self.submit = Button(self.bottom, text=" Submit ",
                             font="arial 15 bold", width="30", command=self.sub)
        self.submit.place(x=105, y=335)
        self.master.mainloop()
    

    def quit(self):
        self.master.destroy()


    # def sub(self):
    #     self.usr_type = self.i.get()
    #     self.usr_username = self.e_user.get()
    #     self.usr_passward = self.e_pass.get()

    #     print(self.usr_type, self.usr_username, self.usr_passward)
    #     self.master.destroy()
    #     if self.usr_type == "1":
    #         adm = Admin()
    #         adm.Admin_("Administrator")
            
    #     elif self.usr_type == "2":
    #         man = Manager()
        
    #     elif self.usr_type == "3":
    #         user = EndUser()

    def sub(self):
        user = self.e_user.get()
        passw = self.e_pass.get()
        mode = self.i.get()
        if (user == "" or passw == ""):
            MessageBox.showinfo(
                "Illegal insert", "All Fields are Required")
        else:
            if (mode == "1"):
                if (user == "Admin" and passw == "Admin"):
                    # MessageBox.showinfo("Sucessful", "Welcome Admin")
                    self.quit()
                    adm = Admin()
                    adm.Admin_("Administrator")
                    
                else:
                    MessageBox.showinfo(
                        "Illegal insert", "Username or Password Is Wrong")

            elif(mode == "2"):
                con = mysql.connect(
                host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select * from mgmt where managerid='" + user + "'")
                myresult = cursor.fetchall()

                for x in myresult:
                    uchk = x[0]
                    pchk = x[1]
                    if (user == uchk and passw == pchk):
                        # MessageBox.showinfo("Sucessful", "Welcome Management Staff")
                        self.quit()
                        man = Manager()
                    else:
                        MessageBox.showinfo("Illegal insert", "Username or Password Is Wrong")
                con.close()

            
            elif(mode == "3"):
                con = mysql.connect(host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select * from users where idusers='" + user + "'")
                myresult = cursor.fetchall()
                for x in myresult:
                    uchk = x[0]
                    pchk = x[1]
                    if (user == uchk and passw == pchk):
                        # MessageBox.showinfo("Sucessful", "Welcome Customer")
                        self.quit()
                        user = EndUser()

                    else:
                        MessageBox.showinfo("Illegal insert", "Username or Password Is Wrong")


class Admin:

    def __init__(self) -> None:
        pass

    def Admin_(self,userTitle,adminBtn = True):
        try:
            self.Admin_windo = Tk()
        except:
            self.Admin_windo = Toplevel()

        self.Admin_windo.title(userTitle)
        self.Admin_windo.geometry(
            f"{self.Admin_windo.winfo_screenwidth()}x{self.Admin_windo.winfo_screenheight()}+0+0")
        windo_width = int(self.Admin_windo.winfo_screenwidth())
        windo_height = int(self.Admin_windo.winfo_screenheight())

        self.top = Frame(self.Admin_windo, height=100, bg=title_bar_color)
        self.top.pack(fill=X)

        # creating top frame
        self.top_image = PhotoImage(file='icon/money.png')
        self.top_image_lable = Label(self.top, image=self.top_image, bg=bg_color)
        self.top_image_lable.place(x=0, y=15)

        self.top_image2_lable = Label(
            self.top, image=self.top_image, bg=bg_color)
        self.top_image2_lable.place(
            x=int(self.Admin_windo.winfo_screenwidth()-self.top_image.width()), y=15)

        self.heading = Label(
            self.top, text="Bank Management System", font="arial 15 bold", bg=bg_color)
        self.heading.place(
            x=windo_width/2 - return_text_size(self.heading['text'], self.heading['font'])/2, y=30)

        self.heading_name = Label(
            self.top, text=userTitle, font="arial 19 bold", bg=bg_color)
        self.heading_name.place(x=windo_width/2 - return_text_size(
            self.heading_name['text'], self.heading_name['font'])/2, y=60)

        # frame for btn
        self.btn_frame = Frame(self.Admin_windo, height=50, bg=title_bar_color)
        self.btn_frame.pack(pady=10)

        self.createAccountButton = Button(
            self.btn_frame, text="Create Account", width=20, bg=bg_color, command=self.createAccount)
        self.createAccountButton.grid(row=0, padx=5, column=0)

        self.balanceEnquiry1 = Button(
            self.btn_frame, text="Balance Enquiry",  width=20, bg=bg_color, command=self.balanceEnquiry)
        self.balanceEnquiry1.grid(row=0, padx=5, column=2)

        self.checkAccountDetails1 = Button(
            self.btn_frame, text="Check Account Details",  width=20, bg=bg_color, command=self.checkAccountDetails)
        self.checkAccountDetails1.grid(row=0, padx=5, column=3)

        self.balanceWithdraw1 = Button(
            self.btn_frame, text="Balance Withdraw",  width=20, bg=bg_color, command=self.balanceWithdraw)
        self.balanceWithdraw1.grid(row=0, padx=5, column=4)

        self.balanceDeposit1 = Button(
            self.btn_frame, text="Balance Deposit",  width=20, bg=bg_color,command=self.balanceDeposit)
        self.balanceDeposit1.grid(row=0, padx=5, column=5)

        self.deleteAccount1 = Button(
            self.btn_frame, text="Delete Account",  width=20, bg=bg_color,command=self.deleteAccount)
        self.deleteAccount1.grid(row=0, padx=5, column=6)

        self.updateAccount1 = Button(
            self.btn_frame, text="Update Account",  width=20, bg=bg_color,command=self.updateAccount)
        self.updateAccount1.grid(row=0, padx=5, column=7)

        if adminBtn:
            self.userAdministration1 = Button(
            self.btn_frame, text="User Administration",  width=20, bg=bg_color,command=self.userAdministration)
            self.userAdministration1.grid(row=0, padx=5, column=8)

        self.bodyFrame = Frame(self.Admin_windo, height=windo_height, bg=title_bar_color)
        self.bodyFrame.pack(fill=BOTH)

        self.createAccount()


        self.Admin_windo.mainloop()
    
    def ActiveButton(self,btn):
        try:
            btn_list = [self.createAccountButton,self.balanceEnquiry1,self.checkAccountDetails1,self.balanceWithdraw1,self.balanceDeposit1,self.deleteAccount1,self.updateAccount1,self.userAdministration1]
        except:btn_list = [self.createAccountButton,self.balanceEnquiry1,self.checkAccountDetails1,self.balanceWithdraw1,self.balanceDeposit1,self.deleteAccount1,self.updateAccount1]


        for i in range(0,len(btn_list)):
            try:
                if i == btn:
                    btn_list[i].config(bg=main_bg_color) 
                else:
                    btn_list[i].config(bg=bg_color) 
 
            except:
                pass
                


    def createAccount(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()
        
        # self.createAccountButton.config(bg=main_bg_color,fg=fg_color)
        self.ActiveButton(0)
        

        def sub():
            acc_no = DoubleVar()
            amount = DoubleVar()
            phone_no = DoubleVar()
            acc_no = (e_acc_no.get())
            fname = (e_fname.get())
            lname = (e_lname.get())
            d_ob = (e_d_ob.get())
            s_c = (t.get())
            amount = (e_amount.get())
            address = (e_address.get())
            phone_no = (e_phone_no.get())
            m_f_t = (i.get())

            if (acc_no == "" or fname == "" or s_c == "" or amount == "" or address == "" or phone_no == "" or m_f_t == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                try:
                    con = mysql.connect(
                        host=database_host, user=database_username, password=database_password, database=database_name01)
                    cursor = con.cursor()
                    cursor.execute("insert into acct values('" + acc_no + "','" + fname + "','" + lname + "','" + d_ob +
                                   "', '" + s_c + "','" + amount + "' , '" + address + "','" + phone_no + "', '" + m_f_t + "')")
                    cursor.execute("insert into users values('" +
                                   acc_no + "','" + phone_no + "')")
                    cursor.execute("commit")
                    MessageBox.showinfo("Insert Status", "Inserted Successfully")
                    e_fname.delete(0, 'end')
                    e_lname.delete(0, 'end')
                    e_amount.delete(0, 'end')
                    e_address.delete(0, 'end')
                    e_phone_no.delete(0, 'end')
                    e_d_ob.delete(0, 'end')
                    con.close()

                    # MessageBox.showinfo("success","Accont Created Successfully")
                
                except Exception as e:
                    MessageBox.showerror("Error",e)

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=BOTH)

        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        fname = Label(bottom, text="First Name ",
                      font="arial 14 bold", bg=main_bg_color)
        fname.place(x=40, y=110)

        lname = Label(bottom, text="Last Name ",
                      font="arial 14 bold", bg=main_bg_color)
        lname.place(x=40, y=165)

        s_c = Label(bottom, text="Account Type ",
                    font="arial 14 bold", bg=main_bg_color)
        s_c.place(x=40, y=220)

        amount = DoubleVar()
        amount = Label(bottom, text="Initial Amount ",
                       font="arial 14 bold", bg=main_bg_color)
        amount.place(x=40, y=275)

        address = Label(bottom, text="Address ",
                        font="arial 14 bold", bg=main_bg_color)
        address.place(x=40, y=330)

        phone_no = DoubleVar()
        phone_no = Label(bottom, text="Phone Number ",
                         font="arial 14 bold", bg=main_bg_color)
        phone_no.place(x=40, y=385)

        m_f_t = Label(bottom, text="Sex ",
                      font="arial 14 bold", bg=main_bg_color)
        m_f_t.place(x=40, y=440)

        d_ob = Label(bottom, text="Date of Birth ",
                     font="arial 14 bold", bg=main_bg_color)
        d_ob.place(x=40, y=495)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        e_fname = Entry(bottom, width="60")
        e_fname.place(x=320, y=110)

        e_lname = Entry(bottom, width="60")
        e_lname.place(x=320, y=165)

        t = StringVar()
        t.set("S")
        Radiobutton(bottom, text="Savings Account",  value="S",
                    bg=main_bg_color, variable=t).place(x=320, y=220)
        Radiobutton(bottom, text="Current Account",  value="C",
                    bg=main_bg_color, variable=t).place(x=450, y=220)

        e_amount = Entry(bottom, width="60")
        e_amount.place(x=320, y=275)

        e_address = Entry(bottom, width="60")
        e_address.place(x=320, y=330)

        e_phone_no = Entry(bottom, width="60")
        e_phone_no.place(x=320, y=385)

        i = StringVar()
        i.set("M")
        Radiobutton(bottom, text="Male",  value="M",
                    bg=main_bg_color, variable=i).place(x=320, y=440)
        Radiobutton(bottom, text="Female",  value="F",
                    bg=main_bg_color, variable=i).place(x=430, y=440)
        Radiobutton(bottom, text="Transgender",  value="T",
                    bg=main_bg_color, variable=i).place(x=540, y=440)

        e_d_ob = Entry(bottom, width="60")
        e_d_ob.place(x=320, y=495)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="30", command=sub)
        self.submit.place(x=320, y=550)
        

    def balanceEnquiry(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()
        
        self.ActiveButton(1)

        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                    lb.insert(0, x)
                cursor.execute("commit")
                con.close()

        # frames

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        detail = Label(bottom, text="Details -> ",
                       font="arial 14 bold", bg=main_bg_color)
        detail.place(x=40, y=110)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        # list
        lb = Entry(bottom, width="60")
        lb.place(x=320, y=110)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="52", command=sub)
        self.submit.place(x=45, y=200)


    def checkAccountDetails(self):

        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(2)
        
        
        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select * from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                print(myresult)
                for x in myresult:
                    e_fname.insert(0, x[1])
                    e_lname.insert(0, x[2])
                    e_dob.insert(0, x[3])
                    e_s_c.insert(0, x[4])
                    e_amount.insert(0, x[5])
                    e_address.insert(0, x[6])
                    e_phone_no.insert(0, x[7])
                    e_m_f_t.insert(0, x[8])

                cursor.execute("commit")
                con.close()

        # frames

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        fname = Label(bottom, text="First Name ",
                      font="arial 14 bold", bg=main_bg_color)
        fname.place(x=40, y=110)

        lname = Label(bottom, text="Last Name ",
                      font="arial 14 bold", bg=main_bg_color)
        lname.place(x=40, y=165)

        dob = Label(bottom, text="Date of Birth ",
                    font="arial 14 bold", bg=main_bg_color)
        dob.place(x=40, y=220)

        s_c = Label(bottom, text="Account Type ",
                    font="arial 14 bold", bg=main_bg_color)
        s_c.place(x=40, y=275)

        amount = DoubleVar()
        amount = Label(bottom, text="Initial Amount ",
                       font="arial 14 bold", bg=main_bg_color)
        amount.place(x=40, y=330)

        address = Label(bottom, text="Address ",
                        font="arial 14 bold", bg=main_bg_color)
        address.place(x=40, y=385)

        phone_no = DoubleVar()
        phone_no = Label(bottom, text="Phone Number ",
                         font="arial 14 bold", bg=main_bg_color)
        phone_no.place(x=40, y=440)

        m_f_t = Label(bottom, text="Sex ",
                      font="arial 14 bold", bg=main_bg_color)
        m_f_t.place(x=40, y=495)

        # Enteries

        e_acc_no = Entry(bottom, width="40")
        e_acc_no.place(x=320, y=55)

        e_fname = Entry(bottom, width="40")
        e_fname.place(x=320, y=110)

        e_lname = Entry(bottom, width="40")
        e_lname.place(x=320, y=165)

        e_dob = Entry(bottom, width="40")
        e_dob.place(x=320, y=220)

        e_s_c = Entry(bottom, width="40")
        e_s_c.place(x=320, y=275)

        e_amount = Entry(bottom, width="40")
        e_amount.place(x=320, y=330)

        e_address = Entry(bottom, width="40")
        e_address.place(x=320, y=385)

        e_phone_no = Entry(bottom, width="40")
        e_phone_no.place(x=320, y=440)

        e_m_f_t = Entry(bottom, width="40")
        e_m_f_t.place(x=320, y=495)

        # Enteries

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="10", command=sub)
        self.submit.place(x=600, y=55)


    def balanceWithdraw(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(3)


        
        def upd():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())
            if (acc_no == ""):
                MessageBox.showinfo(
                    "ID is required for delete", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresul = cursor.fetchall()
                for x in myresul:
                    print(x)
                    fb.insert(0, x)
                cursor.execute("commit")
                MessageBox.showinfo("Update Status", "Withdrawn Successfully")
                con.close()

        def dept():
            amtn = dp.get()
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())
            con = mysql.connect(host=database_host, user=database_username,
                                password=database_password, database=database_name01)
            cursor = con.cursor()
            cursor.execute("update acct set amount= amount - ('" +
                           amtn + "') where acc_no='" + acc_no + "'")
            cursor.execute("commit")
            con.close()
            upd()

        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                    lb.insert(0, x)
                cursor.execute("commit")
                con.close()

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        detail = Label(bottom, text="Current Balance ",
                       font="arial 14 bold", bg=main_bg_color)
        detail.place(x=40, y=110)

        amt = Label(bottom, text="Amount ",
                    font="arial 14 bold", bg=main_bg_color)
        amt.place(x=40, y=165)

        upb = Label(bottom, text="Updated Balance ",
                    font="arial 14 bold", bg=main_bg_color)
        upb.place(x=40, y=220)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        lb = Entry(bottom, width="60")
        lb.place(x=320, y=110)

        dp = Entry(bottom, width="60")
        dp.place(x=320, y=165)

        fb = Entry(bottom, width="60")
        fb.place(x=320, y=220)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="52", command=sub)
        self.submit.place(x=45, y=270)

        self.dep = Button(bottom, text=" Withdraw ",
                          font="arial 15 bold", width="52", command=dept)
        self.dep.place(x=45, y=330)


    def balanceDeposit(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(4)
        
        
        def upd():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())
            if (acc_no == ""):
                MessageBox.showinfo(
                    "ID is required for delete", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresul = cursor.fetchall()
                for x in myresul:
                    print(x)
                    fb.insert(0, x)
                cursor.execute("commit")
                MessageBox.showinfo("Update Status", "Deposited Successfully")
                con.close()

        def dept():
            amtn = dp.get()
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())
            if (acc_no == ""):
                MessageBox.showinfo(
                    "ID is required for delete", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute("update acct set amount= amount + ('" +
                               amtn + "') where acc_no='" + acc_no + "'")
                cursor.execute("commit")
                con.close()
                upd()

        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                    lb.insert(0, x)
                cursor.execute("commit")
                con.close()

        # frames

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        detail = Label(bottom, text="Current Balance ",
                       font="arial 14 bold", bg=main_bg_color)
        detail.place(x=40, y=110)

        amt = Label(bottom, text="Amount ",
                    font="arial 14 bold", bg=main_bg_color)
        amt.place(x=40, y=165)

        upb = Label(bottom, text="Updated Balance ",
                    font="arial 14 bold", bg=main_bg_color)
        upb.place(x=40, y=220)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        lb = Entry(bottom, width="60")
        lb.place(x=320, y=110)

        dp = Entry(bottom, width="60")
        dp.place(x=320, y=165)

        fb = Entry(bottom, width="60")
        fb.place(x=320, y=220)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="52", command=sub)
        self.submit.place(x=45, y=270)

        self.dep = Button(bottom, text=" Deposit ",
                          font="arial 15 bold", width="52", command=dept)
        self.dep.place(x=45, y=330)


    def deleteAccount(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(5)
        


        def delti():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "ID is required for delete", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "delete from acct where acc_no='" + acc_no + "'")
                cursor.execute("commit")
                lb.delete(1, 'end')
                lb.delete(2, 'end')
                lb.delete(3, 'end')
                lb.delete(4, 'end')
                lb.delete(5, 'end')
                lb.delete(6, 'end')
                lb.delete(7, 'end')
                lb.delete(8, 'end')
                lb.delete(9, 'end')
                lb.delete(10, 'end')
                lb.delete(11, 'end')
                lb.delete(12, 'end')
                lb.delete(13, 'end')
                lb.delete(14, 'end')
                e_acc_no.delete(0, 'end')
                MessageBox.showinfo("Delete Status", "Deleted Successfully")
                con.close()

        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select * from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                print(myresult)
                for x in myresult:
                    lb.insert(1, "Account No. :")
                    lb.insert(2, x[0])
                    lb.insert(3, "Name :")
                    lb.insert(4, x[1] + " " + x[2])
                    lb.insert(5, "Account Type :")
                    lb.insert(6, x[3])
                    lb.insert(7, "Amount :")
                    lb.insert(8, x[4])
                    lb.insert(9, "Address :")
                    lb.insert(10, x[5])
                    lb.insert(11, "Phone No. :")
                    lb.insert(12, x[6])
                    lb.insert(13, "Sex")
                    lb.insert(14, x[7])

                cursor.execute("commit")
                con.close()

        # frames


        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        detail = Label(bottom, text="Details -> ",
                       font="arial 14 bold", bg=main_bg_color)
        detail.place(x=40, y=110)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        # list
        lb = Listbox(bottom, height="50", width="60")
        lb.place(x=320, y=110)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="20", command=sub)
        self.submit.place(x=45, y=200)

        self.delt = Button(bottom, text=" Delete ",
                           font="arial 15 bold", width="20", command=delti)
        self.delt.place(x=45, y=300)


    def updateAccount(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(6)

        def search():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select * from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                print(myresult)
                for x in myresult:
                    e_fname.insert(0, x[1])
                    e_lname.insert(0, x[2])
                    e_d_ob.insert(0, x[3])
                    e_s_c.insert(0, x[4])
                    e_amount.insert(0, x[5])
                    e_address.insert(0, x[6])
                    e_phone_no.insert(0, x[7])
                    e_m_f_t.insert(0, x[8])

                cursor.execute("commit")
                con.close()
        


        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute("update acct set fname= '" + e_fname.get() + "' ,lname= '" + e_lname.get() + "',d_ob= '" + e_d_ob.get() + "' , s_c= '" + e_s_c.get() + "' , amount= '" +
                               e_amount.get() + "',address= '" + e_address.get() + "' , phone_no= '" + e_phone_no.get() + "' ,m_f_t= '" + e_m_f_t.get() + "'  where acc_no='" + acc_no + "'")
                MessageBox.showinfo("Update status", "Updated Sucessfully")
                cursor.execute("commit")
                con.close()

        # frames

        bottom = Frame(self.bodyFrame, height=900, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=40)

        fname = Label(bottom, text="First Name ",
                      font="arial 14 bold", bg=main_bg_color)
        fname.place(x=40, y=95)

        lname = Label(bottom, text="Last Name ",
                      font="arial 14 bold", bg=main_bg_color)
        lname.place(x=40, y=150)

        s_c = Label(bottom, text="Account Type ",
                    font="arial 14 bold", bg=main_bg_color)
        s_c.place(x=40, y=205)

        amount = DoubleVar()
        amount = Label(bottom, text="New Amount ",
                       font="arial 14 bold", bg=main_bg_color)
        amount.place(x=40, y=260)

        address = Label(bottom, text="Address ",
                        font="arial 14 bold", bg=main_bg_color)
        address.place(x=40, y=315)

        phone_no = DoubleVar()
        phone_no = Label(bottom, text="Phone Number ",
                         font="arial 14 bold", bg=main_bg_color)
        phone_no.place(x=40, y=370)

        m_f_t = Label(bottom, text="Sex ", font="arial 14 bold", bg=main_bg_color)
        m_f_t.place(x=40, y=425)

        d_ob = Label(bottom, text="Date of Birth",
                     font="arial 14 bold", bg=main_bg_color)
        d_ob.place(x=40, y=475)

        # Enteries

        e_acc_no = Entry(bottom, width="40")
        e_acc_no.place(x=320, y=40)

        e_fname = Entry(bottom, width="40")
        e_fname.place(x=320, y=95)

        e_lname = Entry(bottom, width="40")
        e_lname.place(x=320, y=150)

        e_s_c = Entry(bottom, width="40")
        e_s_c.place(x=320, y=205)

        e_amount = Entry(bottom, width="40")
        e_amount.place(x=320, y=260)

        e_address = Entry(bottom, width="40")
        e_address.place(x=320, y=315)

        e_phone_no = Entry(bottom, width="40")
        e_phone_no.place(x=320, y=370)

        e_m_f_t = Entry(bottom, width="40")
        e_m_f_t.place(x=320, y=425)

        e_d_ob = Entry(bottom, width="40")
        e_d_ob.place(x=320, y=475)

        # Enteries

        # submit
        self.submit = Button(bottom, text="Search",
                             font="arial 15 bold", width="10", command=search)
        self.submit.place(x=600, y=55)

        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="10", command=sub)
        self.submit.place(x=600, y=200)



        
    
    def userAdministration(self):
        for child in self.bodyFrame.winfo_children():
            child.destroy()

        self.ActiveButton(7)
        

        def sub():
            user = StringVar()
            passw = StringVar()
            user = (e_user.get())
            passw = (e_pass.get())
            mode = (i.get())
            if (user == "" or passw == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                if (mode == "2"):
                    con = mysql.connect(
                        host=database_host, user=database_username, password=database_password, database=database_name01)
                    cursor = con.cursor()
                    cursor.execute(
                        "insert into mgmt values('" + user + "','" + passw + "')")
                    cursor.execute("commit")
                    MessageBox.showinfo(
                        "Insert Status", "User Created Sucessfully")
                else:
                    if (mode == "3"):
                        con = mysql.connect(
                            host=database_host, user=database_username, password=database_password, database=database_name01)
                        cursor = con.cursor()
                        cursor.execute(
                            "insert into users values('" + user + "','" + passw + "')")
                        cursor.execute("commit")
                        MessageBox.showinfo(
                            "Insert Status", "User Created Sucessfully")

        # frames
        bottom = Frame(self.bodyFrame, height=530, bg=main_bg_color)
        bottom.pack(fill=X)

        

        self.date_lbl = Label(bottom, text="Date : "+date, bg=main_bg_color)
        self.date_lbl.place(x=500, y=20)

        #Lable and Enteries
        self.user_lbl = Label(bottom, text="Username : ",
                              bg=main_bg_color, font="arial 15 bold")
        self.user_lbl.place(x=90, y=100)

        self.pass_lbl = Label(bottom, text="Password : ",
                              bg=main_bg_color, font="arial 15 bold")
        self.pass_lbl.place(x=90, y=180)

        e_user = Entry(bottom, width="40")
        e_user.place(x=240, y=105)

        e_pass = Entry(bottom, width="40")
        e_pass.place(x=240, y=185)

        i = StringVar()
        i.set("2")
        Radiobutton(bottom, text="Bank Staff",  value="2",
                    bg=main_bg_color, variable=i).place(x=175, y=260)
        Radiobutton(bottom, text="Customer",  value="3",
                    bg=main_bg_color, variable=i).place(x=345, y=260)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="30", command=sub)
        self.submit.place(x=105, y=335)


class Manager(Admin):
    def __init__(self) -> None:
        super().__init__()
        super().Admin_("Manager",False)

class EndUser:
    def __init__(self) -> None:
        self.Main_("Customer")

    def Main_(self,userTitle):
        self.customer_windo = Tk()
        self.customer_windo.title(userTitle)
        self.customer_windo.geometry(
            f"{self.customer_windo.winfo_screenwidth()}x{self.customer_windo.winfo_screenheight()}+0+0")
        windo_width = int(self.customer_windo.winfo_screenwidth())
        windo_height = int(self.customer_windo.winfo_screenheight())

        self.top1 = Frame(self.customer_windo, height=100, bg=title_bar_color)
        self.top1.pack(fill=X)

        # creating top frame
        self.top_image1 = PhotoImage(file='icon/money.png')
        self.top_image_lable1 = Label(self.top1, image=self.top_image1, bg=bg_color)
        self.top_image_lable1.place(x=0, y=15)

        self.top_image2_lable = Label(self.top1, image=self.top_image1, bg=bg_color)
        self.top_image2_lable.place(x=int(self.customer_windo.winfo_screenwidth()-self.top_image1.width()), y=15)

        self.heading = Label(self.top1, text="Bank Management System", font="arial 15 bold", bg=bg_color)
        self.heading.place(x=windo_width/2 - return_text_size(self.heading['text'], self.heading['font'])/2, y=30)

        self.heading_name = Label(self.top1, text=userTitle, font="arial 19 bold", bg=bg_color)
        self.heading_name.place(x=windo_width/2 - return_text_size(self.heading_name['text'], self.heading_name['font'])/2, y=60)

        

        def sub():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == ""):
                MessageBox.showinfo(
                    "Illegal insert", "All Fields are Required")
            else:
                con = mysql.connect(
                    host=database_host, user=database_username, password=database_password, database=database_name01)
                cursor = con.cursor()
                cursor.execute(
                    "select amount from acct where acc_no='" + acc_no + "'")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                    lb.insert(0, x)
                cursor.execute("commit")
                con.close()

        # frames
        self.bodyFrame = Frame(self.customer_windo, height=windo_height, bg=title_bar_color)
        self.bodyFrame.pack(fill=BOTH)

        bottom = Frame(self.bodyFrame, height=800, bg=main_bg_color)
        bottom.pack(fill=X)

        # bottom Frame Design

        #buttons and lables
        acc_no = DoubleVar()
        acc_no = Label(bottom, text="Account number ",
                       font="arial 14 bold", bg=main_bg_color)
        acc_no.place(x=40, y=55)

        detail = Label(bottom, text="Details -> ",
                       font="arial 14 bold", bg=main_bg_color)
        detail.place(x=40, y=110)

        # Enteries

        e_acc_no = Entry(bottom, width="60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        # list
        lb = Entry(bottom, width="60")
        lb.place(x=320, y=110)

        # submit
        self.submit = Button(bottom, text=" Submit ",
                             font="arial 15 bold", width="52", command=sub)
        self.submit.place(x=45, y=200)
        
        self.customer_windo.mainloop()


 
def main():
    app = Main()


if __name__ == "__main__":
    main()
