from integrator import frame
import tkinter as tk
from tkinter import ttk
import sys
from ports import read

columns = ["local port", "local addr", "remote addr",
           "remote port", "PID", "name", "status", "type"]
colWidth = 100

rowHeight = 20

class PortTab (frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.data = read.read_connexions()
        self.elements = []
        self.column_sorted = columns[0]
        self.reverse = False
        self.old_width = 0
        self.vscroll_width = 20

    def update(self, dt):

        if (self.winfo_width() != self.old_width):
            self.show()
            self.elements = []

        self.data = read.read_connexions()

        for e in self.elements:
            self.tree.delete(e)
            self.elements.remove(e)

        for item in self.data:
            out = self.tree.insert(
                '', 'end', values=(item['local_port'], item['local_addr'], item['remote_addr'], item['remote_port'], item['pid'], item['name'], item['status'], item['type']))
            self.elements.append(out)
        self.sort_column(self.tree, self.column_sorted, self.reverse)

        # self.configure(width=self.winfo_width(), height=self.winfo_height())

        print(self.winfo_width())
        # self.tree.configure(width=self.winfo_width())
        print(len(self.data))

    def show(self):

        style = ttk.Style()
        style.configure("Treeview", rowheight=rowHeight)
        # rowHeight = style.lookup("Treeview")
        print( style.element_options("Treeitem.row"))
        print(style.lookup("Treeview.row","height"))

        print("rowHeight: ", rowHeight)
        nb_rows = 25

        print("h", self.winfo_height())

        height = self.winfo_height()
        if (height > 100):
            nb_rows = int((height-rowHeight) / rowHeight)

        self.tree = ttk.Treeview(self, columns=columns,
                                 show="headings", height=nb_rows)
        vscroll = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                command=self.tree.yview)

        print("w", self.vscroll_width)
        print("a", vscroll.winfo_reqwidth())

        cwidth = int(
            (self.winfo_width()-vscroll.winfo_reqwidth())/len(columns))

        if (cwidth < 50):
            cwidth = 100

        nb_col = 50

        for col in columns:
            self.tree.column(col, width=cwidth, stretch=tk.NO)
            self.tree.heading(col, text=col, command=lambda _col=col:
                              self.handle_sort_column(self.tree, _col, False))
        self.tree.grid(row=0, column=0, sticky='nsew')

        vscroll.config(command=self.tree.yview)
        vscroll.grid(row=0, column=1, sticky='ns')

        self.tree.configure(yscroll=vscroll.set)
        self.old_width = self.winfo_width()

    def handle_sort_column(self, tv, col, reverse):

        self.column_sorted = col
        self.reverse = reverse
        self.sort_column(tv, col, reverse)

        # reverse sort next time
        tv.heading(col, command=lambda:
                   self.handle_sort_column(tv, col, not reverse))
        self.sort_column(tv, col, reverse)

    def sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        if (col == "local port" or col == "remote port"):
            l.sort(key=custom_sort, reverse=reverse)
        else:
            l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)


def custom_sort(t):
    if (t[0] != ""):
        return int(t[0])
    else:
        return sys.maxsize
