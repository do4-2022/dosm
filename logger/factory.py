from logger.logger import Logger

class LoggerFactory:

  def createLogger(self) -> Logger:
    return Logger(self)

  def appendLog(self, message: str):
    # todo
    return
