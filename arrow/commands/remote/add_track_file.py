import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('add_track_file')
@click.argument("organism_id", type=str)
@click.argument("track_data", type=click.File('rb+'))
@click.argument("track_config", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, track_data, track_config):
    """Adds a tarball containing track data to an existing organism.

Output:

     a dictionary with information about all tracks on the organism
        
    """
    return ctx.gi.remote.add_track_file(organism_id, track_data, json_loads(track_config))
