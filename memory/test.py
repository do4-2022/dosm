
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from pathlib import Path
import psutil 
import tkinter as tk
from tkinter import *


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,1), dpi=100)
a = f.add_subplot(111)

global xList 
xList = [0]
global yList 
yList = [100-psutil.virtual_memory().available * 100 / psutil.virtual_memory().total]


def animate(i):
    global xList
    global yList
    yList.append(100-round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
    xList.append(xList[len(xList)-1]+1)
    xList= xList[-100:]
    yList= yList[-100:]
    a.clear()
    a.get_xaxis().set_visible(False)
    a.set_ylim([0, 100])
    a.plot(xList, yList)
    global usage
    global usage_gb
    usage.config(text=(str(100-round((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total),1))+'% used'))
    usage_gb.config(text=("Used : "+str(round((psutil.virtual_memory().total-psutil.virtual_memory().available)/1000000000,1))+'GB/'+str(round((psutil.virtual_memory().total/1000000000),1))+"GB"))

    
class RAM(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "RAM")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame = Graph(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        total = tk.Label(self, text="Total available : "+str(round((psutil.virtual_memory().total/1000000000),1))+"GB", font=LARGE_FONT)
        total.pack(pady=10,padx=10)
        frame.tkraise()

class Graph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global usage
        usage = tk.Label(self, text="Memory", font=LARGE_FONT)
        usage.pack(pady=10,padx=10)
        global usage_gb

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        usage_gb = tk.Label(self, text="Used", font=LARGE_FONT)
        usage_gb.pack(pady=10,padx=10)

app = RAM()
ani = animation.FuncAnimation(f, animate, interval=100)
app.mainloop()
