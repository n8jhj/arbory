"""Defines core commands.
"""

import os

import click

from .__version__ import __version__


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, prog_name='arbory')
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False))
@click.option('-f', '--include-files', default=True, type=bool,
    show_default=True)
def tree(dirpath, include_files):
    """Generate a directory tree.

    The specified path must be an existing directory.
    """
    for root, dirs, files in os.walk(dirpath):
        level = root.replace(dirpath, '').count(os.sep)
        indent = ' ' * 4 * level
        click.echo('{}{}/'.format(indent, os.path.basename(root)))
        if include_files:
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                click.echo('{}{}'.format(subindent, f))
