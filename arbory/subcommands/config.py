"""Define functionality for manipulating the configuration.
"""

import click

from arbory.config_spec import config_spec


@click.command()
@click.pass_obj
def config(obj):
    """Manipulate arbory configuration."""
    cfg = obj['config']
    click.echo(cfg['selected'])
