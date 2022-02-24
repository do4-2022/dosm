import tkinter as tk
from ipc import utils
from home import tab_frame

class SummaryFrame(tab_frame.BaseSummaryFrame):
    def __init__(self, master, logger, **options):
        utils.Utils.init_pipes()
        super().__init__(master, logger,)

    def show(self):
        if not self.shown:
            self.semaphore_label = tk.Label(self, text="")
            self.shared_memory_label = tk.Label(self, text="")
            self.pipes_number_label = tk.Label(self, text="")
            self.semaphore_label.pack()
            self.shared_memory_label.pack()
            self.pipes_number_label.pack()
            super().show()

    def update(self, dt):  
        if self.shown:      
            self.semaphore_label["text"] = "Number of semaphores : {}".format(utils.Utils.load_semaphores())
            self.shared_memory_label["text"] = "Total shared  memory usage : {} MB".format(utils.Utils.load_shared_memory() / 1000000)
            self.pipes_number_label["text"] = "Total number of pipes : {}".format(utils.Utils.get_pipes()[1])
