from logger.factory import LoggerFactory

class Logger:

  @staticmethod
  def createLogger(factory: LoggerFactory):
    return Logger(factory)

  def __init__(self, factory: LoggerFactory):
    self.factory = factory

  def writeLog(self, message: str):
    self.factory.appendLog(message)


