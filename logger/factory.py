from os import getenv
from logger.context import LoggerContext
from logger.file_manager import FileManager
from logger.level import LogLevel
from logger.writer import LoggerWriter
from logger.utils import get_current_time


class LoggerFactory:

  def __init__(self):
    self.file_manager = FileManager()
    self.log_writer = LoggerWriter(self.file_manager.get_log_filepath())
    self.log_writer.open()

  def append_log(self, context: LoggerContext, level: LogLevel, message: str):
    self.log_writer.write(f"[%s] [%s] [%s]%s %s" % (get_current_time(), level, context.get_name(), context.get_scopes(), message))
    return
