
from tkinter import StringVar
import tkinter as tk
import functools
from home import base_summary_frame
from process import read


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, name, **options):
        super().__init__(master, logger, name, **options)
        
        self.processCount = StringVar()


    def show(self):
        self.processLs = tk.Label(self, textvariable=self.processCount)
        self.processLs.pack(fill=tk.BOTH, expand=True)


    def update(self, dt):
        result = read.read_process()
        cpu_percent = round(functools.reduce(lambda x, y: {'cpu_percent': y['cpu_percent']+x['cpu_percent']}, result)['cpu_percent'], 2)
        memory_percent = round(functools.reduce(lambda x, y: {'memory_percent': y['memory_percent']+x['memory_percent']}, result)['memory_percent'], 2)
        
        
        self.processCount.set("Process : " + str(len(result)) + "\nCPU : "+str(cpu_percent) + " %\nRAM : " + str(memory_percent) + " %")

