from integrator.frame import DOSMFrame
from tkinter import *
from tkinter import ttk
import psutil

#TODO
#   -combo list with interfaces
#   -draw switchband usage and find a library to do so..


class Tab(DOSMFrame):
    def __init__(self, master, logger, **options):
        super(Tab, self).__init__(master, logger, **options)

        self.interfaces = psutil.net_if_addrs()
        self.interfaces.pop('lo')

        self.keys = []
        for key in self.interfaces.keys():
            self.keys.append(key)
        self.varAddress = StringVar()
        self.selected = self.keys[0]

    def show(self):
        comboBox = ttk.Combobox(self, justify="left", height=10, state="readonly", values=self.keys)
        comboBox.bind('<<ComboboxSelected>>', func=self.changeSelected)
        comboBox.pack(side=LEFT)
        ipaddress = ttk.Label(self, justify="left", textvariable=self.varAddress)
        ipaddress.pack(side=LEFT)

    def update(self, dt):
        return super().update(dt)

    def hide(self):
        return super().hide()

    def changeSelected(self, event):
        if event:
            self.selected = event.widget.get()
            self.varAddress.set(str(self.getIpAddress(self.selected)))

    def getIpAddress(self, interface):
        return self.interfaces.get(interface)[0].__getattribute__('address')
