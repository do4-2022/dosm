class LoggerContext:

  def __init__(self, name: str, scopes):
    self.name = name
    self.scopes = scopes

  def get_name(self):
    return self.name

  def get_scopes(self):
    return " ".join([f" [{scope}]" for scope in self.scopes])

