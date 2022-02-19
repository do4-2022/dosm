class CPUStats (): # Number of actions since boot

    def __init__(self):

        
        self.ctx_switches = []     # context switches since boot
        self.interrupts = []       # interrupts since boot
        self.soft_interrupts = []  # software interrupts since boot
        self.syscalls = []         # system calls since boot



    def update(self, stats):
        self.ctx_switches.append(stats.ctx_switches)
        self.interrupts.append(stats.interrupts)
        self.soft_interrupts.append(stats.soft_interrupts)
        self.syscalls.append(stats.syscalls)