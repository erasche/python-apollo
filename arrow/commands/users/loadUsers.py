import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadUsers')

@click.option(
    "--email",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, email=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.loadUsers(email=email)
