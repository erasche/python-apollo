import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setNames')
@click.argument("features")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, features):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setNames(features)
