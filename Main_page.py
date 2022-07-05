from multiprocessing.sharedctypes import Value
from struct import pack
from tkinter import *
import datetime
import os
import tkinter.messagebox as MessageBox
from subprocess import call
from matplotlib.pyplot import margins
import mysql.connector as mysql
import json
import tkinter.ttk as ttk

import tkinter.font as tkfont


date = datetime.datetime.now().date()
date= str(date)

with open('theme.json','r') as file:
    json_data = json.load(file)
    main_bg_color = json_data['theme']['main_bg_color']
    bg_color =json_data['theme']['bg_color']
    fg_color = json_data['theme']['fg_color']
    title_bar_color = json_data['theme']['title_bar_color']

with open('database_info.json','r') as file:
    json_database = json.load(file)
    database_host = json_database['database_info']['host']
    database_port = json_database['database_info']['port']
    database_username = json_database['database_info']['username']
    database_password = json_database['database_info']['password']
    database_password = json_database['database_info']['password']
    database_database01 = json_database['database_info']['database01']


def return_text_size(txt,family="arial", size=15,weight="bold"):
    font = tkfont.Font(family=family, size=size, weight=weight) 
    size = font.measure(txt)
    
    return int(size)



class Main():
    def __init__(self):
        # self.main_gui()
        self.Admin()


    def main_gui(self):
        self.master = Tk()
        winsize = (self.master.winfo_screenwidth(),self.master.winfo_screenheight())
        self.master.geometry(f"600x580+{int(winsize[0]/2)-300}+{int(winsize[1]/2)-290}")
        self.master.resizable(height = 0, width = 0)

        self.top= Frame(self.master, height=140 , bg= title_bar_color)
        self.top.pack(fill=X)

        self.bottom= Frame(self.master, height=530, bg=main_bg_color)
        self.bottom.pack(fill=X)

        #top Frame design
        self.top_image=PhotoImage(file='icon/money.png')
        self.top_image_lable= Label(self.top, image=self.top_image, bg=bg_color)
        self.top_image_lable.place(x=70, y=15)
        self.top_image2=PhotoImage(file='icon/money.png')
        self.top_image2_lable= Label(self.top, image=self.top_image, bg=bg_color)
        self.top_image2_lable.place(x=480, y=15)
        self.heading= Label(self.top, text="Bank Management System", font="arial 15 bold", bg=bg_color)
        self.heading.place(x= 180, y=30)
        self.heading= Label(self.top, text="LOGIN", font="arial 19 bold", bg=bg_color)
        self.heading.place(x= 270, y=90)
        self.date_lbl = Label(self.bottom, text="Date : "+date, bg=main_bg_color)
        self.date_lbl.place(x=500, y=20)

        #Lable and Enteries
        self.user_lbl = Label(self.bottom, text="Username : ", bg=main_bg_color, font="arial 15 bold")
        self.user_lbl.place(x=90, y=100)
        self.pass_lbl = Label(self.bottom, text="Password : ", bg=main_bg_color, font="arial 15 bold")
        self.pass_lbl.place(x=90, y=180)
        self.e_user= Entry(self.bottom, width= "40")
        self.e_user.place(x=240, y=105)
        self.e_pass= Entry(self.bottom, width= "40", show="*")
        self.e_pass.place(x=240, y=185)
        self.i= StringVar()
        Radiobutton(self.bottom, text="Administrator",  value="1", bg=main_bg_color, variable=self.i).place(x=125, y=260)
        Radiobutton(self.bottom, text="Bank Staff",  value="2", bg=main_bg_color, variable=self.i).place(x=255, y=260)
        Radiobutton(self.bottom, text="Customer",  value="3", bg=main_bg_color, variable=self.i).place(x=375, y=260)
        # submit
        self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="30", command=self.sub)
        self.submit.place(x=105 , y=335)
        self.master.mainloop()

    
    def sub(self):
        self.usr_type = self.i.get()
        self.usr_username = self.e_user.get()
        self.usr_passward = self.e_pass.get()

        print(self.usr_type,self.usr_username,self.usr_passward)
        self.master.destroy()
        self.Admin()

    def Admin(self):
        self.Admin_windo = Tk()
        self.Admin_windo.title("Administration")
        self.Admin_windo.geometry(f"{self.Admin_windo.winfo_screenwidth()}x{self.Admin_windo.winfo_screenheight()}+0+0")
        windo_width = int(self.Admin_windo.winfo_screenwidth())
        windo_height =int(self.Admin_windo.winfo_screenheight())


        self.top= Frame(self.Admin_windo, height=100 , bg= title_bar_color)
        self.top.pack(fill=X)


        # creating top frame
        self.top_image=PhotoImage(file='icon/money.png')
        self.top_image_lable= Label(self.top, image=self.top_image, bg=bg_color)
        self.top_image_lable.place(x=0, y=15)

        self.top_image2_lable= Label(self.top, image=self.top_image, bg=bg_color)
        self.top_image2_lable.place(x=int(self.Admin_windo.winfo_screenwidth()-self.top_image.width()), y=15)

        
        self.heading = Label(self.top, text="Bank Management System", font="arial 15 bold", bg=bg_color)
        self.heading.place(x= windo_width/2 - return_text_size(self.heading['text'],self.heading['font'])/2, y=30)

        self.heading_name = Label(self.top, text="Administration", font="arial 19 bold", bg=bg_color)
        self.heading_name.place(x= windo_width/2 - return_text_size(self.heading_name['text'],self.heading_name['font'])/2, y=60)

        # frame for btn
        self.btn_frame = Frame(self.Admin_windo,height=50, bg=title_bar_color)
        self.btn_frame.pack(pady=10)

        self.createAccountButton = Button(self.btn_frame, text="Create Account", width=20, bg=bg_color) 
        self.createAccountButton.grid(row=0, padx=5,column=0)

        
        self.balanceEnquiry  = Button(self.btn_frame, text="Balance Enquiry",  width=20, bg=bg_color) 
        self.balanceEnquiry .grid(row=0, padx=5,column=2)


        self.checkAccountDetails = Button(self.btn_frame, text="Check Account Details",  width=20, bg=bg_color) 
        self.checkAccountDetails.grid(row=0, padx=5,column=3)

        self.balanceWithdraw = Button(self.btn_frame, text="Balance Withdraw",  width=20, bg=bg_color) 
        self.balanceWithdraw.grid(row=0, padx=5,column=4)


        self.balanceDeposit = Button(self.btn_frame, text="Balance Deposit",  width=20, bg=bg_color) 
        self.balanceDeposit.grid(row=0, padx=5,column=5)

        self.deleteAccount = Button(self.btn_frame, text="Delete Account",  width=20, bg=bg_color) 
        self.deleteAccount.grid(row=0, padx=5,column=6)

        self.updateAccount = Button(self.btn_frame, text="Update Account",  width=20, bg=bg_color) 
        self.updateAccount.grid(row=0, padx=5,column=7)

        self.Admin_windo.mainloop()




def main():
    app = Main()
    



if __name__ == "__main__":
    main()