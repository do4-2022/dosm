import psutil as ps
import tkinter as tk
from tkinter import ttk
from integrator import frame
from logger.logger import Logger
from datetime import datetime


class frame(frame.DOSMFrame):
    def __init__(self, master, logger: Logger, **options):
        self.logger = logger

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        master.title("Logged in users")

        # User columns name and heading text
        columns = {
            "name": "Name",
            "host": "Host",
            "started": "Login date",
            "connexion_pid": "Connexion PID"
        }

        self.datagrid = ttk.Treeview(
            master, columns=list(columns.keys()), show='headings')

        # Set headings
        for column in columns.keys():
            self.datagrid.heading(column, text=columns[column])

        self.datagrid.grid(row=0, column=0, sticky='nsew')

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            master, orient=tk.VERTICAL, command=self.datagrid.yview)
        self.datagrid.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def show(self):
        self.update(0)

    def update(self, dt):
        # Clear data grid
        for item in self.datagrid.get_children():
            self.datagrid.delete(item)

        users = []
        for user in ps.users():
            users.append(
                (user.name, user.host, datetime.fromtimestamp(user.started), user.pid))
            self.logger.write_log(users[len(users) - 1])

        # Add data to datagrid
        for user in users:
            self.datagrid.insert('', tk.END, values=user)

    def hide(self):
        pass
