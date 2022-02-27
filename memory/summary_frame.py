import tkinter as tk
from home import base_summary_frame
import psutil 


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, name, **options):
        super().__init__(master, logger, name, **options)
        self.ramUsagePercent = None
        self.ramUsageGB = None
        self.totalRam = None

    def show(self):
        self.totalRam = tk.Label(self, text="Total available : "+str(round((psutil.virtual_memory().total/1000000000),1))+"GB")
        self.totalRam.pack(pady=10,padx=10)

        self.ramUsagePercent = tk.Label(self, text="Used %")
        self.ramUsagePercent.pack(pady=10,padx=10)

        self.ramUsageGB = tk.Label(self, text="Used GB")
        self.ramUsageGB.pack(pady=10,padx=10)

        # super().show()

    def hide(self):
        self.totalRam.destroy()
        self.ramUsageGB.destroy()
        self.ramUsagePercent.destroy()
        super().hide()

    def update(self, dt):
        self.ramUsagePercent.config(text=(str(100-round((psutil.virtual_memory().available * 100 / psutil.virtual_memory().total),1))+'% used'))
        self.ramUsageGB.config(text=(str(round((psutil.virtual_memory().total-psutil.virtual_memory().available)/1000000000,1))+'GB/'+
        str(round((psutil.virtual_memory().total/1000000000),1))+"GB"))