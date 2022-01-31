import tkinter as tk


class DOSMFrame(tk.Frame):
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