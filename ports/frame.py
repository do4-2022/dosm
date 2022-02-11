from integrator import frame
import tkinter as tk
from tkinter import ttk
from ports import read

columns = ["local port", "local addr", "remote addr",
           "remote port", "PID", "name", "status", "type"]
colWidth = 100
rowHeight = 20


class PortTab (frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):
        res = read.read_connexions()

        canvas = tk.Canvas(self, width=500, height=500, scrollregion=(0, 0, (len(columns) + 1) *
                           colWidth, len(res) * rowHeight))

        for i in range(len(columns)):
            head = columns[i]
            canvas.create_text(i*colWidth, 0, text=head,  anchor=tk.NW)

        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)

        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        hbar.config(command=canvas.xview)
        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=canvas.yview)

        canvas.config(width=500, height=500)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        print(len(res))
        for item in range(len(res)):
            canvas.create_text(10, (item + 1)*rowHeight,
                               text=item, anchor=tk.NW)

        # canvas

        # scrollbar = ttk.Scrollbar(
        #     self, orient=tk.VERTICAL, command=canvas.yview)
        # canvas.config(yscrollcommand == scrollbar.set)
        # scrollbar.config(command=canvas.yview)
        # scrollbar

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
