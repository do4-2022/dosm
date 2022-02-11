from os import getenv
from logger.context import LoggerContext
from logger.level import LogLevel
from logger.writer import LoggerWriter
from datetime import datetime


class LoggerFactory:

  def __init__(self):
    filePath = getenv('LOGGER_LOG_PATH')
    if filePath is None:
      filePath = 'app.log'

    self.log_writer = LoggerWriter(filePath)
    self.log_writer.open()

  def get_current_time(self):
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

  def append_log(self, context: LoggerContext, level: LogLevel, message: str):
    self.log_writer.write(f"[%s] [%s] [%s]%s %s" % (self.get_current_time(), level, context.get_name(), context.get_scopes(), message))
    return
