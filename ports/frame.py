from integrator import frame
import tkinter as tk
from tkinter import ttk
from ports import read

columns = ["local port", "local addr", "remote addr",
           "remote port", "PID", "name", "status", "type"]


class PortTab (frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):
        tree = ttk.Treeview(self, columns=columns, show="headings", height=30)
        for head in columns:
            tree.heading(head, text=head)

        #mylist = tk.Listbox(self, yscrollcommand=scrollbar.set)

        res = read.read_connexions()

        print(len(res))
        for item in res:
            tree.insert(
                '', tk.END, values=(item['local_port'], item['local_addr'], item['remote_addr'], item['remote_port'], item['pid'], item['name'], item['status'], item['type']))
        
        
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.config(command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #
        # for i in range(len(header)):
        #     e = tk.Entry(self, font=("Arial", 12))
        #     e.grid(row=0, column=i)
        #     e.insert(tk.END, header[i])

        # for i in range(1,10):
        #     for j in range(3):

        #         e = tk.Entry(self, width=20,
        #                      font=('Arial', 12))

        #         e.grid(row=i, column=j)
        #         e.insert(tk.END, "ah")
