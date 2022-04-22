import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import teacher
import configparser
import login


class Tatt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700,
                        bg='#FFFFFF', bd=0, highlightthickness=0)

        canvas.pack(fill=BOTH, expand=True)
        config_obj = configparser.ConfigParser()
        config_obj.read("configfile.ini")
        info = config_obj["info"]
        teacher_name = info["teacher_name"]
        canvas.create_rectangle(
                0, 0, 1200, 80, fill='#FFC331', outline='white')
        conn = connect()
        cur = conn.cursor()
        query5 = 'SELECT  name FROM public."teacherData" where roll =\''+str(teacher_name)+'\' ;'
        cur.execute(query5)
        nama = cur.fetchone()
        user_label = Label(self, text="Welcome, "+ str(nama[0]), font=(
            "Ariel 20 bold"),bg='#FFC331', fg='White')
        canvas.create_window(50, 25, anchor="nw", window=user_label)
        logout = Button(self, text="Log In", font=("Ariel 22 bold"),
                       width=6, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(login.login))
        canvas.create_window(950, 15, anchor="nw", window=logout)

        def get_att():
            conn = connect()
            cur = conn.cursor()
            query1 = 'SELECT roll,attendance from public."attend" where course =\''+menu1.get() +'\';'
            query2 = 'SELECT stuid, att FROM public."meetingatt" where id=\'' + menu.get()[1:-2]+'\';'
            if menu1.get() == "Select course" and menu.get() == "Select meeting":
                messagebox.showinfo("Attendance System",
                                    'please select a option')
            elif menu1.get() == "Select course":
                print("Please select")
                cur.execute(query2)
                data2 = cur.fetchall()
            else:
                print("Please select1")
                cur.execute(query1)
                data1 = cur.fetchall()
        
        conn = connect()
        cur = conn.cursor()
        query3 = 'SELECT id FROM public."meeting" where organiser=\''+teacher_name+'\';'
        query4 = 'SELECT course FROM public."teacherData" where roll=\''+teacher_name+'\';'
        print(query3)
        cur.execute(query3)
        data3 = cur.fetchall()
        print(query4)
        cur.execute(query4)
        data4 = cur.fetchone()
        print(data3)
        print(data4)
        menu = StringVar()
        menu.set("Select meeting")
        drop = OptionMenu(self, menu, *data3)
        canvas.create_window(100, 120, anchor="nw", window=drop)
        menu1 = StringVar()
        menu1.set("Select course")
        drop1 = OptionMenu(self, menu1, *data4[0])
        canvas.create_window(400, 120, anchor="nw", window=drop1)
        canvas.create_rectangle(
            50, 180, 1150, 500, fill='white', outline='black')

        att = Button(self, text="Attendance Summary", font=("Ariel 22 bold"),
                     width=20, bg="white", fg='#FFC331', relief=FLAT, command=get_att)
        canvas.create_window(640, 110, anchor="nw", window=att)
        dash = Button(self, text="Dashboard", font=("Ariel 22 bold"),
                      width=10, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(teacher.teacher))
        canvas.create_window(500, 590, anchor="nw", window=dash)
