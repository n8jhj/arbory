"""Define functionality for manipulating the configuration.
"""

import click


@click.command()
@click.pass_obj
def config(obj):
    """Manipulate arbory configuration."""
    cfg = obj['config']
    click.echo(cfg['selected'])
