from tkinter import *
from integrator import frame as modelFrame
import psutil

from tkinter import *
from tkinter import scrolledtext


def createFrame(window):   
    # main Frame
    mainFrame = Frame(window)
    mainFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)

    # text Frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)
    textFrame = Frame(mainFrame, width=40, height=10, background="red")
    textFrame.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)

    # graph Frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=1)
    graphFrame = Frame(mainFrame, width=40, height=10, background="blue")
    graphFrame.grid(row=0, column=1, columnspan=1, sticky=N+S+E+W)


    # text data
    global label
    label = Label(textFrame, justify=LEFT)
    label.pack()
    textRefresher()

    

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
