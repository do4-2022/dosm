import os
import tkinter as tk
from integrator import frame  
import psutil

class Tab(frame.DOSMFrame):
    counter = 0

    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):
        self.label = tk.Label(self, text="IPC Works! {}".format(self.counter) )
        self.label.pack()
        self.load_lsof();

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        self.counter = self.counter + 1
        self.show()

    def hide(self):
        pass

    def load_lsof(self):
        #stdout = os.system('lsof | grep FIFO')
        #print(stdout)
        for proc in psutil.process_iter():
            print(proc.open_files())
