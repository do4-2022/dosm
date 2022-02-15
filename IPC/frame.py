import subprocess
import threading
import tkinter as tk
from integrator import frame  
from threading import Thread

class Tab(frame.DOSMFrame):
    working = False

    def __init__(self, master, logger, **options):
        self.pipes = {}
        self.shared_memory = 0
        self.semaphores = 0
        Thread(None, self.load_pipes).start()
        super().__init__(master, logger, **options)

    def show(self):
        self.semaphore_label = tk.Label(self, text="")
        self.shared_memory_label = tk.Label(self, text="")
        self.semaphore_label.pack()
        self.shared_memory_label.pack()
        self.set = tk.ttk.Treeview(self)
        self.set.pack()

        self.set['columns']= ('process', 'pipe_number')
        self.set.column("#0", width=0,  stretch=tk.NO)
        self.set.column("process",anchor=tk.CENTER, width=150)
        self.set.column("pipe_number",anchor=tk.CENTER, width=100)

        self.set.heading("#0",text="",anchor=tk.CENTER)
        self.set.heading("process",text="Process",anchor=tk.CENTER)
        self.set.heading("pipe_number",text="# of pipes",anchor=tk.CENTER)

        self.set.insert(parent='',index='end',iid=0,text='',
        values=('Loading','please wait'))


    def update(self, dt):
        self.load_shared_memory()
        self.load_semaphores()
        self.semaphore_label["text"] = "Number of semaphores : {}".format(self.semaphores)
        self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(self.shared_memory / 1000)

        if not self.working:
            self.working = True
            for index, ( key, value ) in enumerate(self.pipes.items()):
                if self.set.exists(index):
                    self.set.delete(index)
                self.set.insert(parent='',index='end',iid=index, text='',
                values=(key, value))

            self.working = False

    def hide(self):
        pass

    def load_pipes(self):
        lsof = subprocess.Popen(["lsof"], stdout=subprocess.PIPE)
        grep = subprocess.Popen(["grep", "FIFO"], stdin=lsof.stdout, stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "{print $1}"], stdin=grep.stdout, stdout=subprocess.PIPE)

        while self.working:
            pass

        self.working = True
        self.pipes = {}
        for line in awk.stdout.readlines():
            number = self.pipes.get(line.decode().strip('\n'))
            if number == None:
                self.pipes[line.decode().strip('\n')] = 1
            else:
                self.pipes[line.decode().strip('\n')] = number + 1

        self.working = False

        threading.Timer(30, self.load_pipes)
            
    def load_shared_memory(self):
        self.shared_memory = 0
        shm = subprocess.Popen(["ipcs", "-m"], stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "NR > 3 { print $5 }"] ,stdin=shm.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            decoded = line.decode().strip('\n')
            if decoded.isnumeric():
                self.shared_memory += int(decoded)

    def load_semaphores(self):
        self.semaphores = 0
        shm = subprocess.Popen(["ipcs", "-sc"], stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "NR > 3 { print $4 }"] ,stdin=shm.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            decoded = line.decode().strip('\n')
            if len(decoded) > 1:
                self.semaphores += 1
