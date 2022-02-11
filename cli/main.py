from logs import logs
from misc import misc
import click

cli = click.CommandCollection(sources=[logs, misc])
if __name__ == '__main__':
  cli()
