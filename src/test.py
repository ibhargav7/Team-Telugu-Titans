import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import pyqrcode
import time
root = Tk()
canvas = Canvas(root, width=1200, height=700,
                                bg='#FFFFFF', bd=0, highlightthickness=0)


canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(0, 0, 1200, 80, fill='#FFC331', outline='white')
user_label = Label(root, text="Username ", font=(
                "Ariel 20 bold"), bg='#503284', fg='Black')
canvas.create_window(1000, 25, anchor="nw", window=user_label)
meeting_label = Label(root, text="Check Attendance", font=(
                "Ariel 20 bold"), bg='#503284', fg='white')
canvas.create_window(80, 120, anchor="nw", window=meeting_label) 

menu= StringVar()
menu.set("Select meeting")
drop= OptionMenu(root, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
canvas.create_window(400, 120, anchor="nw", window=drop)
canvas.create_rectangle(50, 180, 1150, 500, fill='white', outline='black')

def get_course(name="AM.EN.LT00001"):
        conn = connect()
        cur = conn.cursor()
        query ='SELECT course from public."teacherData" where organiser=\''+name+'\';'
        print(query)
        cur.execute(query)
        data = cur.fetchone()
        print(data)
        return data
get_course()
att = Button(root, text="Attendance Summary", font=("Ariel 22 bold"),
        width=20, bg="white", fg='#FFC331', relief=FLAT)
canvas.create_window(640, 550, anchor="nw", window=att)

root.mainloop()
