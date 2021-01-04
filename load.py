import pandas as pd
import sqlalchemy

from database_credentials import get_database_url


def write_data(data, table_name, connection):
    data.to_sql(
        table_name,
        connection,
        if_exists='append',
        index=False
    )


def load_data(world_data, total_player_count):
    database_url = get_database_url(database_name='osrs')
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()

    write_data(world_data, 'world_player_counts', connection)
    write_data(total_player_count, 'total_player_counts', connection)

    connection.close()
    engine.dispose()
