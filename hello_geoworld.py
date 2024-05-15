import click
from example_ogcapi_processes.hello_geoworld import process

@click.command()
@click.option(
    "--data",
    prompt="a json object",
    help="example: {{ \"inputs\": {{\"name\": \"My name\"}}}}"
)
def hello_geo_world(data):
    geo_world_instance = process.HelloGeoWorldCmd()
    echo = geo_world_instance.execute(data)

    click.echo(echo)

if __name__ == "__main__":
    hello_geo_world()
