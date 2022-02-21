import tkinter as tk
from tkinter import ttk

from integrator import frame as modelFrame
from logger.level import LogLevel
from logger.logger import Logger
from . import graph
from .cpu_data.global_cpu import GlobalCPU

class Tab (modelFrame.DOSMFrame):

    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.cpu = GlobalCPU()
        self.dataTree = ttk.Treeview()
        self.cpuUsageGraph = graph.LineGraph(self)

    def show(self):   
        # Frame with one row and two columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        # data tree
        self.generateTreeView(self)
        self.dataTree.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)

        # graph Frame
        graphFrame = Frame(self, width=100, height=10)
        graphFrame.grid(row=0, column=2, sticky=N+S+E+W)


        #graph data
        self.cpuUsageGraph = graph.LineGraph(graphFrame,width=40, padx=40, pady=40)
        self.cpuUsageGraph.pack(fill=BOTH)
        self.cpuUsageGraph.show()


        
    def update(self, dt):
        self.cpu.update()
        self.fillTreeView()
        self.cpuUsageGraph.redraw(self.cpu.usages)

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
        master.columnconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)

        columns = ('category', 'value')

        self.dataTree = ttk.Treeview(master, columns=columns, show='headings')
        self.dataTree.column('category', width=400)
        self.dataTree.column('value', width=100)
        # define headings
        self.dataTree.heading('category', text='Category')
        self.dataTree.heading('value', text='Value')
      
        self.dataTree.grid(row=0, column=0, sticky=N+S+E+W)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(master, orient=VERTICAL, command=self.dataTree.yview)
        self.dataTree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=N+S)


    def fillTreeView(self):
        # empty it
        for i in self.dataTree.get_children():
            self.dataTree.delete(i)

        # fill it
        for element in self.cpu.generateDataTuples():
            self.dataTree.insert('', END, values=element)

        
