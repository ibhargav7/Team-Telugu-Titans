import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
from attendance import Tatt
from meeting import meeting
import time
import pyqrcode
import configparser
import login



class teacher(tk.Frame):

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
            

            print(teacher_name)

            meeting_label = Label(self, text="Ongoing Meeting", font=(
                "Ariel 20 bold"), bg='#503284', fg='white')
            canvas.create_window(80, 120, anchor="nw", window=meeting_label)
            canvas.create_rectangle(
                50, 180, 1150, 500, fill='white', outline='black')

            conn = connect()
            cur = conn.cursor()
            query = 'SELECT * from public."meeting" where start<=' + \
                str(getTime())+' and start+duration>'+str(getTime())+';'
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

                def take_att():
                    q1 = 'UPDATE public.meetingatt SET tick=tick+1, tickarr=array_append(tickarr,'+str(
                        getTime())+') WHERE id=\''+str(data[0])+'\';'
                    cur.execute(q1)
                    conn.commit()
                    messagebox.showinfo(
                    "Attendance System", "Attendance recording has started")
                new_meeting = Button(self, text="Take Attendance", font=("Ariel 22 bold"),
                                     width=15, bg="white", fg='#FFC331', relief=FLAT, command=take_att)
                canvas.create_window(440, 380, anchor="nw", window=new_meeting)

                def end():
                    q1 = 'SELECT roll FROM public."studentData" where branch = \'' + \
                        data[5]+'\';'
                    cur.execute(q1)
                    data1 = cur.fetchall()
                    for i in data1:
                        q2 = 'SELECT att, tick FROM public."meetingatt" where id =\'' + \
                            str(data[0])+'\'and stuid = \''+i[0]+'\';'
                        cur.execute(q2)
                        data2 = cur.fetchone()
                        if data2[1] > 0 and data2[0] == data2[1]:
                            q3 = 'UPDATE public.attend SET attendance=attendance+1 WHERE roll=\'' + \
                                i[0]+'\'and course=\''+str(data[4])+'\';'
                            cur.execute(q3)
                            conn.commit()
                    messagebox.showinfo(
                    "Attendance System", "Attendance has been recorded")
                att = Button(self, text="End Session", font=("Ariel 22 bold"),
                             width=10, bg="white", fg='#FFC331', relief=FLAT, command=end)
                canvas.create_window(830, 380, anchor="nw", window=att)

            # close the communication with the PostgreSQL

        get_meeting()
        new_meeting = Button(self, text="Create New Meeting", font=("Ariel 22 bold"),
                             width=20, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(meeting))
        canvas.create_window(100, 550, anchor="nw", window=new_meeting)

        att = Button(self, text="Attendance Summary", font=("Ariel 22 bold"),
                     width=20, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(Tatt))
        canvas.create_window(640, 550, anchor="nw", window=att)

        def refresh():
            get_meeting()

        refresh = Button(self, text="refresh", font=("Ariel 22 bold"),
                         width=7, bg="white", fg='#FFC331', relief=FLAT, command=refresh)
        canvas.create_window(900, 110, anchor="nw", window=refresh)
