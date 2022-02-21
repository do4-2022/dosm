import psutil as ps
import tkinter as tk
from integrator import base_frame
from logger.logger import Logger
from datetime import datetime


class TabFrame(base_frame.BaseFrame):
    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger
        self.name = 'Utilisateurs connectés'

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def show(self):
        # Define datagrid headings
        columns = {
            "name": "Name",
            "host": "Host",
            "started": "Login date",
            "connexion_pid": "Connexion PID"
        }

        # Init datagrid
        self.datagrid = tk.ttk.Treeview(
            self, columns=list(columns.keys()), show='headings')

        # Set datagrid headings
        for (name, display_name) in columns.items():
            self.datagrid.heading(name, text=display_name)

        self.datagrid.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Init scrollbar
        self.scrollbar = tk.ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.datagrid.yview)
        self.datagrid.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        super().show()

    def update(self, dt):
        if self.shown:
            # Clear data grid
            for item in self.datagrid.get_children():
                self.datagrid.delete(item)

            users = []
            for user in ps.users():
                users.append(
                    (user.name, user.host, datetime.fromtimestamp(user.started), user.pid))
                self.logger.write_log(users[-1])

            # Add data to datagrid
            for user in users:
                self.datagrid.insert('', tk.END, values=user)

    def hide(self):
        self.datagrid.destroy()
        self.scrollbar.destroy()
        super().hide()