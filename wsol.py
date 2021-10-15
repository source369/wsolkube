import click
from app.functions.live_pods import *
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

# @click.command()

# q_env = input ("Env :")
# q_key = input ("Key :")
# q_pwd = getpass.getpass(prompt='Password: ', stream=None)
#
def pods(env):
    print('Environment is %s!' % env)

def _app_nav(q_env,keyring,pwd):
    if q_env.lower() == 'dev':
        env = 'kubectl --kubeconfig $(pwd)/kubeconfig -n writing-solutions-dev'
    elif q_env.lower() == 'qa':
        env = 'kubectl --kubeconfig $(pwd)/kubeconfig -n writing-solutions-qa'
    elif q_env.lower() == 'int':
        env = 'kubectl --kubeconfig $(pwd)/kubeconfig -n writing-solutions-int'
    elif q_env.lower() == 'nft':
        env = 'kubectl --kubeconfig $(pwd)/kubeconfig -n writing-solutions-nft'
    elif q_env.lower() == 'stg':
        env = 'kubectl --kubeconfig $(pwd)/kubeconfig -n writing-solutions-stg'

    _pods(env)

@click.command()
@click.option('-c','--count', default=1, help='Number of greetings.')
@click.option('-e','--env', prompt='Environment', help='What Env : DEV/QE/INT/NFT/STG/PROD')
@click.option('-k','--keyring', prompt='Keyring', help='Enter KeyRing Value')
@click.option('-p','--pwd', prompt='Password', help='Enter your Password ')
def init(count, env, keyring,pwd):
    _app_nav(env,keyring,pwd)


