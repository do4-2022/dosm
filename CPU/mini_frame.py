from tkinter import *
from home import mini_frame
from . import graph
from .cpu_data.global_cpu import GlobalCPU
import psutil


class MiniFrame(mini_frame.MiniFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):
        self.cpuUsageGraph = graph.LineGraph(self,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=BOTH)
        self.cpuUsageGraph.show()

    def update(self):
        self.cpu.update()
        self.cpuUsageGraph.redraw(self.cpu.usages)
