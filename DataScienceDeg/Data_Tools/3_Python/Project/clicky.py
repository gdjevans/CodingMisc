import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', 'helvar', prompt='Your name',help='The person to greet.')
@click.option('--env',type=click.Choice(['dev', 'prod']),help='your environment')
@click.option('--password', prompt=True, hide_input=True,confirmation_prompt=True)
def hello(count, helvar, env, password):
    """Simple program that greets NAME for a total of COUNT times."""
    print(password)
    for x in range(count):
        click.echo('Hello %s!' % helvar)
    if env == "prod":
        print("this is production")

if __name__ == '__main__':
    hello()