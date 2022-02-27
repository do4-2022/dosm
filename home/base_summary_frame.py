import tkinter as tk

from integrator import base_frame


class BaseSummaryFrame(tk.LabelFrame):
  def __init__(self, master, logger, name, **options):
    super().__init__(master, width=300, height=250, text=name, **options)
    
    self.logger = logger
    self.shown = False

  def show(self):
    base_frame.BaseFrame.show(self)

  def update(self, dt):
    base_frame.BaseFrame.update(self, dt)

  def hide(self):
    base_frame.BaseFrame.hide(self)


class EmptySummaryFrame(BaseSummaryFrame):
  def __init__(self, master, logger, name, **options):
    super().__init__(master, logger, name, **options)
    tk.Label(self, text="Not yet integrated").pack(fill="both", expand=True)
