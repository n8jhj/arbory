"""Define functionality for manipulating the configuration.
"""

import pathlib

import click

from arbory.const import KW_CONF_SEL


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-u', '--use',
    help='Specify a configuration to use.')
@click.option('-a', '--available', is_flag=True,
    help='Show all available configurations.')
@click.option('-o', '--options', is_flag=True,
    help='Show all configuration options.')
@click.pass_obj
def config(obj, use, available, options):
    """Manipulate arbory configuration."""
    cfg = obj['config']
    if use is not None:
        if use in cfg:
            cfg['DEFAULT'][KW_CONF_SEL] = use
            with open(pathlib.Path('arbory') / 'config.ini', 'w') as cf:
                cfg.write(cf)
            click.echo('Configuration selected: {}'.format(use))
        else:
            click.echo('{!r} does not exist.'.format(use))
    elif available:
        output = []
        for conf in cfg:
            output.append(conf)
        click.echo('\n'.join(output))
    elif options:
        output = []
        for opt in cfg['DEFAULT']:
            if opt != KW_CONF_SEL:
                output.append(opt)
        click.echo('\n'.join(output))
    else:
        click.echo('Configuration: {}'.format(cfg['DEFAULT'][KW_CONF_SEL]))
        return
