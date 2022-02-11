from ast import Str
from logger.context import LoggerContext
from logger.factory import LoggerFactory
from logger.level import LogLevel


class Logger:

  @staticmethod
  def create_logger(name: Str, factory: LoggerFactory):
    return Logger(name, factory)

  def __init__(self, name: Str, factory: LoggerFactory):
    self.context = LoggerContext(name, [])
    self.factory = factory

  def write_log(self, message: str, level: LogLevel = LogLevel.INFO):
    self.factory.append_log(self.context, level, message)

