from ast import Str


class LoggerWriter:

  def __init__(self):
    self.file = None

  def open(self, filepath: Str):
    try:
      self.opened = True
      self.file = open(filepath, 'a')
    except IOError as error:
      print(error)

  def close(self):
    if not self.file is None:
      self.file.close()
    self.opened = False

  def write(self, str: Str):
    if not self.opened:
      print(f"Cannot write to file %s because it is not opened" % self.filepath)
    
    try:
      self.file.write(f"%s\n" % str)
    except IOError as error:
      print(error)
  
