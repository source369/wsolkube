import click
from wheel import cli


@click.group()
def main():
    """
    Simple CLI Tool for querying KubeCTL
    """
    pass

# @cli.command()
# @click.option('-n', '--name', type=str, help='Name to greet', default='WSOL')
# def init(name):
#     click.echo(f'Hello {name}')

# @click.command()
# @click.option('-c','--count', default=1, help='Number of greetings.')
# @click.option('-n','--name', prompt='Your name', help='The person to greet.')
# def init(count, name):
#     for x in range(count):
#         click.echo('Hello %s!' % name)

@click.command()
@click.option('-c','--count', default=1, help='Number of greetings.')
@click.option('-n','--name', prompt='Your name', help='The person to greet.')
def init(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)