import subprocess
import threading
import tkinter as tk
from integrator import frame  
from threading import Thread

class Tab(frame.DOSMFrame):
    counter = 0
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

    def update(self, dt):
        self.counter = self.counter + 1
        self.load_shared_memory()
        self.load_semaphores()
        self.semaphore_label["text"] = "Number of semaphores : {}".format(self.semaphores)
        self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(self.shared_memory / 1000)
        self.show()

    def hide(self):
        pass

    def load_pipes(self):
        self.working = True
        self.pipes = {}
        lsof = subprocess.Popen(["lsof"], stdout=subprocess.PIPE)
        grep = subprocess.Popen(["grep", "FIFO"], stdin=lsof.stdout, stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "{print $1}"], stdin=grep.stdout, stdout=subprocess.PIPE)
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
