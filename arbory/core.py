import click

from .__version__ import __version__


@click.command()
@click.version_option(version=__version__)
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False))
def basic(dirpath):
    """Generate a basic directory tree.

    The specified path must be an existing directory.
    """
    click.echo(dirpath)
