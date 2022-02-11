from integrator import frame
import tkinter as tk
from tkinter import ttk
from ports import read

header = ["port", "PID", "name"]


class PortTab (frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):

        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        mylist = tk.Listbox(self, yscrollcommand=scrollbar.set)


        res = read.read_connexions()


        print(len(res))
        for item in res:
            mylist.insert(tk.END, f"{item['local_port']} | {item['pid']} | {item['name']}")

        mylist.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=mylist.yview)

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
