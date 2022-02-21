import threading
import tkinter as tk
from IPC import utils
from integrator import frame  
from threading import Thread

class Tab(frame.DOSMFrame):
    working = False

    def __init__(self, master, logger, **options):
        self.pipes = {}
        self.number_pipes = 0
        self.shared_memory = 0
        self.semaphores = 0
        Thread(None, self.pipe_thread).start()
        super().__init__(master, logger, **options)

    def show(self):
        self.semaphore_label = tk.Label(self, text="")
        self.shared_memory_label = tk.Label(self, text="")
        self.pipes_number_label = tk.Label(self, text="")
        self.semaphore_label.pack()
        self.shared_memory_label.pack()
        self.pipes_number_label.pack()
        self.set = tk.ttk.Treeview(self)
        self.set.pack()

        self.set['columns']= ('pid', 'process', 'pipe_number')
        self.set.column("#0", width=0,  stretch=tk.NO)
        self.set.column("pid",anchor=tk.CENTER, width=50)
        self.set.column("process",anchor=tk.CENTER, width=150)
        self.set.column("pipe_number",anchor=tk.CENTER, width=100)

        self.set.heading("#0",text="",anchor=tk.CENTER)
        self.set.heading("pid",text="PID",anchor=tk.CENTER)
        self.set.heading("process",text="Process",anchor=tk.CENTER)
        self.set.heading("pipe_number",text="# of pipes",anchor=tk.CENTER)

        self.set.insert(parent='',index='end',iid=0,text='',
        values=('Loading','please wait'))


    def update(self, dt):
        self.shared_memory = utils.load_shared_memory() 
        self.semaphores = utils.load_semaphores()
        self.semaphore_label["text"] = "Number of semaphores : {}".format(self.semaphores)
        self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(self.shared_memory / 1000000)
        self.pipes_number_label["text"] = "Total number of pipes : {}".format(self.number_pipes)

        if not self.working:
            self.working = True
            for index, ( (pid, process), value ) in enumerate(self.pipes.items()):
                if self.set.exists(index):
                    self.set.delete(index)
                self.set.insert(parent='',index='end',iid=index, text='',
                values=(pid, process, value))

            self.working = False

    def hide(self):
        pass

    def pipe_thread(self):
        while self.working:
            pass

        self.working = True
        (self.pipes, self.number_pipes) = utils.load_pipes()
        self.working = False
        threading.Timer(30, self.pipe_thread)
   