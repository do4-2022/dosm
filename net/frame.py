from integrator.frame import DOSMFrame
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil

#TODO
#   -combo list with interfaces
#   -draw switchband usage and find a library to do so..


class Tab(DOSMFrame):
    def __init__(self, master, logger, **options):
        super(Tab, self).__init__(master, logger, **options)

        self.interfaces = psutil.net_if_addrs()
        self.interfaces.pop('lo')

        self.if_stats = dict(psutil.net_if_stats())
        self.if_stats.pop('lo')

        for key in self.if_stats.keys():
            self.if_stats[key] = [0 for x in range(0, 10)]

        self.selected = None
        self.axes = None

        self.varStats = StringVar()
        self.varAddress = StringVar()

    def show(self):
        labelselect = ttk.Label(self, justify="center", text="Please select an interface")
        labelselect.grid(row=0, column=0)

        comboBox = ttk.Combobox(self, justify="center", height=10,
                                state="readonly", values=list(self.interfaces.keys()))

        comboBox.bind('<<ComboboxSelected>>', func=self.changeSelected)
        comboBox.grid(row=1, column=0)

        ipaddress = ttk.Label(self, justify="center", textvariable=self.varAddress)
        ipaddress.grid(row=2, column=0)

        labelstats = ttk.Label(self, justify="center", text="Stats")
        labelstats.grid(row=3, column=0)

        stats = ttk.Label(self, justify="center", textvariable=self.varStats)
        stats.grid(row=4, column=0)

        figure = plt.Figure(figsize=(6, 5), dpi=100)
        diagram = FigureCanvasTkAgg(figure=figure, master=self)
        diagram.get_tk_widget().grid(column=1)
        self.axes = figure.add_subplot(111)
#        Y = [0.2, 0.4, 0.6, 0.8, 1]
        self.animate(self.selected)

    def update(self, dt):
        self.animate(self.selected)

        #log here

    def hide(self):
        return super().hide()

    def changeSelected(self, event):
        if event:
            self.selected = event.widget.get()
            self.varAddress.set(str(self.getIpAddress(self.selected)))
            self.varStats.set(str(self.getStats(self.selected)))

    def getIpAddress(self, interface):
        return self.interfaces.get(interface)[0].__getattribute__('address')

    def getStats(self, interface):
        return f"Netmask : {self.interfaces.get(interface)[0].__getattribute__('netmask')}\n"\
               + f"Broadcast address : {self.interfaces.get(interface)[0].__getattribute__('broadcast')}"

    def updateValues(self):
        fetched = psutil.net_if_stats()
        for key in self.if_stats:
            self.if_stats[key].append(fetched.get(key).__getattribute__('speed'))
            self.if_stats.get(key).pop(0)


    def animate(self, interface):
        self.axes.clear()
        self.updateValues()

        self.axes.plot(self.if_stats.get(self.selected), range(0, 10), linestyle='dotted', color='r')
        #TODO
        #foreach val
            #print into matplotlib
        pass