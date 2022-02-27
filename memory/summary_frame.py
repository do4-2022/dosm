import tkinter as tk
from home import base_summary_frame
from .graph import Graph
from .cpu_data.global_cpu import GlobalCPU


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.cpuUsageGraph = Graph.LineGraph(self)

    def show(self):
        self.cpuUsageGraph = Graph.LineGraph(self,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=tk.BOTH)
        self.cpuUsageGraph.show()
        super().show()

    def hide(self):
        self.cpuUsageGraph.destroy()
        super().hide()

    def update(self, dt):
        self.cpu.update()
        self.cpuUsageGraph.redraw(self.cpu.usages)
