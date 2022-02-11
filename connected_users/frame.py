import psutil
import tkinter as tk
from integrator import frame


class frame(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        self.logger = logger
        self.master = master

        super().__init__(master, logger, **options)
        master.title("Logged in users")

        self.greet_button = tk.Button(master, text="Refresh", command=self.getConnectedUsers)
        self.greet_button.pack()

    def show(self):
        pass

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        pass

    def getConnectedUsers(self):
        users = psutil.users()

        print(len(users))
        print(users)
        
