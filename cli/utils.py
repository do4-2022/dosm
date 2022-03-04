from os import listdir
from os.path import isfile, join, getsize

def get_file_list(path):
  try:
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    onlylogs = [f for f in onlyfiles if f.endswith('.log')]
    onlylogs.sort()
    return onlylogs
  except Exception:
    return []

def format_bytes(size):
  power = 2**10
  n = 0
  power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
  while size > power:
      size /= power
      n += 1
  return f"{size}{power_labels[n]+'B'}"
