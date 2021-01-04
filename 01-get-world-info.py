from datetime import datetime

from log import initialize_logs, update_logs
from extract import get_osrs_world_select, extract_world_data
from transform import transform_world_data


def get_world_info():
    dt = datetime.now()
    response = get_osrs_world_select()
    status_code = response.status_code

    if (response.ok):
        world_data = extract_world_data(response)
        world_info = transform_world_data(
                world_data, 
                columns=['world', 'location', 'type', 'activity'],
                dt=None
        )
        world_info.to_csv('data/world_info.csv', index=False)
    else:
        print('Bad Response - HTTP', status_code)

    update_logs(dt, status_code)


def main():
    initialize_logs()
    get_world_info()


if __name__ == '__main__':
    main()
