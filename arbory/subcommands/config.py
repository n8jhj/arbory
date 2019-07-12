"""Define functionality for manipulating the configuration.
"""

import click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--use')
@click.pass_obj
def config(obj, use):
    """Manipulate arbory configuration."""
    cfg = obj['config']
    if use is None:
        click.echo('Configuration: {}'.format(cfg['DEFAULT']['selected']))
        return
    if use in cfg:
        cfg['DEFAULT']['selected'] = use
        with open('arbory\\config.ini', 'w') as cf:
            cfg.write(cf)
        click.echo('Configuration selected: {}'.format(use))
    else:
        click.echo('{!r} does not exist.'.format(use))
