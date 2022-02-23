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
        self.fig = Figure(figsize=(2, 2), dpi=100)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.set_ylim([0, 100])
        self.canvas = FigureCanvasTkAgg()

    def show(self):
        
        self.subplot.plot([])

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def redraw(self, listY):
        self.subplot.clear()
        self.subplot.set_ylim([0, 100])
        self.subplot.set_xticks([])
        self.subplot.plot(listY)
        self.canvas.draw()

    def hide(self):
        pass