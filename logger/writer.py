from ast import Str


class LoggerWriter:

  def __init__(self, filepath: Str):
    self.filepath = filepath

  def open(self):
    try:
      self.opened = True
      self.file = open(self.filepath, 'a')
    except IOError as error:
      print(error)

  def write(self, str: Str):
    if not self.opened:
      print(f"Cannot write to file %s because it is not opened" % self.filepath)
    
    try:
      self.file.write(f"%s\n" % str)
    except IOError as error:
      print(error)
  
