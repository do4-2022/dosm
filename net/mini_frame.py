import time

from net import frame
import math
import psutil
from home import base_summary_frame
from tkinter import ttk
from tkinter import *


class MiniFrame(frame.Tab, base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

        self.selected = list(self.interfaces.keys())[0]

    def show(self):
        self.update(0)
        time.sleep(1)
        self.update(0)


        iconrecv = ttk.Label(self, justify="center", text="🡇")
        iconrecv.grid(row=0, column=0)

        currentRecv = ttk.Label(self, justify="center", textvariable=self.currentRecv)
        currentRecv.grid(row=1, column=0)
        
        iconsent = ttk.Label(self, justify="center", text="🡅")
        iconsent.grid(row=0, column=1)

        currentSent = ttk.Label(self, justify="center", textvariable=self.currentSent)
        currentSent.grid(row=1, column=1)
