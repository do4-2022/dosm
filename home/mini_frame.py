import tkinter as tk


class MiniFrame(tk.Frame):
    def __init__(self, master, logger, **options):
      self.logger = logger
      super().__init__(master, width=300, height=250, bg="#5D55C1", **options)

    def update(self, dt):
      """
      `dt` is the elapsed delta time since the last update in second
      """
      pass
    
    def hide(self):
      pass