import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import student
import configparser
import login


class stuatt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700,
                        bg='#FFFFFF', bd=0, highlightthickness=0)

        canvas.pack(fill=BOTH, expand=True)
        config_obj = configparser.ConfigParser()
        config_obj.read("configfile.ini")
        info = config_obj["info"]
        student_name = info["student_name"]
        canvas.create_rectangle(
                0, 0, 1200, 80, fill='#FFC331', outline='white')
        conn = connect()
        cur = conn.cursor()
        query5 = 'SELECT  name,branch FROM public."studentData" where roll =\''+str(student_name)+'\' ;'
        cur.execute(query5)
        nama = cur.fetchone()
        user_label = Label(self, text="Welcome, "+ str(nama[0]), font=(
            "Ariel 20 bold"),bg='#FFC331', fg='White')
        canvas.create_window(50, 25, anchor="nw", window=user_label)
        logout = Button(self, text="Log Out", font=("Ariel 22 bold"),
                       width=6, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(login.login))
        canvas.create_window(950, 15, anchor="nw", window=logout)

        def get_att():
            query1 = 'SELECT course,attendance from public."attend" where roll =\''+str(student_name)+'\';'
            conn = connect()
            cur = conn.cursor()
            cur.execute(query1)
            data1 = cur.fetchall()
            user_label1 = Label(self, text="Student RollNo.", font=(
                    "Ariel 12 bold"),bg='white', fg='black')
            canvas.create_window(80, 200,width=350, height=20, anchor="nw", window=user_label1)
            user_label2 = Label(self, text="Attendance", font=(
                "Ariel 12 bold"),bg='white', fg='black')
            canvas.create_window(430, 200,width=350, height=20, anchor="nw", window=user_label2)
            user_label3 = Label(self, text="Total Classes", font=(
                "Ariel 12 bold"),bg='white', fg='black')
            canvas.create_window(780, 200,width=350, height=20, anchor="nw", window=user_label3)
            l=40
            t=200
            for i in range (len(data1)):
                t=t+l
                user_label5 = Label(self, text=data1[i][0], font=(
                    "Ariel 12"),bg='white', fg='black')
                canvas.create_window(80, t,width=350, height=20, anchor="nw", window=user_label5)
                user_label4 = Label(self, text=data1[i][1],  font=(
                    "Ariel 12"),bg='white', fg='black')
                canvas.create_window(430, t,width=350, height=20, anchor="nw", window=user_label4)
                query2 = 'select count(course) from public.meeting where sec=\''+str(nama[1])+'\' and course=\''+str(data1[i][0])+'\';'
                print(query2)
                cur.execute(query2)
                set = cur.fetchone()
                print(set)
                user_label6 = Label(self, text=str(set[0]),  font=(
                    "Ariel 12"),bg='white', fg='black')
                canvas.create_window(780, t,width=350, height=20, anchor="nw", window=user_label6)
        canvas.create_rectangle(
            50, 180, 1150, 500, fill='white', outline='black')

        att = Button(self, text="Attendance Summary", font=("Ariel 22 bold"),
                     width=20, bg="white", fg='#FFC331', relief=FLAT, command=get_att)
        canvas.create_window(380, 110, anchor="nw", window=att)
        dash = Button(self, text="Dashboard", font=("Ariel 22 bold"),
                      width=10, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(student.student))
        canvas.create_window(500, 590, anchor="nw", window=dash)
