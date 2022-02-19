from os import listdir
from os.path import isfile, join, getsize
import click


@click.group()
def logs():
  pass

@logs.command()
@click.argument('path', type=click.Path(exists=True, readable=True, resolve_path=True))
def show_files(path):
  """Show all the logs files and exit.

  PATH is the path to the root folder of dosm
  """

  path = f"%s/logs" % click.format_filename(path)
  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  onlylogs = [f for f in onlyfiles if f.endswith('.log')]
  onlylogs.sort()

  click.echo()
  for f in onlylogs:
    size = getsize(f"%s/%s" % (path, f))
    click.echo(f"  ├ %s (%s)" % (f, format_bytes(size)))
  click.echo()

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"%d%s" % (size, power_labels[n]+'B')
