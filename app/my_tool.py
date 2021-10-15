
# import click
# from wheel import cli

# @click.group()
# def cli():
#     pass
# @cli.command()
# def hello():
#     click.echo("Hello World")

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

# @cli.command()
# @click.option('-n', '--name', type=str, help='Name to greet', default='World')
# def hello(name):
#     click.echo(f'Hello {name}')

# @cli.command()
# def hello():
#     click.print("Hello World")
#
# if __name__ == '__main__':
#     hello()