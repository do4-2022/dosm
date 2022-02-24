
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

from integrator import base_frame
from logger.level import LogLevel
from logger.logger import Logger

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

class TabFrame (base_frame.BaseFrame):

    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.ramUsageGraph = None
        self.ramUsagePercent = None
        self.ramUsageGB = None
        self.totalRam = None
        self.graphFrame = None
        self.frame = None
        self.figure = Figure(figsize=(5,1), dpi=100)
        self.subplot = self.figure.add_subplot(111)
        self.xList = [0]
        self.yList = [100-psutil.virtual_memory().available * 100 / psutil.virtual_memory().total]
        self.name = "Memory"

        

    def show(self):

        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill="both", expand = True)
        self.totalRam = tk.Label(self.frame, text="Total available : "+str(round((psutil.virtual_memory().total/1000000000),1))+"GB", font=LARGE_FONT)
        self.totalRam.pack(pady=10,padx=10)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.graphFrame = Graph(self.frame, self.figure)
        self.graphFrame.grid(row=0, column=0, sticky="nsew")
        self.graphFrame.tkraise()    
        
        # graph Frame
        self.graphFrame = tk.Frame(self)
        self.graphFrame.pack()

        super().show()

    def hide(self):
        self.totalRam.destroy()
        self.frame.destroy()
        super().hide()

        
    def update(self, dt):
            self.yList.append(100-round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
            self.xList.append(self.xList[len(self.xList)-1]+1)
            self.xList= self.xList[-100:]
            self.yList= self.yList[-100:]
            self.subplot.clear()
            self.subplot.get_xaxis().set_visible(False)
            self.subplot.set_ylim([0, 100])
            self.subplot.plot(self.xList, self.yList)
            
class Graph(tk.Frame):

    def __init__(self, parent, f):
        tk.Frame.__init__(self, parent)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
