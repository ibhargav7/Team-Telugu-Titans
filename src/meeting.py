import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import time

class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700,
                bg='#FFFFFF', bd=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_rectangle(0, 0, 1200, 80, fill='#FFC331', outline='white')


        def getTime():
            t = time.localtime()
            current_time = int(time.strftime("%H"+"%M"+"%S", t))
            return current_time


        main_label = Label(self, text="Create a Meeting: ", font=(
            "Ariel 25 bold"), bg='white', fg='brown')
        canvas.create_window(60, 115, anchor="nw", window=main_label)
        course_label = Label(self, text="Course ", font=(
            "Ariel 20 bold"), bg='white', fg='black')
        canvas.create_window(160, 200, anchor="nw", window=course_label)
        course_entry = Entry(self, font=("Ariel 18 bold"))
        course_entry.focus()
        canvas.create_window(440, 200, anchor="nw", window=course_entry)
        def get_time():
            self.start_entry = getTime()

        start_label = Label(self, text="Start Time ", font=(
            "Ariel 20 bold"), bg='white', fg='black')
        canvas.create_window(160, 300, anchor="nw", window=start_label)
        start_entry = Entry(self, font=("Ariel 18 bold"))
        start_entry.focus()
        canvas.create_window(440, 300, anchor="nw", window=start_entry)
        dur_label = Label(self, text="Duration ", font=(
            "Ariel 20 bold"), bg='white', fg='black')
        canvas.create_window(160, 400, anchor="nw", window=dur_label)
        dur_entry = Entry(self, font=("Ariel 18 bold"))
        dur_entry.focus()
        canvas.create_window(440, 400, anchor="nw", window=dur_entry)
        sec_label = Label(self, text="Section", font=(
            "Ariel 20 bold"), bg='white', fg='black')
        canvas.create_window(160, 500, anchor="nw", window=sec_label)
        sec_entry = Entry(self, font=("Ariel 18 bold"))
        sec_entry.focus()

        canvas.create_window(440, 500, anchor="nw", window=sec_entry)
        password_label = Label(self, text="Password ", font=(
            "Ariel 20 bold"), bg='#503284', fg='black')
        new_meeting = Button(self, text="Create Meet", font=("Ariel 22 bold"),
                            width=12, bg="white", fg='#FFC331', relief=FLAT)
        canvas.create_window(200, 590, anchor="nw", window=new_meeting)

        att = Button(self, text="Dashboard", font=("Ariel 22 bold"),
                    width=10, bg="white", fg='#FFC331', relief=FLAT)
        canvas.create_window(800, 590, anchor="nw", window=att)
        now = Button(self, text="now", font=("Ariel 16 bold"),
                    width=3, bg="white", fg='#FFC331', relief=FLAT,command=get_time)
        canvas.create_window(820, 300, anchor="nw", window=now)
                
                
                
                    
