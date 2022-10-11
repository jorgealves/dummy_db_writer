import click
import faker

from pypika import Query, Table

fake = faker.Faker()

column_types = click.Choice(
    [
        'name',
        'date',
        'email',
        'text',
        'address',
        'zipcode',
    ]
)

@click.group
def dummy_writer():
    pass



@dummy_writer.command
@click.option('--table', '-t','table', type=click.STRING, help='Table name')
@click.option('--column', '-c','columns', multiple=True, type=click.STRING, help='Column name')
@click.option('--columnValue', '-v','columnValues', multiple=True, type=column_types, help='Table column value')
@click.option('--records', '-n','records', type=click.types.INT, default=50, show_default=True, prompt=True, help='Number of records to create')
def go(table:str, columns:list, columnValues:list, records:int): 
    table = Table(name=str(table))
    rows = []
    for _ in range(records): 
        rows.append( tuple(
            getattr(fake,columnValue)()
            for columnValue in columnValues if hasattr(fake,columnValue)
        ))
    click.echo(str(Query.into(table).columns(columns).insert(rows)))
            