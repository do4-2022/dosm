import threading
import tkinter as tk
from IPC import utils
from integrator import base_frame  
from threading import Thread

class TabFrame(base_frame.BaseFrame):
    pipes_dict = {}
    number_of_pipes = 0

    def __init__(self, master, logger, **options):
        utils.Utils.init_pipes()
        super().__init__(master, logger, **options)

    def show(self):
        self.semaphore_label = tk.Label(self, text="")
        self.shared_memory_label = tk.Label(self, text="")
        self.pipes_number_label = tk.Label(self, text="")
        self.semaphore_label.pack()
        self.shared_memory_label.pack()
        self.pipes_number_label.pack()
        self.pipes = tk.ttk.Treeview(self)
        self.pipes.pack()

        self.pipes['columns']= ('pid', 'process', 'pipe_number')
        self.pipes.column("#0", width=0,  stretch=tk.NO)
        self.pipes.column("pid",anchor=tk.CENTER, width=50)
        self.pipes.column("process",anchor=tk.CENTER, width=150)
        self.pipes.column("pipe_number",anchor=tk.CENTER, width=100)

        self.pipes.heading("#0",text="",anchor=tk.CENTER)
        self.pipes.heading("pid",text="PID",anchor=tk.CENTER)
        self.pipes.heading("process",text="Process",anchor=tk.CENTER)
        self.pipes.heading("pipe_number",text="# of pipes",anchor=tk.CENTER)

        self.pipes.insert(parent='',index='end',iid=0,text='',
        values=('Loading','please wait'))


    def update(self, dt):
        if not utils.Utils.working:
            (self.pipes_dict, self.number_of_pipes) = utils.Utils.get_pipes()
            
        self.semaphore_label["text"] = "Number of semaphores : {}".format(utils.Utils.load_semaphores())
        self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(utils.Utils.load_shared_memory() / 1000000)
        self.pipes_number_label["text"] = "Total number of pipes : {}".format(self.number_of_pipes)

        for index, ( (pid, process), value ) in enumerate(self.pipes_dict.items()):
            if self.pipes.exists(index):
                self.pipes.delete(index)
            self.pipes.insert(parent='',index='end',iid=index, text='',
            values=(pid, process, value))
            
    def hide(self):
        pass