import tkinter as tk
from integrator import frame

class DOSMFrame(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        self.logger = logger
        super().__init__(master, **options)

    def show(self):
        pass

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        pass