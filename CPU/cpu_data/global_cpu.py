from .cpu import CPU
from .time import CPUTime
from .stats import CPUStats
import psutil

class GlobalCPU ():

    def __init__(self):

        self.usages = []
        self.frequencies = []
        self.number_of_logical_cpus = psutil.cpu_count( logical=True)
        self.number_of_physical_cpus = psutil.cpu_count( logical=False)

        self.cpu_list = []

        freq_per_cpu = psutil.cpu_freq(percpu=True)
        for i in range(0,self.number_of_logical_cpus):
            self.cpu_list.append(CPU(freq_per_cpu[i].min, freq_per_cpu[i].max))

        self.loads = []

        # time spent by cpu in specific mode ( in secondes )
        self.time = CPUTime()
        self.stats = CPUStats()



    def update(self):
        self.usages.append(psutil.cpu_percent(interval=0.5, percpu=False))
        self.frequencies.append(psutil.cpu_freq(percpu=False).current)

        usage_per_cpu = psutil.cpu_percent(interval=0.5, percpu=True)
        freq_per_cpu = psutil.cpu_freq(percpu=True)
        for i in range(0, self.number_of_logical_cpus):
            self.cpu_list[i].add_usage(usage_per_cpu[i])
            self.cpu_list[i].add_frequency(freq_per_cpu[i].current)
            
        self.loads.append(psutil.getloadavg()[0] / self.number_of_logical_cpus * 100)

        self.time.update(psutil.cpu_times())
        self.stats.update(psutil.cpu_stats())



    def generateDataTuples(self):
        list = []
        list.append(("Global CPU usage", f"{self.usages[-1]}%"))
        list.append(("Global CPU usage in the last min", f"{self.loads[-1]}%"))
        list.append(("Global CPU frequence", f"{round(self.frequencies[-1],3)}MHz"))
        list.append(("Number of physical CPU", self.number_of_physical_cpus))
        list.append(("Number of logical CPU", self.number_of_logical_cpus))

        list.extend(self.time.generateDataTuples())
        list.extend(self.stats.generateDataTuples())

        list.append(("Per CPU data : ", ""))
        for i in range(0, self.number_of_logical_cpus) :
            list.append((f"  CPU n°{i+1} : ", ""))
            list.extend(self.cpu_list[i].generateDataTuples())

        return list


        
