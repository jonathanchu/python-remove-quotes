import os
import click


@click.command()
@click.option('--filename', '-f', help='Filename to process.')
@click.argument('filename', required=True)
def main(filename):
    """Removes all quotes in a file."""
    read_filename = filename
    orig_filename, ext = os.path.splitext(read_filename)
    write_filename = orig_filename + '_new{}'.format(ext)

    write_buffer = open(write_filename, 'wb')

    with open(read_filename, 'r') as f:
        for line in f:
            line = line.replace('"', '').replace("'", "")
            write_buffer.write(bytes(line, 'UTF-8'))

    f.close()
    write_buffer.close()
