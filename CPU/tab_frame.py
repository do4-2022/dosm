import tkinter as tk
from tkinter import ttk

from integrator import base_frame
from logger.level import LogLevel
from logger.logger import Logger
from . import graph
from .cpu_data.global_cpu import GlobalCPU

class TabFrame (base_frame.BaseFrame):

    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.dataTree = ttk.Treeview()
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):   

        # data tree
        dataFrame = tk.Frame(self)
        dataFrame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.generateTreeView(dataFrame)

        # graph Frame
        graphFrame = tk.Frame(self, width=100, height=100)
        graphFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


        #graph data
        self.cpuUsageGraph = graph.LineGraph(graphFrame,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=tk.BOTH)
        self.cpuUsageGraph.show()

    def hide(self):
        tk.pack_forget(self)
        
    def update(self, dt):
        self.cpu.update()
        self.fillTreeView()
        self.cpuUsageGraph.redraw(self.cpu.usages)
        self.after(1000, self.update, 1000)

        self.log()


    def log(self):
        if len(self.cpu.usages) >= 2:
            if self.cpu.usages[-1] >= 75 and self.cpu.usages[-2] < 75:
                self.logger.write_log(f"CPU global usage exceded 75% ({self.cpu.usages[-1]}%)", level=LogLevel.WARN)
            elif self.cpu.usages[-1] >= 50 and self.cpu.usages[-2] < 50:
                self.logger.write_log(f"CPU global usage exceded 50% ({self.cpu.usages[-1]}%)", level=LogLevel.INFO)
            elif self.cpu.usages[-1] < 75 and self.cpu.usages[-2] >= 75:
                self.logger.write_log(f"CPU global usage has gone under 75% ({self.cpu.usages[-1]}%)", level=LogLevel.INFO)
        

    def generateTreeView(self, master):
        columns = ('category', 'value')

        self.dataTree = ttk.Treeview(master, columns=columns, show='headings')
        self.dataTree.column('category', width=400)
        self.dataTree.column('value', width=100)
        # define headings
        self.dataTree.heading('category', text='Category')
        self.dataTree.heading('value', text='Value')
      
        # add a scrollbar
        scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.dataTree.yview)
        self.dataTree.configure(yscroll=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.dataTree.pack(side=tk.LEFT, fill=tk.Y, expand=True)


    def fillTreeView(self):
        # empty it
        for i in self.dataTree.get_children():
            self.dataTree.delete(i)

        # fill it
        for element in self.cpu.generateDataTuples():
            self.dataTree.insert('', tk.END, values=element)

        
