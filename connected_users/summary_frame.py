import psutil as ps
import tkinter as tk
from home import base_summary_frame
from logger.logger import Logger


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger: Logger, name, **options):
        super().__init__(master, logger, name, **options)
        self.logger = logger

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def show(self):
        self.text = tk.StringVar()

        self.label = tk.Label(self, textvariable=self.text)

        self.label.pack(fill=tk.BOTH, expand=True)

        super().show()

    def update(self, dt):
        nb_connected_user = len(ps.users())
        
        if self.shown:
            self.text.set(f"{nb_connected_user} connected " + ("user" if nb_connected_user < 2 else "users"))

    def hide(self):
        self.label.destroy()
        self.text.destroy()

        super().hide()
