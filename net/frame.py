from integrator.frame import DOSMFrame
from tkinter import *
from tkinter import ttk
import psutil

class Tab(DOSMFrame):
    def __init__(self, master, logger, **options):
        super(Tab, self).__init__(master, logger, **options)

        self.interfaces = psutil.net_if_addrs()
        self.interfaces.pop('lo')

        self.if_stats = dict(psutil.net_if_stats())
        self.if_stats.pop('lo')

        self.if_counters = dict(psutil.net_io_counters(pernic=True))
        self.if_counters.pop('lo')

        self.selected = None

        self.varStats = StringVar()
        self.varAddress = StringVar()

        self.varRecv = StringVar()
        self.statRecv = StringVar()

        self.varSent = StringVar()
        self.statSent = StringVar()

    def show(self):
        labelselect = ttk.Label(self, justify="center", text="Please select an interface")
        labelselect.grid(row=0, column=0)

        comboBox = ttk.Combobox(self, justify="center", height=10,
                                state="readonly", values=list(self.interfaces.keys()))

        comboBox.bind('<<ComboboxSelected>>', func=self.changeSelected)
        comboBox.grid(row=1, column=0)

        ipaddress = ttk.Label(self, justify="center", textvariable=self.varAddress)
        ipaddress.grid(row=2, column=0)

        labelstats = ttk.Label(self, justify="center", text="Stats")
        labelstats.grid(row=3, column=0)

        stats = ttk.Label(self, justify="center", textvariable=self.varStats)
        stats.grid(row=4, column=0)

        bytesrecv = ttk.Label(self, justify="center", textvariable=self.varRecv)
        bytesrecv.grid(row=1, column=1)
        statsrecv = ttk.Label(self, justify="center", textvariable=self.statRecv)
        statsrecv.grid(row=2, column=1)

        bytessent = ttk.Label(self, justify="center", textvariable=self.varSent)
        bytessent.grid(row=1, column=2)
        statssent = ttk.Label(self, justify="center", textvariable=self.statSent)
        statssent.grid(row=2, column=2)

        self.animate(self.selected)

    def update(self, dt):
        self.animate(self.selected)

        #log here

    def hide(self):
        return super().hide()

    def changeSelected(self, event):
        if event:
            self.selected = event.widget.get()
            self.varAddress.set(str(self.getIpAddress(self.selected)))
            self.varStats.set(str(self.getStats(self.selected)))

            self.varSent.set(f"{self.if_counters.get(self.selected).__getattribute__('bytes_sent')} bytes send")
            self.statSent.set(f"packets sent {self.if_counters.get(self.selected).__getattribute__('packets_sent')}")

            self.varRecv.set(f"{self.if_counters.get(self.selected).__getattribute__('bytes_recv')} bytes received")
            self.statRecv.set(f"packets received {self.if_counters.get(self.selected).__getattribute__('packets_recv')}")


    def getIpAddress(self, interface):
        return self.interfaces.get(interface)[0].__getattribute__('address')

    def getStats(self, interface):
        return f"Netmask : {self.interfaces.get(interface)[0].__getattribute__('netmask')}\n"\
               + f"Broadcast address : {self.interfaces.get(interface)[0].__getattribute__('broadcast')}"

    def updateValues(self):
        self.if_counters = dict(psutil.net_io_counters(pernic=True))
        self.if_counters.pop('lo')

    def animate(self, selected):
        self.updateValues()
        pass