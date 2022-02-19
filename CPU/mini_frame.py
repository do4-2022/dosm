from tkinter import *
from home import mini_frame
from CPU import graph
import psutil


class MiniFrame(mini_frame.MiniFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):
        self.cpuUsageGraph = graph.LineGraph(self,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=BOTH)
        self.cpuUsageGraph.show()

    def update(self):
        self.cpuUsageGraph.add(psutil.cpu_percent(interval=0.5, percpu=False))