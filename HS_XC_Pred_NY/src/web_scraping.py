from bs4 import BeautifulSoup
import requests
import pandas as pd

def time_to_secs(time):
    min_sec_list = time.replace(':', ' ').split()
    minute = 0.0
    sec = 0.0

 
    minute = float(min_sec_list[0])*60
    sec = float(min_sec_list[1])

    time = minute+sec
    return time

def get_team_event_results(id, state, gender, year, event, season='outdoor-track-and-field', sc=False):
    if sc==False:
        steep = ''
    else:
        steep = 'SC'
    html = requests.get(f'https://{state}.milesplit.com/rankings/events/high-school-{gender}/{season}/{event}m{steep}?year={year}&grade=returners&team={id}')
    soup = BeautifulSoup(html.content, 'html.parser')
    data_class = soup.find('div', class_='data')
    times = [time.text for time in data_class.find_all('td', class_='time')]
    names = [name.text for name in data_class.find_all('div', class_='athlete')]
    team = [temp.text for temp in data_class.find_all('div', class_='team')]
    grades = [grade.text for grade in data_class.find_all('td', class_='year')]

    team_dict = {'Name':names, 'Grade': grades, 'Team':team, 'Time': times}

    for key in list(team_dict.keys()):
        key_list = []
        for item in team_dict[key]:
            replacement = item.replace('\n', '').replace(' ', '')
            key_list.append(replacement)
        team_dict[key] = key_list

    secs_list = []
    for time in team_dict['Time']:
        temp = time_to_secs(time)
        secs_list.append(temp)

    team_dict['Time'] = secs_list
    id_list = [id] * len(secs_list)
    team_dict['TeamID'] = id_list
    
    team_df = pd.DataFrame(team_dict)

    rows = len(team_df['Name'])
    team_df['Event'] = [event] * rows

    return team_df

def full_team_distance_results_joiner(id, state, gender, year, season='outdoor-track-and-field'):
    input = [('800', False), ('1600', False), ('3200', False), ('3000', True), ('2000', True)]
    df_list = []
    for i in input:
        event = i[0]
        sc = i[1]
        temp = get_team_event_results(id, state, gender, year, event, season, sc)
        df_list.append(temp)
    team_distRes = pd.concat(df_list).reset_index(drop=True)
    return team_distRes

def range_team_results_to_df(start_id: int, end_id: int,state, gender, year, season='outdoor-track-and-field'):
    range_list = list(range(start_id, end_id+1))
    str_id_list = []
    for i in range_list:
        temp = str(i)
        str_id_list.append(temp)
    
    df_list = []
    for i in str_id_list:
        temp_df = full_team_distance_results_joiner(i, state, gender, year)
        df_list.append(temp_df)
    
    big_df = pd.concat(df_list).reset_index(drop=True)

    return big_df




