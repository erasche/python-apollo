import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadUserById')
@click.argument("userId")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, userId):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.loadUserById(userId)
