from ast import Str


class LoggerContext:

  def __init__(self, name: Str, scopes):
    self.name = name
    self.scopes = scopes

  def get_name(self):
    return self.name

  def get_scopes(self):
    return " ".join([(f" [%s]" % scope) for scope in self.scopes])

