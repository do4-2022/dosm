class CPUStats (): # Number of actions since boot

    def __init__(self):
        self.memory_limit = 100
        self.ctx_switches = []     # context switches since boot
        self.interrupts = []       # interrupts since boot
        self.soft_interrupts = []  # software interrupts since boot
        self.syscalls = []         # system calls since boot



    def update(self, stats):
        self.ctx_switches.append(stats.ctx_switches)
        self.interrupts.append(stats.interrupts)
        self.soft_interrupts.append(stats.soft_interrupts)
        self.syscalls.append(stats.syscalls)
        
        # clear memory (keep only the "memory_limit" last ones)
        self.ctx_switches = self.ctx_switches[-self.memory_limit:]
        self.interrupts = self.interrupts[-self.memory_limit:]
        self.soft_interrupts = self.soft_interrupts[-self.memory_limit:]
        self.syscalls = self.syscalls[-self.memory_limit:]
        

    def generateDataTuples(self):
        list = []

        list.append(("Number of",  "", ))
        list.append(("\t- context switches since boot", self.ctx_switches[-1]))
        list.append(("\t- interrupts since boot", self.interrupts[-1]))
        list.append(("\t- software interrupts since boot", self.soft_interrupts[-1]))
        list.append(("\t- system calls since boot", self.syscalls[-1]))

        return list
