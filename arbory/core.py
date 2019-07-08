"""Defines core commands.
"""

import configparser
import os
import pathlib

import click

from .__version__ import __version__


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, prog_name='arbory')
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False),
    required=False)
@click.option('-f', '--include-files', default=True, type=bool,
    show_default=True)
def tree(dirpath, include_files):
    """Generate a directory tree.

    The specified path must be an existing directory.
    """
    # Get configuration specifications.
    cfg = config_spec()
    # Check for dirpath argument existence.
    if dirpath is None:
        dirpath = os.getcwd()
    # Make tree.
    for root, dirs, files in os.walk(dirpath):
        level = root.replace(dirpath, '').count(os.sep)
        indent = ' ' * 4 * level
        d_str = os.path.basename(root) + '/'
        fg_col = cfg['dir_color_fg']
        bg_col = cfg['dir_color_bg']
        click.echo(indent + click.style(d_str, fg=fg_col, bg=bg_col))
        if include_files:
            subindent = ' ' * 4 * (level + 1)
            for f_str in files:
                fg_col = cfg['file_color_fg']
                click.echo(subindent + click.style(f_str, fg=fg_col))


def config_spec():
    config = configparser.ConfigParser()
    config.read(pathlib.Path(__file__).parent / 'config.ini')
    selected = config['DEFAULT']['selected']
    return config[selected]
