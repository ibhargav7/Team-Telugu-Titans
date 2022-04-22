import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from connection import connect
import time
import teacher 
import configparser

class meeting(tk.Frame):

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


        def getTime():
            t = time.localtime()
            current_time = int(time.strftime("%H"+"%M", t))
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
            start_entry.insert(0,getTime())
        config_obj = configparser.ConfigParser()
        config_obj.read("configfile.ini")
        info = config_obj["info"]
        teacher_name = info["teacher_name"]  
        def new():
            if course_entry.get()=="":
                messagebox.showinfo("Meeting System", "Please enter the Course name")
            elif start_entry.get()=="":
                messagebox.showinfo("Meeting System", "Please enter the Start Time")
            elif dur_entry.get()=="":
                messagebox.showinfo("Meeting System", "Please enter the Duration of the meeting")
            elif sec_entry.get()=="":
                messagebox.showinfo("Meeting System", "Please enter the Section")
            else:
                course = course_entry.get()
                start = start_entry.get()
                dur = dur_entry.get()
                sec = sec_entry.get()
                conn = connect()
                cur = conn.cursor()
                query ='INSERT INTO public.meeting(start, duration, organiser, course, sec) VALUES ('+start+','+dur+',\''+teacher_name+'\',\''+course+'\',\''+sec+'\');'
                print(query)
                cur.execute(query)
                conn.commit()
                messagebox.showinfo("Meeting System", "Meeting Sheduled")
                q1='SELECT roll FROM public."studentData" where branch = \''+sec+'\''
                cur.execute(q1)
                data1 = cur.fetchall()
                q2='SELECT max(id) FROM public."meeting" ;'
                cur.execute(q2)
                data2 = cur.fetchone()
                print(data2[0])
                for i in data1:
                    print(i)
                    q3='INSERT INTO public.meetingatt(id, stuid, att, tick, tickarr) VALUES ('+str(data2[0])+',\''+i[0]+'\',\''+str(0)+'\',\''+str(0)+'\',\'{}\');'
                    cur.execute(q3)
                    conn.commit()
                
                # close the communication with the PostgreSQL
                cur.close()
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
        
        new_meeting = Button(self, text="Create Meet", font=("Ariel 22 bold"),
                            width=12, bg="white", fg='#FFC331', relief=FLAT, command=new)
        canvas.create_window(200, 590, anchor="nw", window=new_meeting)

        att = Button(self, text="Dashboard", font=("Ariel 22 bold"),
                    width=10, bg="white", fg='#FFC331', relief=FLAT, command=lambda: controller.show_frame(teacher.teacher))
        canvas.create_window(800, 590, anchor="nw", window=att)
        now = Button(self, text="now", font=("Ariel 16 bold"),
                    width=3, bg="white", fg='#FFC331', relief=FLAT,command=get_time)
        canvas.create_window(820, 300, anchor="nw", window=now)
                
                
                
                    
