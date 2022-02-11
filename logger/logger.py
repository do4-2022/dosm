from logger.factory import LoggerFactory

class Logger:

  def __init__(self, factory: LoggerFactory):
    self.factory = factory

  def writeLog(self, message: str):
    self.factory.appendLog(message)


