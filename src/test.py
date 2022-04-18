import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
root = Tk()
bg = Image.open('Images/Amrita.png')
bg1 = Image.open('Images/ATTENDANCE MANAGEMENT SYSTEM.png')
bg2 = Image.open('Images/login.png')
newsize = (300, 120)
bg = bg.resize(newsize)
bg2 = bg2.resize((400, 400))
bg = ImageTk.PhotoImage(bg)
bg1 = ImageTk.PhotoImage(bg1)
bg2 = ImageTk.PhotoImage(bg2)

canvas = Canvas(root, width=1200, height=700,
                bg='#FFFFFF', bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(0, 0, 1200, 80, fill='#FFC331', outline='white')
user_label = Label(root, text="Username ", font=(
    "Ariel 20 bold"), bg='#503284', fg='Black')
canvas.create_window(1000, 25, anchor="nw", window=user_label)
meeting_label = Label(root, text="Ongoing Meeting", font=(
    "Ariel 20 bold"), bg='#503284', fg='white')
canvas.create_window(80, 120, anchor="nw", window=meeting_label)
canvas.create_rectangle(50, 180, 1150, 450, fill='white', outline='black')




new_meeting = Button(root, text="Create New Meeting", font=("Ariel 22 bold"),
                   width=8, bg="white", fg='#FFC331', relief=FLAT)
canvas.create_window(180, 550, anchor="nw", window=new_meeting)

login = Button(root, text="Attendance Summary", font=("Ariel 22 bold"),
                   width=8, bg="white", fg='#FFC331', relief=FLAT)
canvas.create_window(780, 550, anchor="nw", window=login)
root.mainloop()
