import tkinter as tk
from tkinter import ttk
from ipc import utils
from integrator import base_frame  
from utils import parse_int_sort

COLUMNS = ("pid", "process", "pipe_number")


class TabFrame(base_frame.BaseFrame):
    pipes_dict = {}
    number_of_pipes = 0
    time_passed = 0

    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        utils.Utils.init_pipes()

        self.name = 'IPC'

        self.number_of_semaphores = 0
        self.shared_memory = 0

        self.column_sorted = COLUMNS[0]
        self.reverse = False
        
        self.semaphore_label = None
        self.shared_memory_label = None
        self.pipes_number_label = None
        self.pipes = None
        self.scrollbar = None

    def show(self):
        self.semaphore_label = tk.Label(self, text="Loading, please wait")
        self.shared_memory_label = tk.Label(self, text="")
        self.pipes_number_label = tk.Label(self, text="")
        
        self.semaphore_label.pack()
        self.shared_memory_label.pack()
        self.pipes_number_label.pack()

        self.pipes = ttk.Treeview(self, columns=COLUMNS, show="headings")
        self.pipes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.pipes.heading("pid", text="PID", anchor=tk.CENTER, 
            command=lambda: self.handle_sort_column('pid', False))
        self.pipes.heading("process", text="Process", anchor=tk.CENTER,
            command=lambda: self.handle_sort_column('process', False))
        self.pipes.heading("pipe_number", text="# of pipes", anchor=tk.CENTER,
            command=lambda: self.handle_sort_column('pipe_number', False))

        self.pipes.column("pid", stretch=True)
        self.pipes.column("process", stretch=True)
        self.pipes.column("pipe_number", stretch=True)

        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.pipes.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.pipes.configure(yscroll=self.scrollbar.set)
        super().show()

    def update(self, dt):
        if self.shown:
            if not utils.Utils.working:
                (self.pipes_dict, self.number_of_pipes) = utils.Utils.get_pipes()
            self.time_passed += dt

            semaphores_number = utils.Utils.load_semaphores()
            shared_memory = utils.Utils.load_shared_memory()

            if self.time_passed >= 60:
                self.time_passed = 0
                self.logger.write_log("Number of semaphores : {}".format(self.number_of_semaphores))
                self.logger.write_log("Shared memory : {} MB".format(self.shared_memory / 1000000))
                self.logger.write_log("Total number of pipes : {}".format(self.number_of_pipes))
            
            if self.semaphore_label:
                self.semaphore_label["text"] = "Number of semaphores : {}".format(semaphores_number)
            if self.shared_memory_label:
                self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(shared_memory / 1000000)
            if self.pipes_number_label:
                self.pipes_number_label["text"] = "Total number of pipes : {}".format(self.number_of_pipes)

            for index, ((pid, process), value) in enumerate(self.pipes_dict.items()):
                if self.pipes:
                    if self.pipes.exists(index):
                        self.pipes.delete(index)
                    self.pipes.insert(parent='',index='end',iid=index, text='', values=(pid, process, value))
            self.sort_column()
                
    def hide(self):
        to_destroy = (
            self.semaphore_label,
            self.shared_memory_label,
            self.pipes_number_label,
            self.pipes,
            self.scrollbar
        )

        for widget in to_destroy:
            if widget:
                widget.destroy()

        super().hide()

    def handle_sort_column(self, column, reverse):
        self.column_sorted = column
        self.reverse = reverse

        # sort the data
        self.sort_column()

        # reverse sort next time
        if self.pipes:
            self.pipes.heading(self.column_sorted,
                command=lambda: self.handle_sort_column(column, not reverse))

    def sort_column(self):
        # get the data to be sorted
        if self.pipes:
            l = [(self.pipes.set(k, self.column_sorted), k) for k in self.pipes.get_children()]

            if (self.column_sorted == "pid" or self.column_sorted == "pipe_number"):
                l.sort(key=parse_int_sort, reverse=self.reverse)
            else:
                l.sort(reverse=self.reverse)

            for index, (_, k) in enumerate(l):
                self.pipes.move(k, '', index)