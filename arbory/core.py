import click


@click.command()
@click.argument('dirpath', type=click.Path(exists=True, file_okay=False))
def basic(dirpath):
    """Generate a basic directory tree.

    The specified path must be an existing directory.
    """
    click.echo(dirpath)
