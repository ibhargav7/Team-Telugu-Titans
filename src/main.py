from re import T
import tkinter as tk
from tkinter import *
import tkinter as tk
from teacher import teacher
from attendance import Tatt
from meeting import meeting
from student import student
from stuatt import stuatt
from login import login

LARGE_FONT = ("Verdana", 12)


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.title = "Attendance Management System"
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (login, Tatt, student, meeting, teacher, stuatt):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()




app = Main()
app.mainloop()
