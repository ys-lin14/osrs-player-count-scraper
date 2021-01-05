def get_database_url(database_name):
    """Get the url for connecting to the MySQL database
    
    Args:
        database_name (str): name of database
    
    Returns:
        database_url (str): url used to connect to the database
    """

    credentials = {
        'username': 'username',
        'password': 'password',
        'hostname': 'hostname',
        'database_name': database_name
    }
    
    database_url = (
            'mysql+mysqlconnector://{0}:{1}@{2}/{3}'
        .format(
            credentials['username'],
            credentials['password'],
            credentials['hostname'],
            credentials['database_name']
        )
    )
    
    return database_url
