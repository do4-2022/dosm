from tkinter import *
from integrator import frame as modelFrame
import psutil



def createFrame(window):

    canvas = Frame(window, width=200, height=200, bg="#FF0000")
    canvas.grid(row = 0, column = 0, sticky=NSEW)
    canvas.columnconfigure(0, weight=1)
    canvas.rowconfigure(0, weight=1)

    # frame = tk.Frame(canvas, bg="#00FF00")
    # frame.grid(row = 0, column = 0, pady = 2)
    # frame.columnconfigure(0, weight=1)
    # frame.rowconfigure(0, weight=1)

    # global label
    # label = tk.Label(frame, anchor='w', justify=tk.LEFT)
    
    # frame2 = tk.Frame(canvas, bg="#0000FF")
    # frame2.grid(row = 1, column = 0, pady = 2)
    # frame2.columnconfigure(1, weight=1)
    # frame2.rowconfigure(0, weight=1)

    # textRefresher()

def generateText():
    text =  f"Global CPU usage (%) : {psutil.cpu_percent(interval=0.5, percpu=False)} \n"
    text += f"CPU usage per core (%) : { psutil.cpu_percent(interval=0.5, percpu=True) } \n"
    text += f"CPU times \n"
    text += f"Number of logical CPU : { psutil.cpu_count( logical=True) } \n"
    text += f"Number of physical CPU : {psutil.cpu_count( logical=False)} \n"
    text += f"CPU stats : {psutil.cpu_stats()} \n"
    text += f"Global CPU frequence : {psutil.cpu_freq(percpu=False)} \n"
    text += f"Frequence per CPU : {psutil.cpu_freq(percpu=True)} \n"
    text += f"Average load :  {psutil.getloadavg()}"
    return text
    

def textRefresher():
    global label
    label.config(text=generateText())
    label.after(1000, textRefresher)

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