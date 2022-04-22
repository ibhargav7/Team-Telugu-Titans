from re import T
import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
from teacher import teacher
from attendance import Tatt
from meeting import meeting
from student import student
import configparser

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

        for F in (login, Tatt, student, meeting, teacher):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bg = Image.open('Images/Amrita.png')
        bg1 = Image.open('Images/ATTENDANCE MANAGEMENT SYSTEM.png')
        bg2 = Image.open('Images/login.png')
        newsize = (300, 120)
        bg = bg.resize(newsize)
        bg2 = bg2.resize((400, 400))
        bg = ImageTk.PhotoImage(bg)
        bg1 = ImageTk.PhotoImage(bg1)
        bg2 = ImageTk.PhotoImage(bg2)

        canvas = Canvas(self, width=1200, height=700,
                        bg='#FFFFFF', bd=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_rectangle(
            1, 1, 600, 700, fill='#503284', outline='white')
        img1 = Label(self, image=bg, bg='white')
        img2 = Label(self, image=bg1, bg='white')
        img3 = Label(self, image=bg2, bg='#503284')
        canvas.create_window(770, 30, anchor='nw', window=img1)
        canvas.create_window(700, 250, anchor='nw', window=img2)
        canvas.create_window(0, 0, anchor='nw', window=img3)
        img1.image = bg
        img1.place()
        img2.image = bg1
        img2.place()
        img3.image = bg2
        img3.place()
        user_label = Label(self, text="Username ", font=(
            "Ariel 20 bold"), bg='#503284', fg='white')
        canvas.create_window(80, 250, anchor="nw", window=user_label)
        user_entry = Entry(self, font=("Ariel 18 bold"))
        user_entry.focus()
        canvas.create_window(80, 300, anchor="nw", window=user_entry)
        password_label = Label(self, text="Password ", font=(
            "Ariel 20 bold"), bg='#503284', fg='white')
        canvas.create_window(80, 360, anchor="nw", window=password_label)
        paswd = StringVar()
        password_entry = Entry(self, textvar=paswd,
                               font=("Ariel 18 bold"), show="*")
        canvas.create_window(80, 410, anchor="nw", window=password_entry)

        def new():
            if user_entry.get() == "":
                messagebox.showinfo(
                    "Login System", "Please enter the Username")
            elif password_entry.get() == "":
                messagebox.showinfo(
                    "Login System", "Please enter the Password")
            elif user_entry.get() == "" and password_entry.get() == "":
                messagebox.showinfo(
                    "Login System", "Please enter the Username and Password")
            else:
                name = user_entry.get()
                password = password_entry.get()
                if (len(name) > 14):
                    conn = connect()
                    cur = conn.cursor()
                    query = 'SELECT roll,password from public."studentData" where roll=\''+name+'\';'
                    print(query)
                    cur.execute(query)
                    data = cur.fetchone()
                    print(data)
                    if data == None:
                        messagebox.showinfo(
                            "Login System", 'Incorrect username or password')
                    elif data[0] == name and data[1] == password:
                        config_obj = configparser.ConfigParser()
                        config_obj.read("configfile.ini")
                        info = config_obj["info"]
                        info["student_name"] = name
                        with open('configfile.ini', 'w') as configfile:
                            config_obj.write(configfile)
                        messagebox.showinfo(
                            "Login System", 'Logged in Successfully')
                        controller.show_frame(student)
                    else:
                        messagebox.showinfo('Incorrect username or password')

                    # close the communication with the PostgreSQL
                    cur.close()
                else:

                    conn = connect()
                    cur = conn.cursor()
                    query = 'SELECT roll,password from public."teacherData" where roll=\''+name+'\';'
                    print(query)
                    cur.execute(query)
                    data = cur.fetchone()
                    print(data)
                    if data == None:
                        messagebox.showinfo("Login System", 'Incorrect username or password')
                    elif data[0] == name and data[1] == password:
                        config_obj = configparser.ConfigParser()
                        config_obj.read("configfile.ini")
                        info = config_obj["info"]
                        info["teacher_name"] = name
                        t = info["teacher_name"]
                        with open('configfile.ini', 'w') as configfile:
                            config_obj.write(configfile)
                        messagebox.showinfo(
                            "Login System", 'Logged in Successfully')
                        controller.show_frame(teacher)
                    else:
                        messagebox.showinfo('Incorrect username or password')

                    # close the communication with the PostgreSQL
                    cur.close()

        login = Button(self, text="Log In", font=("Ariel 22 bold"),
                       width=8, bg="white", fg='#FFC331', relief=FLAT, command=new)
        canvas.create_window(180, 500, anchor="nw", window=login)


app = Main()
app.mainloop()
