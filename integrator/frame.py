import tkinter as tk


class DOSMFrame(tk.Frame):
    def __init__(self, logger):
        self.logger = logger

    def show(self):
        pass

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        pass