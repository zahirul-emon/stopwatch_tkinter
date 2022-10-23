#Importing Modules
from tkinter import *
import time
#Functions Declaration
def start():
    global  s, m, h
    time.sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if stop == 0:
        varS.set(s)
        varM.set(m)
        varH.set(h)
        root.after(200,start)
def stop_watch():
    global stop
    stop = 1
def reset_watch():
    global stop, s, m, h
    stop = 1
    s = 0
    m = 0
    h = 0
    varS.set(s)
    varM.set(m)
    varH.set(h)
def restart_watch():
    global stop, s, m, h
    stop = 0
    s = 0
    m = 0
    h = 0
    root.after(200,start)    
# Master window setting
root = Tk()
root.title("My Stop Watch")
root.geometry("265x200")
root.maxsize(265,200)
root.minsize(265,200)
root.configure(bg = "orange")
# Variable Declaration
varS = IntVar()
varS.set("00")
varM = IntVar()
varM.set("00")
varH = IntVar()
varH.set("00")
stop = 0
s = 0
m = 0
h = 0
# Fonts combination Declaration
font_digit = ("Digital Display",40, "normal")
font_heading = ("Technology",30, "normal")
font_button = ("Times New Roman", 16, "normal")
#Hour, Min, Sec Label for dispaly
hour = Label(root, text = "Hour:", width = 5, font = font_heading).place(x =10, y = 50)
Label(root, textvariable = varH, width = 2, font = font_digit).place(x = 110, y = 50)
minute = Label(root, text = "Min:", width = 5, font = font_heading).place(x =10, y = 100)
Label(root, textvariable = varM, width = 2, font = font_digit).place(x = 110, y = 100)
second = Label(root, text = "Sec:", width = 5, font = font_heading).place(x = 10, y = 150)
Label(root, textvariable = varS,width = 2, font = font_digit).place(x = 110, y = 150)
#Buttons
Start_button = Button(root, text = "Start", command = start, bg = "green",width = 6, font = font_button).place(x = 170, y = 50)
Stop_button = Button(root, text = "Stop", command = stop_watch, bg = "red",width = 6, font = font_button).place(x = 170, y = 100)
restart_button = Button(root, text = "Restart", command = restart_watch, bg = "yellow",width = 6, font = font_button).place(x = 170, y = 150)
reset_button = Button(root, text = "Reset", command = reset_watch, bg = "Cyan",width = 19, font = font_button).place(x = 11, y = 5)

root.mainloop()
