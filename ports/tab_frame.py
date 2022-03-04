import json
import tkinter as tk
from tkinter import ttk

from integrator import base_frame
from logger.level import LogLevel
from logger.logger import Logger

from ports import read
from utils import parse_int_sort

COLUMNS = ("local port", "local addr", "remote addr", "remote port", "PID", "name", "status", "type")
DATA_FIELDS = ("local_port", "local_addr", "remote_addr", "remote_port", "pid", "name", "status", "type")


class TabFrame(base_frame.BaseFrame):
    """
    This frame is used to display the active network connexions, every update the status of all open ports is dumped as json
    """

    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)

        """
        Initialize default valdues
        """

        self.data = read.read_connexions()
        self.elements = []
        self.column_sorted = COLUMNS[0]
        self.reverse = False
        self.name = 'Ports'

    def show(self):
        # Create the treeview and the scrollbar
        self.tree = ttk.Treeview(self, columns=COLUMNS, show="headings")
        self.vscroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)

        # place the elements
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vscroll.pack(side=tk.RIGHT, fill=tk.Y)

        # link the scrollbar to the treeview
        self.tree.configure(yscroll=self.vscroll.set)

        # Create the columns
        for col in COLUMNS:
            self.tree.heading(col, text=col, command=lambda _col=col: self.handle_sort_column(self.tree, _col, False))

        super().show()

    def update(self, dt):
        """
        If the window size has changed, we need to redraw
        """

        if self.shown:
            # gather data
            self.data = read.read_connexions()
            self.logger.write_log(json.dumps(self.data), level=LogLevel.INFO)

            # remove old data
            for element in self.elements:
                self.tree.delete(element)
            self.elements.clear()

            # add new data
            for item in self.data:
                value = [item[field] for field in DATA_FIELDS]
                element = self.tree.insert('', 'end', values=value)
                self.elements.append(element)
            self.sort_column(self.tree, self.column_sorted, self.reverse)

    def hide(self):
        self.elements.clear()
        self.tree.destroy()
        self.vscroll.destroy()
        super().hide()

    def handle_sort_column(self, tv, col, reverse):
        # save the current sort order
        self.column_sorted = col
        self.reverse = reverse

        # sort the data
        self.sort_column(tv, col, reverse)

        # reverse sort next time
        tv.heading(col, command=lambda: self.handle_sort_column(tv, col, not reverse))

    def sort_column(self, tv, col, reverse):
        # get the data to be sorted
        l = [(tv.set(k, col), k) for k in tv.get_children('')]

        # sort the data, if the data is a number, use numerical sort
        if (col == "local port" or col == "remote port"):
            l.sort(key=parse_int_sort, reverse=reverse)
        else:
            l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)