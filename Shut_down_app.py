from tkinter import *
from tkinter import messagebox
import os

def restart():
    result=messagebox.askquestion("Restart","Are you sure want to restart?")
    if result=="yes":
       os.system("Shutdown /r /t 1")
def restart_time():
    result=messagebox.askquestion("restart","Are you sure want to restart?")
    if result=="yes":
       os.system("Shutdown /r /t 20")
def logout():
    result=messagebox.askquestion("Log out","Are you sure want to restart?")
    if result=="yes":
       os.system("Shutdown -l")
def Shutdown():
    result=messagebox.askquestion("Shutdown","Are you sure want to restart?")
    if result=="yes":
       os.system("Shutdown /s /t 1")            


st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button=Button(st,text="Restart", font=("Time Nez Roman", 20, "bold"),
                 relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button=Button(st,text="Restart Time", font=("Time Nez Roman", 20, "bold"),
                  relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button=Button(st,text="Log-Out", font=("Time Nez Roman", 20, "bold"), 
                 relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

sd_button=Button(st,text="ShutDown", font=("Time Nez Roman", 20, "bold"), 
                 relief=RAISED, cursor="plus", command=Shutdown)
sd_button.place(x=150, y=370, height=50, width=200)

st.mainloop()