from tkinter import *
from integrator import frame as modelFrame
import psutil


def createFrame(window):   
    # main Frame
    mainFrame = Canvas(window)
    mainFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)

    # text Frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)
    global textFrame
    textFrame = Frame(mainFrame, width=40, height=10, background="red")
    textFrame.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)

    # graph Frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=1)
    graphFrame = Frame(mainFrame, width=40, height=10, background="blue")
    graphFrame.grid(row=0, column=1, columnspan=1, sticky=N+S+E+W)


    # text data
    generateLabel()
    textRefresher()

def generateGlobalCPUText():
    freq = psutil.cpu_freq(percpu=False)
    time = psutil.cpu_times()
    load = psutil.getloadavg()
    stats = psutil.cpu_stats()

    text  = f"Global CPU usage :   \t{psutil.cpu_percent(interval=0.5, percpu=False)}% \n"
    text += f"Global CPU frequence : \t{round(freq.current, 3)}Mhz ( [{freq.min}, {freq.max}] )\n"
    text += f"Number of logical CPU : \t{ psutil.cpu_count( logical=True) } \n"
    text += f"Number of physical CPU : \t{psutil.cpu_count( logical=False)} \n"

    text += f"Average CPU load : \n"
    text += f"\t In the last minute : {load[0]}\n"
    text += f"\t In the last 5 minutes : {load[1]}\n"
    text += f"\t In the last 15 minutes : {load[2]}\n"

    text += f"CPU time spent in mode : \n"
    text += f"\t- user mode : \t\t\t{time.user}s\n"
    text += f"\t- system mode : \t\t\t{time.system}s\n"
    text += f"\t- idle mode : \t\t\t{time.idle}s\n"
    text += f"\t- nice mode (UNIX) : \t\t{time.nice}s\n"
    text += f"\t- iowait mode (Linux) : \t\t{time.iowait}s\n"
    text += f"\t- irq mode (Linux, FreeBSD) : \t{time.irq}s\n"
    text += f"\t- softirq mode (Linux) : \t\t{time.softirq}s\n"
    text += f"\t- steal mode (Linux >= 2.6.11) : \t{time.steal}s\n"
    text += f"\t- guest mode (Linux >= 2.6.24) : \t{time.guest}s\n"
    text += f"\t- guest nice mode (Linux >= 3.2.0) : \t{time.guest_nice}s\n"

    text += f"Stats : \n"
    text += f"\t{stats.ctx_switches} context switches since boot\n"
    text += f"\t{stats.interrupts} interrupts since boot\n"
    text += f"\t{stats.soft_interrupts} software interrupts since boot\n"
    text += f"\t{stats.syscalls} system calls since boot\n"
    

    return text

def generatePerCPUText():
    usage = psutil.cpu_percent(interval=0.5, percpu=True)
    freq = psutil.cpu_freq(percpu=True)
    text = ""
    for i in range(0, psutil.cpu_count( logical=True)) :
        text += f"{i+1} : \n"
        text += f"\tusage : \t\t{usage[i]}% \n"
        text += f"\tcurrent freq : \t{freq[i].current}Mhz \n"
        text += f"\tminimal freq : \t{freq[i].min}Mhz \n"
        text += f"\tmaximal freq : \t{freq[i].max}Mhz \n"
    return text



def generateLabel():
    global textFrame
    Label(textFrame, text="Global CPU information : \n", font='Helvetica 14 bold', justify=LEFT).pack()

    global globalCPULabel
    globalCPULabel = Label(textFrame, text=generateGlobalCPUText(), justify=LEFT)
    globalCPULabel.pack(anchor='w')

    Label(textFrame, text="Information Per CPU : \n", font='Helvetica 14 bold', justify=LEFT).pack()
    
    global perCPULabel
    perCPULabel = Label(textFrame, text=generatePerCPUText(), justify=LEFT)
    perCPULabel.pack(anchor='w')




    
def textRefresher():
    global globalCPULabel
    global perCPULabel
    globalCPULabel.config(text=generateGlobalCPUText())
    perCPULabel.config(text=generatePerCPUText())

    globalCPULabel.after(1000, textRefresher) # every second...