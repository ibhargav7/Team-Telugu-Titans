import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect

class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=1200, height=700, bg='#FFFFFF',bd=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_rectangle(0, 0, 1200, 80, fill='#FFC331', outline='white')
        course_label = Label(self, text="Course ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(60, 250, anchor="nw", window=course_label)
        course_entry = Entry(self, font=("Ariel 18 bold"))
        course_entry.focus()
        canvas.create_window(60, 300, anchor="nw", window=course_entry)
        start_label = Label(self, text="Start Time ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(80, 250, anchor="nw", window=start_label )
        start_entry = Entry(self, font=("Ariel 18 bold"))
        start_entry.focus()
        canvas.create_window(80, 300, anchor="nw", window=start_entry)
        dur_label = Label(self, text="Duration ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(100, 250, anchor="nw", window=dur_label)
        dur_entry = Entry(self, font=("Ariel 18 bold"))
        dur_entry.focus()
        canvas.create_window(100, 300, anchor="nw", window=dur_entry)
        sec_label = Label(self, text="Section", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(120, 250, anchor="nw", window=sec_label)
        sec_entry = Entry(self, font=("Ariel 18 bold"))
        sec_entry.focus()
        canvas.create_window(120, 300, anchor="nw", window=sec_entry)
        password_label = Label(self, text="Password ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        
        
        
            
