import click
import faker

from pypika import Query, Table

fake = faker.Faker()

column_types = click.Choice(
    [
        'name',
        'date',
        'email',
        'address',
        'zipcode',
    ]
)

@click.group
def dummy_writer():
    pass



@dummy_writer.command
@click.option('--table', '-t','table', type=click.STRING, help='Table name')
@click.option('--column', '-c','columns', multiple=True, type=column_types, help='Table column Value')
@click.option('--records', '-n','records', type=click.types.INT, default=50, show_default=True, prompt=True, help='Number of records to create')
def go(table:str, columns:list, records:int): 
    table = Table(name=str(table))
    rows = []
    for _ in range(records): 
        rows.append( tuple(
            getattr(fake,column)()
            for column in columns if hasattr(fake,column)
        ))
    click.echo(str(Query.into(table).insert(rows)))
            
        
