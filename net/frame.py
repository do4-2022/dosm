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

    def show(self):
        noteBook = ttk.Combobox(self, justify="left",
                                height=10, state="normal", values=self.keys)
        noteBook.pack(side=LEFT)


    def update(self, dt):
        return super().update(dt)

    def hide(self):
        return super().hide()