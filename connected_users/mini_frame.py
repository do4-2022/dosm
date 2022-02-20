import psutil as ps
import tkinter as tk
from home import mini_frame
from logger.logger import Logger


class mini_frame(mini_frame.MiniFrame):
    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def show(self):
        self.text = tk.StringVar()

        label = tk.Label(self, textvariable=self.text)

        label.pack(fill=tk.BOTH, expand=True)

    def update(self, dt):
        nb_connected_user = len(ps.users())
        
        self.text.set(f"{nb_connected_user} connected " + ("user" if nb_connected_user < 2 else "users"))

    def hide(self):
        pass
