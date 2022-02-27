from net import tab_frame
from home import base_summary_frame
from tkinter import ttk
from tkinter import *


class SummaryFrame(tab_frame.TabFrame, base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, name, **options):
        base_summary_frame.BaseSummaryFrame.__init__(self, master, logger, name, **options)
        tab_frame.TabFrame.__init__(self, master, logger, **options)

        self.selected = list(self.interfaces.keys())[0]

    def show(self):
        self.update(0)


        iconrecv = ttk.Label(self, justify="center", text="Download")
        iconrecv.grid(row=0, column=0)

        currentRecv = ttk.Label(self, justify="center", textvariable=self.currentRecv)
        currentRecv.grid(row=1, column=0)
        
        iconsent = ttk.Label(self, justify="center", text="Upload")
        iconsent.grid(row=0, column=1)

        currentSent = ttk.Label(self, justify="center", textvariable=self.currentSent)
        currentSent.grid(row=1, column=1)
