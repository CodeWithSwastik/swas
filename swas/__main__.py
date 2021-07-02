import click

from .executor import execute, shell

@click.command()
@click.option('-c', '--code')
@click.argument(
    'src',
    type=click.Path(exists=True, dir_okay=False),
    required=False
)
def main(src, code):
    if code is None:
        if src is None:
            shell()
            return
        else:
            with open(src) as f:
                code = f.read()

    execute(code)

if __name__ == '__main__':
    main()
