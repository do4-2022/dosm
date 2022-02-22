from integrator.frame import DOSMFrame
from tkinter import *
from tkinter import ttk
import psutil
import math

class Tab(DOSMFrame):
    def __init__(self, master, logger, **options):
        super(Tab, self).__init__(master, logger, **options)

        self.interfaces = psutil.net_if_addrs()
        self.interfaces.pop('lo')

        self.if_stats = dict(psutil.net_if_stats())
        self.if_stats.pop('lo')

        self.if_counters = dict(psutil.net_io_counters(pernic=True, nowrap=True))
        self.if_counters.pop('lo')

        self.selected = None

        self.varStats = StringVar()
        self.varAddress = StringVar()

        self.varRecv = StringVar()
        self.varRecv.set("0 bytes received")

        self.statRecv = StringVar()

        self.varSent = StringVar()
        self.varSent.set("0 bytes sent")

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

        iconrecv = ttk.Label(self, justify="center", text="🡇")
        iconrecv.grid(row=0, column=1)
        bytesrecv = ttk.Label(self, justify="center", textvariable=self.varRecv)
        bytesrecv.grid(row=1, column=1)
        statsrecv = ttk.Label(self, justify="center", textvariable=self.statRecv)
        statsrecv.grid(row=2, column=1)

        iconsent = ttk.Label(self, justify="center", text="🡅")
        iconsent.grid(row=0, column=2)
        bytessent = ttk.Label(self, justify="center", textvariable=self.varSent)
        bytessent.grid(row=1, column=2)
        statssent = ttk.Label(self, justify="center", textvariable=self.statSent)
        statssent.grid(row=2, column=2)

        self.updateValues()

    def update(self, dt):
        self.updateValues()

        #log here

    def hide(self):
        return super().hide()

    def changeSelected(self, event):
        if event:
            self.updateValues()
            self.selected = event.widget.get()
            self.varAddress.set(str(self.getIpAddress(self.selected)))
            self.varStats.set(str(self.getStats(self.selected)))

            self.varSent.set(f"{self.prettyPrintBytes(self.if_counters.get(self.selected).__getattribute__('bytes_sent'))} send")
            self.statSent.set(f"packets sent {self.if_counters.get(self.selected).__getattribute__('packets_sent')}")

            self.varRecv.set(f"{self.prettyPrintBytes(self.if_counters.get(self.selected).__getattribute__('bytes_recv'))} received")
            self.statRecv.set(f"packets received {self.if_counters.get(self.selected).__getattribute__('packets_recv')}")


    def getIpAddress(self, interface):
        return self.interfaces.get(interface)[0].__getattribute__('address')

    def getStats(self, interface):
        return f"Netmask : {self.interfaces.get(interface)[0].__getattribute__('netmask')}\n"\
               + f"Broadcast address : {self.interfaces.get(interface)[0].__getattribute__('broadcast')}"

    def updateValues(self):
        self.if_counters = dict(psutil.net_io_counters(pernic=True, nowrap=True))
        self.if_counters.pop('lo')

    def prettyPrintBytes(self, size_bytes):
        # bout de code pris depuis cette URL https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
        # je vais au moins expliquer ce que fait la fonction ligne par ligne pour montrer que j'ai compris
        if size_bytes == 0:
            return "0 B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))  # On arrondit et convertit en entier l'arrondit de log(s, 1024)
        # on prends un log base 1024 log(x, 1024) car à chaque fois que le nombre d'octets est mis au carré le résultat augmente de 1
        p = math.pow(1024, i)  # donne le nombre de bytes d'une unité
        s = round(size_bytes / p, 2) # conversion de B vers XB
        return "%s %s" % (s, size_name[i])  # on renvoie une string avec le montant et l'unité aproppriée
