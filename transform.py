import locale
import numpy as np
import pandas as pd
import re


def drop_even_columns(data):
    data = data[data.columns[1::2]]
    return data


def select(data, columns):
    data = data[columns]
    return data


def rename_columns(data):
    columns = ['world', 'player_count', 'location', 'type', 'activity']
    new_columns = dict(zip(data.columns, columns))
    renamed_data = data.rename(columns=new_columns)
    return renamed_data


def add_datetime_column(data, dt):
    data['datetime'] = dt
    return data


def get_content(tag, index=0):
    try:
        content = tag.contents[index]
    except:
        content = np.nan

    return content


def get_contents(data):
    data['world'] = data['world'].apply(lambda t: get_content(t, index=1))
    
    for column in data.columns:
        data[column] = data[column].apply(lambda t: get_content(t))
        
    return data


def get_match(pattern, string):
    try:
        match = re.search(pattern, string).group(0)
    except:
        match = np.nan
    return match


def get_total_player_count(data):
    # pattern adapted from https://stackoverflow.com/questions/5917082/
    locale.setlocale(locale.LC_ALL, '')
    pattern = r'\d{1,3}(,\d{3})*'
    player_count = data.loc[0, 'player_count']
    player_count = get_match(pattern, player_count)
    data.loc[0, 'player_count'] = locale.atoi(player_count)
    return data


def get_numbers(data):
    columns = ['world', 'player_count']
    pattern = re.compile(r'\d+')
    for column in columns:
        data[column] = data[column].apply(lambda s: get_match(pattern, s))
        try:
            data[column] = data[column].astype(np.int16)
        except:
            data[column] = data[column].astype(np.float)

    return data


def transform_world_data(data, dt, columns):
    data = data.copy()
    transformed_data = (
        data.pipe(drop_even_columns)
            .pipe(rename_columns)
            .pipe(get_contents)
            .pipe(get_numbers)
            .pipe(add_datetime_column, dt=dt)
            .pipe(select, columns=columns)
    )
    return transformed_data


def transform_total_player_count(data, dt):
    data = data.copy()
    transformed_data = (
        data.pipe(get_total_player_count)
            .pipe(add_datetime_column, dt=dt)
            .pipe(select, columns=['datetime', 'player_count'])
    )
    return transformed_data


def transform_data(world_data, total_player_count, dt):
    transformed_world_data = transform_world_data(
        world_data, 
        dt=dt, 
        columns=['datetime', 'world', 'player_count']
    )
    transformed_total_player_count = transform_total_player_count(
        total_player_count,
        dt
    )
    return transformed_world_data, transformed_total_player_count
    
