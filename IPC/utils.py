import subprocess

def load_pipes():
    lsof = subprocess.Popen(["lsof", "-F", "ptc"], stdout=subprocess.PIPE)
    pipes = {}
    pipes_number = 0
    for line in lsof.stdout.readlines():
        current_line = line.decode().strip('\n')
        if current_line[0] == 'p':
            pid = current_line[1:]
        elif current_line[0] == 'c':
            process = current_line[1:]
        elif current_line.find('FIFO') != -1:
            number = pipes.get((pid, process))
            pipes_number += 1
            if number == None:
                pipes[(pid, process)] = 1
            else:
                pipes[(pid, process)] = number + 1

    return (pipes, pipes_number)

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
