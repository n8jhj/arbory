"""Define functionality for manipulating the configuration.
"""

import pathlib

import click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--use')
@click.option('-a', '--available', is_flag=True)
@click.option('-o', '--options', is_flag=True)
@click.pass_obj
def config(obj, use, available, options):
    """Manipulate arbory configuration."""
    cfg = obj['config']
    if use is not None:
        if use in cfg:
            cfg['DEFAULT']['selected'] = use
            with open(pathlib.Path('arbory') / 'config.ini', 'w') as cf:
                cfg.write(cf)
            click.echo('Configuration selected: {}'.format(use))
        else:
            click.echo('{!r} does not exist.'.format(use))
    elif available:
        for conf in cfg:
            click.echo(conf)
    elif options:
        for opt in cfg['DEFAULT']:
            click.echo(opt)
    else:
        click.echo('Configuration: {}'.format(cfg['DEFAULT']['selected']))
        return
