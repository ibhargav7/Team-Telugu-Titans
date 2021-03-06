import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import time
import pyqrcode
import configparser
from stuatt import stuatt
import login

class student(tk.Frame):

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
        print(nama)
        user_label = Label(self, text="Welcome, "+ str(nama[0]), font=(
            "Ariel 20 bold"),bg='#FFC331', fg='White')
        canvas.create_window(50, 25, anchor="nw", window=user_label)
        logout = Button(self, text="Log Out", font=("Ariel 22 bold"),
                       width=6, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(login.login))
        canvas.create_window(950, 15, anchor="nw", window=logout)

        def generate_QR(str):
            qr = pyqrcode.create("http://localhost/meeting/" + str)
            img = BitmapImage(data=qr.xbm(scale=7))

            img_lbl = Label(self, image=img, bg='white')
            canvas.create_window(80, 200, anchor="nw", window=img_lbl)
            img_lbl.image = img
            img_lbl.place()

        def getTime():
            t = time.localtime()
            current_time = int(time.strftime("%H"+"%M", t))
            return current_time

        def get_meeting():
            

            print(student_name)

            meeting_label = Label(self, text="Ongoing Meeting", font=(
                "Ariel 20 bold"), bg='#503284', fg='white')
            canvas.create_window(80, 120, anchor="nw", window=meeting_label)
            canvas.create_rectangle(
                50, 180, 1150, 500, fill='white', outline='black')

            conn = connect()
            cur = conn.cursor()
            query = 'SELECT * from public."meeting" where start<=' + \
                str(getTime())+' and start+duration>'+str(getTime())+' and sec = \''+str(nama[1])+'\';'
            print(query)
            cur.execute(query)
            data = cur.fetchone()
            print(data)
            if data == None:
                metno_label = Label(self, text="There are no ongoing Meetings", font=(
                    "Ariel 24 bold"), bg='white', fg='Black')
                canvas.create_window(
                    400, 220, width=600, height=40, anchor="nw", window=metno_label)
            else:
                generate_QR(str(data[0]))
                metno1_label = Label(self, text="Ongoing Meeting:", font=(
                    "Ariel 24 bold"), bg='white', fg='Black')
                canvas.create_window(
                    400, 220, width=600, height=40, anchor="nw", window=metno1_label)
                metno2_label = Label(self, text=(data[4]+" - " + data[5]).title(), font=(
                    "Ariel 20 bold"), bg='white', fg='#FFC331')
                canvas.create_window(
                    430, 300, anchor="nw", window=metno2_label)
                q1 = 'select tickarr from public.meetingatt where id =\''+str(data[0])+'\';'

                cur.execute(q1)
                data3 = cur.fetchone()
                def take_att():
                    q2 = 'UPDATE public.meetingatt SET att=att+1 WHERE id = \''+str(data[0])+'\' and stuid=\''+student_name+'\';'
                    cur.execute(q2)
                    conn.commit()
                    messagebox.showinfo(
                    "Attendance System", "Your attendance has been recorded")
                if getTime() in range (data3[0][-1],data3[0][-1]+4):