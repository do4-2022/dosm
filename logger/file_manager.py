from logger.utils import get_current_date
from pathlib import Path
from os import path
from config import LOGGER_MAX_FILE_SIZE


# This class is used to create a log file and manage revision
# A revision is created when the size of the log file is greater than 5mb
class FileManager:

  def __init__(self, on_file_change):
    self.pathPrefix = "logs/"
    self.revision = 1
    self.current_date = get_current_date()
    self.on_file_change = on_file_change # represent the function to call when a revision is changed

  def verify_path(self):
    Path(self.pathPrefix).mkdir(parents=True, exist_ok=True)

  # Find the current revision (format: date-revision.log)
  def find_current_revision(self):
    while self.check_file_size():
      self.revision += 1
    self.on_file_change()

  def get_log_filepath(self):
    return f"{self.pathPrefix}{self.current_date}-{self.revision}.log"

  def check_file_size(self):
    if not path.exists(self.get_log_filepath()):
      return False

    size = path.getsize(self.get_log_filepath())
    return size > LOGGER_MAX_FILE_SIZE

