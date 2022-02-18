import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from PIL import ImageTk
import numpy as np



class LineGraph(tk.Frame):
    def __init__(self, master, **options):
        super().__init__(master, **options)
        self.listY = []
        self.fig = Figure(figsize=(2, 2), dpi=100)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.set_ylim([0, 100])

    def show(self):
        
        self.subplot.plot(self.listY)

        canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def add(self, Y):
        self.listY.append(Y)
        self.subplot.clear()
        self.subplot.plot(self.listY)

    def hide(self):
        pass