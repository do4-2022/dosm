
class LoggerWriter:
  def __init__(self):
    self.file = None

  def open(self, filepath):
    try:
      self.file = open(filepath, 'a')
      self.opened = True
    except IOError as error:
      print(error)

  def close(self):
    if self.file is not None:
      self.file.close()
    self.opened = False

  def write(self, s: str):
    if not self.opened:
      print("Cannot write to file because it is not opened")
    
    if self.file is not None:
      try:
        self.file.write(f"{s}\n")
      except IOError as error:
        print(error)
  
