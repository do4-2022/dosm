import os
import psutil

def read_process():
  """Read all process on the system
    Returns a list of process with the following structure : 
    [
      {
        'pid',
        'name',
        'nice',
        'cpu_percent'
        'status',
        'memory_percent',
        'time',
        'command'
      },
      {
        ...
      }, ...
    ]
  """

  process = psutil.process_iter()

  processOut = []

  for proc in process:

    # Parse name and pid

    name = "unknown"
    pid = "unknown"
    if (proc.pid is not None):
      try:
          pid = proc.pid
          name = proc.name()
      except:
        pass

    command = "unknown"
    if(proc.exe is not None):
      try: 
        command = proc.exe()
      except:
        pass

    nice = proc.nice()
    cpu_percent = proc.cpu_percent()
    status = proc.status()
    status = proc.status()
    memory_percent = round(proc.memory_percent(),2)
    time = proc.cpu_times().user
    
    
  # processOut.append({
  #   'pid': pid,
  #   'name': name,
  #   'nice': nice,
  #   'cpu_percent': cpu_percent,
  #   'status': status,
  #   'memory_percent': memory_percent,
  #   'time': time,
  #   'command': command,
  # })

    processOut.append({
      'pid': pid,
      'name': name,
      'nice': nice,
      'cpu_percent': cpu_percent,
      'status': status,
      'memory_percent': memory_percent,
      'time': time,
      'command': command,
    })

  return processOut