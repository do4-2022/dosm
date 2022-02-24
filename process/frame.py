import json
import sys
import tkinter as tk
from tkinter import ttk

from integrator import frame
from logger.level import LogLevel
from logger.logger import Logger

from process import read

COLUMNS = ('PID','name','nice','cpu percent', 'status','memory percent','time','command')
DATA_FIELDS = ('pid','name','nice','cpu_percent','status','memory_percent','time','command')

class Tab (frame.DOSMFrame):
    """
    This frame is used to display the active network connexions, every update the status of all open ports is dumped as json
    """

    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)

        """
        Initialize default valdues
        """

        self.data = read.read_process()
        self.elements = []
        self.column_sorted = COLUMNS[0]
        self.reverse = False
        self.name = 'Process'

    def show(self):
        # Create the treeview and the scrollbar
        self.tree = ttk.Treeview(self, columns=COLUMNS, show="headings")
        self.vscroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.tag_configure('bg_red', background='red', font=('Arial', 12, 'bold'))
        self.tree.tag_configure('bg_orange', background='orange', font=('Arial', 12, 'bold'))
        # place the elements
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vscroll.pack(side=tk.RIGHT, fill=tk.Y)

        # link the scrollbar to the treeview
        self.tree.configure(yscroll=self.vscroll.set)

        # Create the columns
        for col, i in zip(COLUMNS,range(len(COLUMNS))):
            width=100
            if i==0:
                width=70
            elif i==2 or i==3:
                width=50
            elif i==7:
                width=500
            else :
                width=100
            self.tree.column("# "+str(i+1), width=width, stretch=True)

            self.tree.heading(i, text=col, command=lambda _col=col: self.handle_sort_column(self.tree, _col, False))

        super().show()

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        If the window size has changed, we need to redraw
        """
        if self.shown: 

            self.data = read.read_process()
            self.logger.write_log(json.dumps(self.data), level=LogLevel.INFO)

            # remove old data
            for element in self.elements:
                self.tree.delete(element)
            self.elements.clear()

            # add new data
            for item in self.data:
                value = [item[field] for field in DATA_FIELDS]
                tags = ()
                if item['cpu_percent'] > 25 and item['cpu_percent'] < 50:
                    tags = ('bg_orange')
                elif item['cpu_percent'] >= 50 :
                    tags = ('bg_red')
                element = self.tree.insert('', 'end', values=value, tags=tags)#tags=('fg', 'bg'))
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
        if (col == COLUMNS[0] or col == COLUMNS[2]):
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