import psutil as ps
import tkinter as tk
from integrator import frame
from logger.logger import Logger
from datetime import datetime


class Tab(frame.DOSMFrame):
    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger

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
        scrollbar = tk.ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.datagrid.yview)
        self.datagrid.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def update(self, dt):
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
        pass
