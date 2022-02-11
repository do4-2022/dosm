import os
import subprocess
import tkinter as tk
from integrator import frame  
import psutil

class Tab(frame.DOSMFrame):
    counter = 0

    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)

    def show(self):
        self.label = tk.Label(self, text="IPC Works! {}".format(self.counter) )
        self.label.pack()
        self.load_lsof();

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        self.counter = self.counter + 1
        self.show()

    def hide(self):
        pass

    def load_lsof(self):
        dictionary = {};
        lsof = subprocess.Popen(["lsof"], stdout=subprocess.PIPE)
        grep = subprocess.Popen(["grep", "FIFO"], stdin=lsof.stdout, stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "{print $1}"], stdin=grep.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            number = dictionary.get(line.decode().strip('\n'))
            if number == None:
                dictionary[line.decode().strip('\n')] = 1
            else:
                dictionary[line.decode().strip('\n')] = number + 1
            
        print(dictionary)
        #stdout = os.system("")