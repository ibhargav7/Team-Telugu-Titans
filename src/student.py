import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect


class student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700,
                        bg='#FFFFFF', bd=0, highlightthickness=0)


        canvas.pack(fill=BOTH, expand=True)
        canvas.create_rectangle(0, 0, 1200, 80, fill='#FFC331', outline='white')
        user_label = Label(self, text="Username ", font=(
                        "Ariel 20 bold"), bg='#503284', fg='Black')
        canvas.create_window(1000, 25, anchor="nw", window=user_label)
        meeting_label = Label(self, text="Ongoing Meeting", font=(
                        "Ariel 20 bold"), bg='#503284', fg='white')
        canvas.create_window(80, 120, anchor="nw", window=meeting_label)
        canvas.create_rectangle(50, 180, 1150, 500, fill='white', outline='black')


        att = Button(self, text="Attendance Summary", font=("Ariel 22 bold"),
               width=20, bg="white", fg='#FFC331', relief=FLAT)
        canvas.create_window(340, 550, anchor="nw", window=att)
