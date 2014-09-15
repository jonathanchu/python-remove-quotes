import click


@click.command()
@click.option('--filename', '-f', is_flag=True, help='Filename to process.')
@click.argument('filename', required=True)
def main(name, filename):
    """Removes all quotes in a file."""
    pass
