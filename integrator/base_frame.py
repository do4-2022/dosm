import tkinter as tk


class BaseFrame(tk.Frame):
    def __init__(self, master, logger, **options):
        self.logger = logger
        self.name = 'Integrator'
        self.shown = False
        super().__init__(master, **options)

    def show(self):
        self.shown = True

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        self.shown = False