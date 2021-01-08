"""Defines tree command functionality.
"""

import os
import pathlib

import click

from arbory.const import KW_CONF_SEL


@click.command()
@click.pass_obj
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False),
    required=False)
@click.option('-f/-F', '--include-files/--no-files', default=True,
    show_default=True)
@click.option('-d', '--depth', type=int, default=1, show_default=True,
    help="Depth to recurse to.")
@click.option('-z', '--show-sizes', is_flag=True,
    help="Show directory and file sizes.")
def tree(obj, dirpath, include_files, depth, show_sizes):
    """Print the file tree of an existing directory."""
    cfg = obj['config']
    sel = cfg['DEFAULT'][KW_CONF_SEL]
    cfg = cfg[sel]
    if not dirpath:
        dirpath = pathlib.Path.cwd()
    for root, dirs, files in os.walk(dirpath):
        dirlevel = root.replace(str(dirpath), '').count(os.sep)
        filelevel = dirlevel + 1
        # Depth of -1 or lower shows entire tree.
        if dirlevel >= 0 and dirlevel > depth:
            continue
        indent = ' ' * 4 * dirlevel
        d_str = os.path.basename(root) + '/'
        fg_col = cfg['dir_color_fg']
        bg_col = cfg['dir_color_bg']
        line = indent + click.style(d_str, fg=fg_col, bg=bg_col)
        if show_sizes:
            line += ' ' * 2 + dir_size(pathlib.Path(root))
        click.echo(line)
        if not include_files or (filelevel >= 0 and filelevel > depth):
            continue
        subindent = ' ' * 4 * filelevel
        for f_str in files:
            fg_col = cfg['file_color_fg']
            line = subindent + click.style(f_str, fg=fg_col)
            if show_sizes:
                line += ' ' * 2 + file_size(pathlib.Path(root) / f_str)
            click.echo(line)


def file_size(path):
    return metric_units(path.stat().st_size)


def dir_size(path):
    return metric_units(sum(
        f.stat().st_size for f in path.glob('**/*') if f.is_file()
    ))


def metric_units(size):
    """Add appropriate units for the file or directory size, given in
    bytes.
    """
    if size // int(1e12):
        return f"{size / 1e12} TB"
    elif size // int(1e9):
        return f"{size / 1e9} GB"
    elif size // int(1e6):
        return f"{size / 1e6} MB"
    elif size // int(1e3):
        return f"{size / 1e3} kB"
    else:
        return f"{size} B"
