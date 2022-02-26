from logger.context import LoggerContext
from logger.file_manager import FileManager
from logger.level import LogLevel
from logger.writer import LoggerWriter
from logger.utils import get_current_time


# This is the main entry point for logging
# This class is responsible of creating a logger and writing it to a file
class LoggerFactory:

  def __init__(self):
    self.file_manager = FileManager(self.log_file_change) # Create the file manager
    self.log_writer = LoggerWriter() # Create the logger writer

    self.file_manager.verify_path() # Verify the path
    self.file_manager.find_current_revision() # Find the current revision

  def append_log(self, context: LoggerContext, level: str, message: str):
    self.log_writer.write(f"[{get_current_time()}] [{level}] [{context.get_name()}] {context.get_scopes()} {message}")

  def log_file_change(self):
    self.log_writer.close()
    self.log_writer.open(self.file_manager.get_log_filepath())
