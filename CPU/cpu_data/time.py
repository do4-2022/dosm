class CPUTime (): # store spent time in specific mode for the cpu

    def __init__(self):

        # time spent by cpu in specific mode ( in secondes )
        self.system = []
        self.idle = []
        self.user = []
        self.nice = []
        self.iowait = []
        self.irq = []
        self.softirq = []
        self.steal = []
        self.guest = []
        self.guest_nice = []


    def update(self, time):
        
        self.system.append(time.user)
        self.idle.append(time.system)
        self.user.append(time.idle)
        self.nice.append(time.nice)
        self.iowait.append(time.iowait)
        self.irq.append(time.irq)
        self.softirq.append(time.softirq)
        self.steal.append(time.steal)
        self.guest.append(time.guest)
        self.guest_nice.append(time.guest_nice)
    


    def generateDataTuples(self):
        list = []

        list.append(("CPU time spent in mode",  ""))
        list.append(("\t- user mode", f"{self.user[-1]}s" ))
        list.append(("\t- system mode", f"{self.system[-1]}s" ))
        list.append(("\t- idle mode", f"{self.idle[-1]}s" ))
        list.append(("\t- nice mode (UNIX)", f"{self.nice[-1]}s" ))
        list.append(("\t- iowait mode (Linux)", f"{self.iowait[-1]}s" ))
        list.append(("\t- irq mode (Linux, FreeBSD)", f"{self.irq[-1]}s" ))
        list.append(("\t- softirq mode (Linux)", f"{self.softirq[-1]}s" ))
        list.append(("\t- steal mode (Linux >= 2.6.11)", f"{self.steal[-1]}s" ))
        list.append(("\t- guest mode (Linux >= 2.6.24)", f"{self.guest[-1]}s" ))
        list.append(("\t- guest nice mode (Linux >= 3.2.0)", f"{self.guest_nice[-1]}s" ))

        return list