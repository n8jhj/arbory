"""Defines tree command functionality.
"""

import os

import click

from arbory.const import KW_CONF_SEL


@click.command()
@click.pass_obj
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False))
@click.option('-f/-F', '--include-files/--no-files', default=True,
    show_default=True)
@click.option('-d', '--depth', type=int, default=3, show_default=True,
    help="Depth to recurse to.")
def tree(obj, dirpath, include_files, depth):
    """Make file tree.

    The specified path must be an existing directory.
    """
    cfg = obj['config']
    sel = cfg['DEFAULT'][KW_CONF_SEL]
    cfg = cfg[sel]
    for root, dirs, files in os.walk(dirpath):
        level = root.replace(dirpath, '').count(os.sep)
        # Depth of -1 or lower shows entire tree.
        if level >= 0 and level > depth:
            continue
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
