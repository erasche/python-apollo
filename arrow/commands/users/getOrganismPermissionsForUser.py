import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('getOrganismPermissionsForUser')
@click.argument("user", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, user):
    """Display a user's organism permissions
    """
    return ctx.gi.users.getOrganismPermissionsForUser(user)
