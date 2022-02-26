# Define the context for the logger
class LoggerContext:

  def __init__(self, name: str, scopes):
    self.name = name # represent the name of the logger
    self.scopes = scopes # represent the scopes of the logger

  def get_name(self):
    return self.name

  def get_scopes(self):
    return " ".join([f" [{scope}]" for scope in self.scopes])

