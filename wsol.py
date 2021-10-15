
import click
from wheel import cli


@click.group()
def cli():
    pass

@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='WSOL')
def init(name):
    click.echo(f'Hello {name}')

