import os
import psutil


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

    connextions = psutil.net_connections()

    for con in connextions:
        print(con.pid,con.laddr)



    # print(psutil.net_connections())
    # print(readProcs())