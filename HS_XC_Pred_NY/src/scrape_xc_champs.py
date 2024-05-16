from bs4 import BeautifulSoup
import requests
import pandas as pd

meet_id_list = ['563515', '578154', '563514', '579610', '563689', '563523', '563513', '566096', '580363', '566109', '567388', '564844', '566097', '567648', '567649', '563096']

def race_results_from_link(link):
    site = requests.get(f'{link}')
    soupy = BeautifulSoup(site.content, 'html.parser')
    results = soupy.find('div', id='meetResultsBody')
    results_text = results.find('pre').text
    justRunners = results_text.replace('BOYS CLASS A 5K', '').replace('-', '').replace('PLACE', '').replace('PTS', '').replace('GRADE', '').replace('SCHOOL', '').replace('TIME','').replace('PACE','').replace('NAME','').replace('  ','##').replace(' ','').replace('##',' ')
    splittedRunners = justRunners.split('\r\n')

    splRun_list = []
    for runner in splittedRunners:
        splRun_list.append(runner)

    splRun_listList = []
    for runner in splRun_list:
        temp = runner.split(' ')
        splRun_listList.append(temp)

    # removes empty and space strings to make all sublists to have the same amount of elements
    for i in range(len(splRun_listList)):
        j=0
        while j < len(splRun_listList[i]):
            # print(i, j)
            element = splRun_listList[i][j]
            if element == '':
                splRun_listList[i].remove(element)
            elif element == ' ':
                splRun_listList[i].remove(element)
            else:
                j=j+1

    # remove empty lists & title
    splRun_listList = splRun_listList[1:]
    splRun_listList = [notempty for notempty in splRun_listList if notempty]

    #remove random 4th col number
    for i in range(len(splRun_listList)):
        if splRun_listList[i][3] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            del splRun_listList[i][3] 
    places = []
    names = []
    grades = []
    teams = []
    times = []

    for list in splRun_listList:
        places.append(list[0])
        names.append(list[1])
        grades.append(list[2])
        teams.append(list[3])
        times.append(list[4])

    #final cleaning
    i=0
    for name in names:
        for char in name:
            if char.isdigit() == True:
                rep = names[i].replace(char, '')
                names[i] = rep
        i=i+1
    j=0
    for grade in grades:
        for char in grade:
            if char.isdigit() == True:
                rep = grades[j].replace(char, '')
                grades[j] = rep
        j=j+1

    #turn to df
    results_df = pd.DataFrame({'PLACE': places, 'NAME': names, 'GRADE': grades, 'TEAM': teams, 'TIME': times})  

    return results_df


def extract_meet_results(meet_id):  
    html = requests.get(f"https://ny.milesplit.com/meets/{meet_id}/results")
    soup = BeautifulSoup(html.content, 'html.parser')

    fileList = soup.find('ul', id='resultFileList')
    file_list = fileList.find_all('a')

    link1_list = []
    for race in file_list:
        link = race.get('href')
        link1_list.append(link)

    link_list =[]
    for link in link1_list:
        link2 = link.replace('formatted', 'raw')
        link_list.append(link2)

    temp_df_list = []
    for link in link_list:
        temp_df = race_results_from_link(link)
        temp_df_list.append(temp_df)

    meet_df = pd.concat(temp_df_list)

    return meet_df

df = extract_meet_results('563514')
print(df)

        

    