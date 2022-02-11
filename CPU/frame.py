from logging import root
import tkinter as tk
from integrator import frame as modelFrame
import psutil



def createFrame(window):
    frame = tk.Canvas(window, width=1000, height=680, bg="#BBBBF9")
    frame.place(x=0, y=0)
    global label
    label = tk.Label(frame, anchor='w', justify=tk.LEFT)
    label.place(x=0, y=0)
    textRefresher()
    



def generateText():
    text =  f"Global CPU usage (%) : {psutil.cpu_percent(interval=0.5, percpu=False)} \n"
    text += f"CPU usage per core (%) : { psutil.cpu_percent(interval=0.5, percpu=True) } \n"
    text += f"CPU times \n"
    text += f"Number of logical CPU : { psutil.cpu_count( logical=True) } \n"
    text += f"Number of physical CPU : {psutil.cpu_count( logical=False)} \n"
    text += f" : {psutil.cpu_stats()} \n"
    text += f" : {psutil.cpu_freq(percpu=False)} \n"
    text += f" : {psutil.cpu_freq(percpu=True)} \n"
    text += f" :  {psutil.getloadavg()} \n"

    return text
    
def textRefresher():
    global label
    label.config(text=generateText())
    label.after(1000, textRefresher) # every second...

def test():
    print( psutil.cpu_percent(interval=0.5, percpu=False) )
    print( psutil.cpu_percent(interval=0.5, percpu=True) )
    print( psutil.cpu_times() )
    print( psutil.cpu_count( logical=True) )
    print( psutil.cpu_count( logical=False) )
    print( psutil.cpu_stats() )
    print( psutil.cpu_freq(percpu=False) )
    print( psutil.cpu_freq(percpu=True) )
    print( psutil.getloadavg() )