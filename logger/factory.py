from os import getenv
from logger.writer import LoggerWriter

class LoggerFactory:

  def __init__(self):
    filePath = getenv('LOGGER_LOG_PATH')
    if filePath is None:
      filePath = 'app.log'

    self.logWriter = LoggerWriter(filePath)
    self.logWriter.open()

  def appendLog(self, message: str):
    # todo: compute timestamp and module name
    self.logWriter.write(message)
    return
