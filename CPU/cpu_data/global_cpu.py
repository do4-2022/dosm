from .cpu import CPU
from .time import CPUTime
from .stats import CPUStats
import psutil

class GlobalCPU ():

    def __init__(self):

        self.usages = []
        self.frequencies = []
        self.number_of_logical_cpus = psutil.cpu_count( logical=True)
        self.number_of_physical_cpus = psutil.cpu_count( logical=True)

        self.cpu_list = []

        freq_per_cpu = psutil.cpu_freq(percpu=True)
        for i in range(0,self.number_of_logical_cpus):
            self.cpu_list.append(CPU(freq_per_cpu[i].min, freq_per_cpu[i].max))

        self.loads = []

        # time spent by cpu in specific mode ( in secondes )
        self.time = CPUTime()

        self.stats = CPUStats()
        

    def instance(self):
        # Returns the singleton instance.
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


    def update(self):
        self.usages.append(psutil.cpu_percent(interval=0.5, percpu=False))

        usage_per_cpu = psutil.cpu_percent(interval=0.5, percpu=True)
        freq_per_cpu = psutil.cpu_freq(percpu=True)
        for i in range(0, psutil.cpu_count( logical=True)):
            self.cpu_list[i].add_usage(usage_per_cpu[i])
            self.cpu_list[i].add_frequency(freq_per_cpu[i].current)
            
        self.load.append(psutil.getloadavg()[0])

        self.time.update(psutil.cpu_times())
        self.stats.update(psutil.cpu_stats())
        
