import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 


class Graph(tk.Frame):

    def __init__(self, parent, f):
        tk.Frame.__init__(self, parent)
        self.canvas = FigureCanvasTkAgg(f, parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)