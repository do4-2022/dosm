from logger.utils import get_current_date
from pathlib import Path

class FileManager:

  def __init__(self):
    self.pathPrefix = "logs/"
    self.verify_path()

  def verify_path(self):
    Path(self.pathPrefix).mkdir(parents=True, exist_ok=True)

  def get_log_filepath(self):
    return f"%s%s.log" % (self.pathPrefix, get_current_date())

