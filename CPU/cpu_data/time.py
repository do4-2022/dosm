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