import os
import subprocess
import tkinter as tk
from integrator import frame  

class Tab(frame.DOSMFrame):
    counter = 0

    def __init__(self, master, logger, **options):
        self.pipes = {}
        self.shared_memory = 0
        super().__init__(master, logger, **options)

    def show(self):
        self.label = tk.Label(self, text="IPC Works! {}".format(self.counter) )
        self.label.pack()
        self.load_shared_memory()
        self.load_pipes()

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        self.counter = self.counter + 1
        self.show()

    def hide(self):
        pass

    def load_pipes(self):
        self.pipes = {};
        lsof = subprocess.Popen(["lsof"], stdout=subprocess.PIPE)
        grep = subprocess.Popen(["grep", "FIFO"], stdin=lsof.stdout, stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "{print $1}"], stdin=grep.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            number = self.pipes.get(line.decode().strip('\n'))
            if number == None:
                self.pipes[line.decode().strip('\n')] = 1
            else:
                self.pipes[line.decode().strip('\n')] = number + 1
            
    def load_shared_memory(self):
        self.shared_memory = 0
        shm = subprocess.Popen(["ipcs", "-m"], stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "NR > 3 { print $5 }"] ,stdin=shm.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            decoded = line.decode().strip('\n')
            if decoded.isnumeric():
                self.shared_memory += int(decoded)
        print(self.shared_memory / 1000000)

