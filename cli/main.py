import click

VERSION = "1.0.0"

@click.group()
def misc():
  pass

@misc.command()
def version():
  """Show the cli version and exit."""
  click.echo(f"Cli version: {VERSION}")


cli = click.CommandCollection(sources=[misc])
if __name__ == '__main__':
  cli()
