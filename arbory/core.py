import click

from .__version__ import __version__


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False))
def basic(dirpath):
    """Generate a basic directory tree.

    The specified path must be an existing directory.
    """
    click.echo(dirpath)
