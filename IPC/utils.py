import subprocess
import threading

class Utils():

    pipes = {}
    pipes_number = 0
    working = False
    initialized = False

    def get_pipes():
        while Utils.working:
            pass
        return (Utils.pipes, Utils.pipes_number)

    def init_pipes():
        if not Utils.initialized:
            Utils.initialized = True
            threading.Thread(None, Utils.update_pipes).start()

    def update_pipes():
        lsof = subprocess.Popen(["lsof", "-F", "ptc"], stdout=subprocess.PIPE)
        while Utils.working:
            pass

        Utils.working = True

        Utils.pipes = {}
        Utils.pipes_number = 0
        for line in lsof.stdout.readlines():
            current_line = line.decode().strip('\n')
            if current_line[0] == 'p':
                pid = current_line[1:]
            elif current_line[0] == 'c':
                process = current_line[1:]
            elif current_line.find('FIFO') != -1:
                number = Utils.pipes.get((pid, process))
                Utils.pipes_number += 1
                if number == None:
                    Utils.pipes[(pid, process)] = 1
                else:
                    Utils.pipes[(pid, process)] = number + 1

        Utils.working = False
        threading.Timer(30, Utils.update_pipes)

    def load_shared_memory():
        shared_memory = 0
        shm = subprocess.Popen(["ipcs", "-m"], stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "NR > 3 { print $5 }"] ,stdin=shm.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            decoded = line.decode().strip('\n')
            if decoded.isnumeric():
                shared_memory += int(decoded)
        return shared_memory

    def load_semaphores():
        semaphores = 0
        shm = subprocess.Popen(["ipcs", "-sc"], stdout=subprocess.PIPE)
        awk = subprocess.Popen(["awk", "NR > 3 { print $4 }"] ,stdin=shm.stdout, stdout=subprocess.PIPE)
        for line in awk.stdout.readlines():
            decoded = line.decode().strip('\n')
            if len(decoded) > 1:
                semaphores += 1
        return semaphores
