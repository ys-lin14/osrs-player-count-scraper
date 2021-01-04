import pandas as pd

def initialize_logs():
    logs = pd.DataFrame(columns=['datetime', 'response'])
    logs.to_csv('data/logs.csv', index=False)
    
    
def check_last_request(logs):
    last_response = logs.loc[0, 'response']
    last_request_successful = (last_response == 200)
    return last_request_successful
   
    
def update_logs(dt, status_code):
    logs = pd.read_csv('data/logs.csv')
    
    new_log_entry = pd.DataFrame.from_dict({
        'datetime': [dt],
        'response': [status_code]
    })
    
    logs = logs.append(new_log_entry)
    logs.to_csv('data/logs.csv', index=False)
