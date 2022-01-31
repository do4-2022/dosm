import os

def readProcs():
    '''
    Lists the /proc/[pid] folders and returns a list of processes
    '''
    procs = []
    for pid in os.listdir('/proc'):
        if pid.isdigit():
            procs.append(pid)
    return procs

if __name__ == '__main__':
    print(readProcs())