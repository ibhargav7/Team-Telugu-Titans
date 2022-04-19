import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import time
import pyqrcode


class teacher(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700,
                        bg='#FFFFFF', bd=0, highlightthickness=0)

        canvas.pack(fill=BOTH, expand=True)

        def generate_QR(str):
            qr = pyqrcode.create("http://localhost/meeting" + str)
            img = BitmapImage(data=qr.xbm(scale=7))

            img_lbl = Label(self, image=img, bg='white')
            canvas.create_window(80, 200, anchor="nw", window=img_lbl)
            img_lbl.image = img
            img_lbl.place()

        def getTime():
            t = time.localtime()
            current_time = int(time.strftime("%H"+"%M", t))
            return current_time
        canvas.create_rectangle(
            0, 0, 1200, 80, fill='#FFC331', outline='white')
        def get_meeting():
            user_label = Label(self, text="Username ", font=(
                "Ariel 20 bold"), bg='#503284', fg='Black')
            canvas.create_window(1000, 25, anchor="nw", window=user_label)
            meeting_label = Label(self, text="Ongoing Meeting", font=(
                "Ariel 20 bold"), bg='#503284', fg='white')
            canvas.create_window(80, 120, anchor="nw", window=meeting_label)
            canvas.create_rectangle(
                50, 180, 1150, 500, fill='white', outline='black')

            conn = connect()
            cur = conn.cursor()
            query = 'SELECT * from public."meeting";'
            print(query)
            cur.execute(query)
            data = cur.fetchone()
            print(data)
            if data == None:
                metno_label = Label(self, text="There are no ongoing Meetings", font=(
                    "Ariel 20 bold"), bg='white', fg='Black')
                canvas.create_window(400, 200, anchor="nw", window=metno_label)
            else:
                generate_QR(str(data[0]))
                metno1_label = Label(self, text="Ongoing Meeting:", font=(
                    "Ariel 24 bold"), bg='white', fg='Black')
                canvas.create_window(400, 220, anchor="nw", window=metno1_label)
                metno2_label = Label(self, text=(data[4]+" - " + data[5]).title(), font=(
                    "Ariel 20 bold"), bg='white', fg='#FFC331')
                canvas.create_window(430, 300, anchor="nw", window=metno2_label)

                new_meeting = Button(self, text="Take Attendance", font=("Ariel 22 bold"),
                                    width=15, bg="white", fg='#FFC331', relief=FLAT)
                canvas.create_window(440, 380, anchor="nw", window=new_meeting)

                att = Button(self, text="End Session", font=("Ariel 22 bold"),
                            width=10, bg="white", fg='#FFC331', relief=FLAT)
                canvas.create_window(830, 380, anchor="nw", window=att)

            # close the communication with the PostgreSQL
            cur.close()
        get_meeting()
        new_meeting = Button(self, text="Create New Meeting", font=("Ariel 22 bold"),
                             width=20, bg="white", fg='#FFC331', relief=FLAT)
        canvas.create_window(100, 550, anchor="nw", window=new_meeting)

        att = Button(self, text="Attendance Summary", font=("Ariel 22 bold"),
                     width=20, bg="white", fg='#FFC331', relief=FLAT)
        canvas.create_window(640, 550, anchor="nw", window=att)
