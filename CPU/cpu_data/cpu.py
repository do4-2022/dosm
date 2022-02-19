
class CPU ():

    def __init__(self, min_freq, max_freq):
        self.usages = []
        self.frequencies = []
        self.min_frequency = min_freq
        self.max_frequency = max_freq

    def add_usage(self, usage):
        self.usages.append(usage)

    def add_frequency(self, frequency):
        self.frequencies.append(frequency)