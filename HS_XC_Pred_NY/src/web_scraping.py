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

def get_team_event_results(id, state, gender, year, event, season='outdoor-track-and-field'):
    html = requests.get(f'https://{state}.milesplit.com/rankings/events/high-school-{gender}/{season}/{event}m?year={year}&grade=returners&team={id}')
    soup = BeautifulSoup(html.content, 'html.parser')
    data_class = soup.find('div', class_='data')
    times = [time.text for time in data_class.find_all('td', class_='time')]
    names = [name.text for name in data_class.find_all('div', class_='athlete')]
    team = [temp.text for temp in data_class.find_all('div', class_='team')]
    grades = [grade.text for grade in data_class.find_all('td', class_='year')]

    team_dict = {'Name':names, 'Grade': grades, 'Team':team, 'Time': times}

    for key in list(team_dict.keys()):
        print(key)
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

    return team_df

