import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Login, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        bg = Image.open('Images/Amrita.png')
        bg1 = Image.open('Images/ATTENDANCE MANAGEMENT SYSTEM.png')
        bg2 = Image.open('Images/login.png')
        newsize = (300, 120)
        bg = bg.resize(newsize)
        bg2 = bg2.resize((400,400))
        bg = ImageTk.PhotoImage(bg)
        bg1 = ImageTk.PhotoImage(bg1)
        bg2 = ImageTk.PhotoImage(bg2)
        
                
        canvas = Canvas(self, width=1200, height=700, bg='#FFFFFF',bd=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        canvas.create_rectangle(0, 0, 600, 700, fill='#503284', outline='white')
        canvas.create_image(770, 30, image=bg, anchor='nw')
        canvas.create_image(700, 250, image=bg1, anchor='nw')
        canvas.create_image(0, 0, image=bg2, anchor='nw')

        user_label = Label(self, text="Username ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(80, 250, anchor="nw", window=user_label)
        user_entry = Entry(self, font=("Ariel 18 bold"))
        user_entry.focus()
        canvas.create_window(80, 300, anchor="nw", window=user_entry)
        password_label = Label(self, text="Password ", font=("Ariel 20 bold"),bg='#503284', fg='white')
        canvas.create_window(80, 360, anchor="nw", window=password_label)
        paswd=StringVar()
        password_entry = Entry(self, textvar=paswd, font=("Ariel 18 bold"), show="*")
        canvas.create_window(80, 410, anchor="nw", window=password_entry)
        def new():
            if user_entry.get()=="":
                messagebox.showinfo("Login System", "Please enter the Username")
            elif password_entry.get()=="":
                messagebox.showinfo("Login System", "Please enter the Password")
            elif user_entry.get()=="" and password_entry.get()=="":
                messagebox.showinfo("Login System", "Please enter the Username and Password")
            else:
                name = user_entry.get()
                password = password_entry.get()
                conn = connect()
                cur = conn.cursor()
                query ='SELECT roll,password from public."studentData" where roll=\''+name+'\';'
                print(query)
                cur.execute(query)
                data = cur.fetchone()
                print(data)
                if data==None:
                    messagebox.showinfo("Login System", 'Incorrect username or password')
                elif data[0]==name and data[1]==password:
                    
                    messagebox.showinfo("Login System", 'Logged in Successfully')
                    controller.show_frame(Login)
                else:
                    messagebox.showinfo('Incorrect username or password')

                
                # close the communication with the PostgreSQL
                cur.close()
        login = Button(self, text="Log In", font=("Ariel 22 bold"),
                    width=8, bg="white", fg='#FFC331', relief=FLAT, command=new)
        canvas.create_window(180, 500, anchor="nw", window=login)
        
            



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()