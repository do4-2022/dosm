from datetime import datetime
import json
import tkinter as tk
from tkinter import ttk

from integrator import base_frame
from logger.level import LogLevel
from logger.logger import Logger
from login_history import extractor
from utils import parallel_run

TABLE_COLUMNS = ('user', 'tty', 'ip', 'date', 'state/loggedout', 'uptime')

class TabFrame(base_frame.BaseFrame):
    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)

        self.name = 'Login History'
        self.data = []
        self.sort_by = 'date'
        self.sort_reverse = False
        self.waiting_label = None
        self.tree_view = None
        self.scroll_bar = None

    def update_tree_view(self):
        if(self.tree_view):
            #Delete previous data
            for entry in self.tree_view.get_children():
                self.tree_view.delete(entry)

            #Insert new data sorted
            for user in self.data["entries"]:
                value = [val for val in user.values()]
                self.tree_view.insert('', 'end', values=value)

    def show(self):
        #Create a waiting label
        if not self.waiting_label:
            self.waiting_label = tk.Label(self, text='Loading data...')
            self.waiting_label.pack(fill=tk.BOTH, expand=True)

        #Loading data
        parallel_run(extractor.get_logins_list, self.set_data)

        #Call parent show method
        super().show()

    def set_data(self, data):
        if self.shown:
            if self.waiting_label:
                self.waiting_label.destroy()
                self.waiting_label = None

            #Create tree view
            if not self.tree_view:
                self.tree_view = ttk.Treeview(self, columns=TABLE_COLUMNS, show="headings")
                self.tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            #Create scroll bar
            if not self.scroll_bar:
                self.scroll_bar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree_view.yview)
                self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
                
            #Attach scrollbar to tree view
            self.tree_view.configure(yscrollcommand=self.scroll_bar.set)

            #Create column entries
            for entry in TABLE_COLUMNS:
                self.tree_view.heading(entry, text=entry, command=lambda col=entry: self.handle_sort(col))

            #Format date
            self.data = data
            for entry in self.data["entries"]:
                entry["date"] = datetime.strftime(entry["date"], "%a %b %d %H:%M:%S %Y")
            
            #Log the data
            self.logger.write_log(json.dumps(self.data) ,level=LogLevel.INFO)

            #Update data and sort by date by default
            self.handle_sort('date')

    def hide(self):
        #Destroy elements
        if self.waiting_label:
            self.waiting_label.destroy()
            self.waiting_label = None

        if self.tree_view:
            self.tree_view.destroy()
            self.tree_view = None

        if self.scroll_bar:
            self.scroll_bar.destroy()
            self.scroll_bar = None
        super().hide()

    #Handle sort when user click on columns
    def handle_sort(self, col):
        #Reset previous sorted col
        if self.tree_view:
            self.tree_view.heading(self.sort_by, text=self.sort_by)

        #If previous was clicked reverse order, if another one was clicked reset order and change sorting value
        if self.sort_by == col:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_by = col
            self.sort_reverse = False

        if(self.sort_by == 'date'):
            #Sort the data by date
            self.data["entries"].sort(key=lambda entry: datetime.strptime(entry['date'], "%a %b %d %H:%M:%S %Y"), reverse=self.sort_reverse)
        else:
            #Sort the data
            self.data["entries"].sort(key=lambda entry: entry[self.sort_by], reverse=self.sort_reverse)

        #Update tree view
        self.update_tree_view()

        #Add text on sorted value
        if self.tree_view:
            if(self.sort_reverse):
                self.tree_view.heading(col, text=col + " (descending)")
            else:
                self.tree_view.heading(col, text=col + " (ascending)")