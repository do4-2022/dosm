
from tkinter import StringVar
from tkinter import ttk

from home import base_summary_frame
from ports import read


class SummaryFrame(base_summary_frame.BaseSummaryFrame):
    def __init__(self, master, logger, name, **options):
        super().__init__(master, logger, name, **options)
        self.portsCount = StringVar()
        self.listenCount = StringVar()

    def show(self):
        self.portsLb = ttk.Label(self, textvariable=self.portsCount)
        self.listenLb = ttk.Label(self, textvariable=self.listenCount)
        self.portsLb.pack()
        self.listenLb.pack()

    def update(self, dt):
        result = read.read_connexions()
        self.portsCount.set("Active ports : " + str(len(result)))

        listen = 0
        for item in result:
            if item['status'] == "LISTEN":
                listen += 1

        self.listenCount.set(str(listen) + " listening")
