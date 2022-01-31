import tkinter
import tkinter as tk
from integrator import frame  

class Tab(frame.DOSMFrame):
    counter = 0

    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):
        self.label = tk.Label(self, text="IPC Works! {}".format(self.counter) )
        self.label.pack()

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        self.counter = self.counter + 1
        self.show()

    def hide(self):
        pass