from os import listdir
from os.path import isfile, join, getsize
from utils import getFileList, format_bytes
from re import compile, match
from datetime import date, datetime
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

  if len(files) == 0:
    click.echo("No logs files found")
    return

  # print the list of files with their size
  click.echo()
  for f in files:
    size = getsize(f"{path}/{f}")
    click.echo(f"  ├ {f} ({format_bytes(size)})")
  click.echo()

@logs.command()
@click.argument('path', type=click.Path(exists=True, readable=True, resolve_path=True))
@click.argument('start', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.argument('end', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--level', default='ALL', help='The level of the logs.', show_default=True)
def get(path, start, end, level):
  """Show the logs with the given level (ALL by default) and the timestamp.

  PATH is the path to the root folder of dosm

  START is the start date of the logs
  
  STOP is the end date of the logs
  """

  # get list of files
  path = f"{click.format_filename(path)}/logs"
  files = getFileList(path)

  if len(files) == 0:
    click.echo("No logs found")
    return

  # find the matching log file name with the given timestamp
  splitted_files = ["-".join(f"{file}".split("-")[:-1]) for file in files]
  filtered_files = [file for file in splitted_files if datetime.fromisoformat(file) >= start and datetime.fromisoformat(file) <= end]
  
  # remove duplicates from the list of files
  non_duplicated_files = list(dict.fromkeys(filtered_files))

  # get content of the files
  concatenated_lines = []
  files_with_revisions = ([file for file in files for non_duplicated_file in non_duplicated_files if file.startswith(non_duplicated_file)])
  regex_level = compile(f"^\[[\d-]* [\d:]*] \[{level}]")
  for file in files_with_revisions:
    with open(f"{path}/{file}", 'r') as file:
      lines = file.readlines()
      if level == "ALL":
        concatenated_lines.extend(lines)
      else:
        concatenated_lines.extend([line for line in lines if match(regex_level, line)])
  
  if len(concatenated_lines) == 0:
    click.echo("No logs found")
    return

  # show the lines
  click.echo("".join(concatenated_lines))
