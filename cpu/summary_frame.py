import tkinter as tk
from home import base_summary_frame
from . import graph
from .cpu_data.global_cpu import GlobalCPU


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):
        super().show()
        self.cpuUsageGraph = graph.LineGraph(self)
        self.cpuUsageGraph.pack(fill=tk.BOTH)
        self.cpuUsageGraph.show()

    def hide(self):
        super().hide()
        self.cpuUsageGraph.destroy()

    def update(self, dt):
        self.cpu.update()
        self.cpuUsageGraph.redraw(self.cpu.usages)
