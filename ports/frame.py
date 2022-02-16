import json
import sys
import tkinter as tk
from tkinter import ttk

from integrator import frame
from logger.level import LogLevel
from logger.logger import Logger

from ports import read

columns = ["local port", "local addr", "remote addr",
           "remote port", "PID", "name", "status", "type"]
row_height = 20


class PortTab (frame.DOSMFrame):
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
        self.column_sorted = columns[0]
        self.reverse = False
        self.old_width = 0
        self.vscroll_width = 20

    def update(self, dt):
        """
        If the window size has changed, we need to redraw
        """

        if (self.winfo_width() != self.old_width):
            self.logger.write_log(
                "Window has been resized, redrawing frame", level=LogLevel.DEBUG)
            self.show()
            self.elements = []

        # gather data

        self.data = read.read_connexions()

        # here we’re modyfing the data rather than recreating the container to avoid flickering and loosing the scroll position

        # delete old elements

        for e in self.elements:
            self.tree.delete(e)
            self.elements.remove(e)

        # add new elements

        for item in self.data:

            self.logger.write_log(json.dumps(item), level=LogLevel.INFO)

            out = self.tree.insert(
                '', 'end', values=(item['local_port'], item['local_addr'], item['remote_addr'], item['remote_port'], item['pid'], item['name'], item['status'], item['type']))
            self.elements.append(out)
        self.sort_column(self.tree, self.column_sorted, self.reverse)

    def show(self):

        # Set the row height to a known value

        style = ttk.Style()
        style.configure("Treeview", rowheight=row_height)

        # Calculate the number of rows that can be displayed, if the window is sized depending on the size of the frame, we use 25 rows as a default

        nb_rows = 25
        height = self.winfo_height()
        if (height > 100):
            nb_rows = int((height-row_height) / row_height)

        # Create the treeview and the scrollbar

        self.tree = ttk.Treeview(self, columns=columns,
                                 show="headings", height=nb_rows)
        vscroll = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                command=self.tree.yview)

        # Calculate the width of a column based on the width of the window, 100 if the window is not initialized

        column_width = 100

        if (self.winfo_width() > 100):
            column_width = int(
                (self.winfo_width()-vscroll.winfo_reqwidth())/len(columns))

        # Create the columns

        for col in columns:
            self.tree.column(col, width=column_width, stretch=tk.NO)
            self.tree.heading(col, text=col, command=lambda _col=col:
                              self.handle_sort_column(self.tree, _col, False))

       # place the elements

        self.tree.grid(row=0, column=0, sticky='nsew')
        vscroll.grid(row=0, column=1, sticky='ns')

        # bind the scrollbar to the treeview

        vscroll.config(command=self.tree.yview)
        self.tree.configure(yscroll=vscroll.set)

        self.old_width = self.winfo_width()

    def handle_sort_column(self, tv, col, reverse):

        # save the current sort order

        self.column_sorted = col
        self.reverse = reverse

        # sort the data

        self.sort_column(tv, col, reverse)

        # reverse sort next time

        tv.heading(col, command=lambda:
                   self.handle_sort_column(tv, col, not reverse))

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


# Return the parsed number, if the string is not a number, return the maximum integer value
def parse_int_sort(t):
    try:
        if (t[0] != ""):
            return int(t[0])
        else:
            return sys.maxsize
    except:
        return sys.maxsize
