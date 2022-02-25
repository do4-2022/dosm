from os import listdir
from os.path import isfile, join, getsize
from utils import getFileList, format_bytes
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

  # get list of files
  path = f"{click.format_filename(path)}/logs"
  files = getFileList(path)

  # print the list of files with their size
  click.echo()
  for f in files:
    size = getsize(f"{path}/{f}")
    click.echo(f"  ├ {f} ({format_bytes(size)})")
  click.echo()
