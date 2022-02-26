# This class implements a writetable interface for logging messages
class LoggerWriter:
  def __init__(self):
    self.file = None

  # Open the log file
  def open(self, filepath):
    try:
      self.file = open(filepath, 'a')
      self.opened = True
    except IOError as error:
      print(error)

  # Close the log file
  def close(self):
    if self.file is not None:
      self.file.close()
    self.opened = False

  # Write a message to the log file
  def write(self, s: str):
    if not self.opened:
      print("Cannot write to file because it is not opened")
    
    if self.file is not None:
      try:
        self.file.write(f"{s}\n")
      except IOError as error:
        print(error)
  
