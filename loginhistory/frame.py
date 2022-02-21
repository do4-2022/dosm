from datetime import datetime
import tkinter as tk
from tkinter import RIGHT, ttk
from integrator import frame
from loginhistory import extractor

table_columns = ('user', 'tty', 'ip', 'date', 'state/loggedout', 'uptime')

class LoginHistoryFrame(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

        self.name = 'Login History'
        self.data = extractor.get_logins_list()
        self.sort_by = 'date'
        self.sort_reverse = True

    def show(self):

        #Create tree view 
        self.tree_view = ttk.Treeview(self, columns=table_columns, show="headings")

        #Create scroll bar
        self.scroll_bar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree_view)

        #Pack elements
        self.tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll_bar.pack(side=RIGHT, fill=tk.Y)

        #Attach scrollbar to tree view
        self.tree_view.configure(yscrollcommand=self.scroll_bar.set)

        #Create column entries
        for entry in table_columns:
            self.tree_view.heading(entry, text=entry)

        super().show()
    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """

        #Update only if on screen
        if (self.shown):
            self.data = extractor.get_logins_list()

            #Sort the data
            self.data["entries"].sort(key=lambda entry: entry[self.sort_by], reverse=self.sort_reverse)

            #Delete previous data
            for entry in self.tree_view.get_children():
                self.tree_view.delete(entry)

            #Insert new data sorted
            for user in self.data["entries"]:
                value = [val for val in user.values()]
                self.tree_view.insert('', 'end', values=value)
        pass

    def hide(self):

        self.tree_view.destroy()
        self.scroll_bar.destroy()
        super.hide()

        pass