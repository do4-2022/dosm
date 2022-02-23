
class CPU ():

    def __init__(self, min_freq, max_freq):
        self.memory_limit = 100
        self.usages = []
        self.frequencies = []
        self.min_frequency = min_freq
        self.max_frequency = max_freq

    def add_usage(self, usage):
        self.usages.append(usage)
        # clear memory (keep only the "memory_limit" last ones)
        self.usages = self.usages[-self.memory_limit:]

    def add_frequency(self, frequency):
        self.frequencies.append(frequency)
        # clear memory (keep only the "memory_limit" last ones)
        self.frequencies = self.frequencies[-self.memory_limit:]


    def generateDataTuples(self):
        list = []

        list.append(("\tCPU usage :",  f"{self.usages[-1]}%"))
        list.append(("\tCPU frequency :",  f"{self.frequencies[-1]}MHz"))
        list.append(("\tCPU min frequency :",  f"{self.min_frequency}MHz"))
        list.append(("\tCPU max frequency :",  f"{self.max_frequency}MHz"))

        return list
