"""Defines core commands.
"""

import configparser
import os
import pathlib

import click

from .__version__ import __version__
from .tree import tree


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option(version=__version__, prog_name='arbory')
def arb(ctx):
    """Utilities for file tree generation."""
    # Get configuration specifications and add to context.
    ctx.ensure_object(dict)
    ctx.obj['config'] = config_spec()


def config_spec():
    config = configparser.ConfigParser()
    config.read(pathlib.Path(__file__).parent / 'config.ini')
    selected = config['DEFAULT']['selected']
    return config[selected]


arb.add_command(tree)
