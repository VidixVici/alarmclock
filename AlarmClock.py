import time
from playsound import playsound
import numpy as np
import tkinter as tk 
import array as arr 
import pyperclip as pc 
from tkinter import *
import os
# latest update: Add number of times alarm will sound


def hoursAndMinutes(h, m, s):
    global HaM
    HaM = (int(h) * 3600 + int(m) * 60 + int(s))
    print(HaM)
    return(HaM)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window

        self.pack(fill=BOTH, expand=1)

        # create buttons

        exitButton = Button(self, text='Exit',command=self.clickExitButton)

        startTimer = Button(self, text='Start Timer',command=self.SetTimer)

        stopTimer = Button(self, text='Stop Timer',command=self.StopTimer)

        # create text entry boxes under global var
        global hoursEntry
        hoursEntry = tk.Entry()
        hoursEntry.configure(bg='#09111D')
        hoursEntry.bind("<Button-1>", lambda e: hoursEntry.delete(0, tk.END))
        hoursEntry.insert(0, "0")

        global minutesEntry
        minutesEntry = tk.Entry()
        minutesEntry.configure(bg='#09111D')
        minutesEntry.bind("<Button-1>", lambda e: minutesEntry.delete(0, tk.END))
        minutesEntry.insert(0, "0")

        global secondsEntry
        secondsEntry = tk.Entry()
        secondsEntry.configure(bg='#09111D')
        secondsEntry.bind("<Button-1>", lambda e: secondsEntry.delete(0, tk.END))
        secondsEntry.insert(0, "0")

        global offEntry
        offEntry = tk.Entry()
        offEntry.configure(bg='#09111D')
        offEntry.bind("<Button-1>", lambda e: offEntry.delete(0, tk.END))
        offEntry.insert(0, "10")
        
        # create labels and place in application window

        hourslabel = tk.Label(text='Hours: ')
        hourslabel.place(x=0, y=0)
        hoursEntry.place(x=0, y=23)
        hourslabel.configure(bg='#09111D')

        minuteslabel = tk.Label(text='Minutes: ')
        minuteslabel.place(x=0, y=51)
        minutesEntry.place(x=0, y=73)
        minuteslabel.configure(bg='#09111D')

        secondslabel = tk.Label(text='Seconds:')
        secondslabel.place(x=0, y=103)
        secondsEntry.place(x=0, y=128)
        secondslabel.configure(bg='#09111D')

        offlabel = tk.Label(text='How many times should the Alarm Ring?: ')
        offlabel.place(x=0, y=157)
        offEntry.place(x=0, y=180)
        offlabel.configure(bg='#09111D')

        # place buttons created earlier to run functions

        exitButton.place(x=340, y=370)
        exitButton.configure(highlightbackground='#09111D')

        startTimer.place(x=140, y=370)
        startTimer.configure(highlightbackground='#09111D')

        stopTimer.place(x=240, y=370)
        stopTimer.configure(highlightbackground='#09111D')

    # function for exit button

    def clickExitButton(self):
        exit()

    def SetTimer(self):
        global HaM
        global h
        global m
        global s 
        global off
        off = offEntry.get()
        h = hoursEntry.get()
        m = minutesEntry.get()
        s = secondsEntry.get()
        hoursAndMinutes(h, m, s)
        while HaM:
            mins, secs = divmod(HaM, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            HaM -= 1
            print(timer, end="\r")

        print('Timer Completed')
        while int(off) > 0:
            playsound('wow.mp3')
            playsound('annoying.mp3')
            off = int(off) - 1
            print(off, end="\r")

    def StopTimer(self):
        global off
        off = 0

root = Tk()
app = Window(root)
root.wm_title('VxV AlarmClock')
root.geometry('400x400')
app.configure(bg='#09111D')
root.mainloop()
