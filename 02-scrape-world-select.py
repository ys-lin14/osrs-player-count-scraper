import pandas as pd

from datetime import datetime

from log import check_last_request, update_logs
from extract import get_osrs_world_select, extract_data
from transform import transform_data
from load import load_data

def scrape_world_select():
    dt = datetime.now()
    response = get_osrs_world_select()
    status_code = response.status_code

    if (response.ok):
        world_data, total_player_data = extract_data(response)
        
        world_data, total_player_count = (
            transform_data(world_data, total_player_data, dt)
        )

        load_data(world_data, total_player_count)
    else:
        print('Bad Response - HTTP', status_code)

    update_logs(dt, status_code)


def main():
    logs = pd.read_csv('data/logs.csv')
    last_request_successful = check_last_request(logs)

    if (last_request_successful):
        scrape_world_select()


if __name__ == '__main__':
    main()
