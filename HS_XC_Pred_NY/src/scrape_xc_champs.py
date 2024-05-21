from bs4 import BeautifulSoup
import requests
import pandas as pd

meet_id_list = ['563515', '563514', '579610', '563689', '563523', '563513', '566096', '580363', '566109', '567388', '564844', '566097', '567648', '567649', '563096']

chsaa_link = 'https://ny.milesplit.com/meets/578154-chsaa-intersectionals-2023/results/989287/raw/'

def race_results_from_link(link):
    site = requests.get(link)
    soupy = BeautifulSoup(site.content, 'html.parser')
    results = soupy.find('div', id='meetResultsBody')
    results_text = results.find('pre').text

    noise_gone = results_text.replace('-','').replace('=','').replace('  ','##').replace(' ','').replace('##',' ')
    splitted = noise_gone.split('\r\n')

    spl_listList = []
    if '\t' in splitted[5]:
        for obj in splitted:
            temp = obj.split('\t')
            spl_listList.append(temp)
    else:
        for obj in splitted:
            temp = obj.split(' ')
            spl_listList.append(temp)

    # removes empty and space strings to make all sublists to have the same amount of elements
    for i in range(len(spl_listList)):
        j=0
        while j < len(spl_listList[i]):
            element = spl_listList[i][j]
            if element == '':
                spl_listList[i].remove(element)
            elif element == ' ':
                spl_listList[i].remove(element)
            else:
                j=j+1

    # rid of empty lists
    spl_listList = [notempty for notempty in spl_listList if notempty]

    #rid of lists less than 4 length and over 6 length
    spl_listList = [correct for correct in spl_listList if len(correct) >= 4]

    # create list of ints as strings for removing 'points' values
    int_list = [i for i in range(1, 1001)]
    str_int_list = [str(num) for num in int_list]

    # remove random 4th col number
    for i in range(len(spl_listList)):
        if len(spl_listList[i])>4:
            if spl_listList[i][4] in str_int_list:
                del spl_listList[i][4]
    for i in range(len(spl_listList)):
        if len(spl_listList[i])>3:
            if spl_listList[i][3] in str_int_list:
                del spl_listList[i][3]
    for i in range(len(spl_listList)):
        if spl_listList[i][2] in str_int_list:
            del spl_listList[i][2]
    for i in range(len(spl_listList)):
        if spl_listList[i][1] in str_int_list or spl_listList[i][1] == '(<5)':
            del spl_listList[i][1]

    # drop score, bib, grade
    for i in range(len(spl_listList)):
        if 'Score' in spl_listList[i]:
            spl_listList[i].remove('Score')
        if 'Bib' in spl_listList[i]:
            spl_listList[i].remove('Bib')
        if 'Grade' in spl_listList[i]:
            spl_listList[i].remove('Grade')

    #remove team scores
    spl_listList = [correct for correct in spl_listList if ':' not in correct[1]]
    #remove extra team score
    if ':' in spl_listList[0][2]:
        spl_listList = spl_listList[1:]

    # remove second place
    if spl_listList[0][2] == 'PLACE':
        del spl_listList[0][2]

    spl_listList = [correct for correct in spl_listList if len(correct) <= 6]

    # remove all class identifiers
    for i in range(len(spl_listList)):
        j=0
        while j < len(spl_listList[i]):
            element = spl_listList[i][j]
            if element == 'A':
                spl_listList[i].remove(element)
            elif element == 'B':
                spl_listList[i].remove(element)
            elif element == 'C':
                spl_listList[i].remove(element)
            elif element == 'D':
                spl_listList[i].remove(element)
            else:
                j=j+1

    # remove all grade identifiers
    for i in range(len(spl_listList)):
        element = spl_listList[i][2]
        if 'SR' in element:
            spl_listList[i].remove(element)
        elif 'JR' in element:
            spl_listList[i].remove(element)
        elif 'SO' in element:
            spl_listList[i].remove(element)
        elif 'FR' in element:
            spl_listList[i].remove(element)


    #heading extraction
    heading = spl_listList.pop(0)
    heading = [scoreless for scoreless in heading if scoreless != 'Score']
    heading = [scoreless for scoreless in heading if scoreless != 'CLASS']
    heading = [gradeless for gradeless in heading if gradeless != 'GRADE']
    heading = [scoreless for scoreless in heading if scoreless != 'BibNo']
    heading = [seedless for seedless in heading if seedless != 'Seed']
    heading = [scoreless for scoreless in heading if 'Point' not in scoreless]
    heading = [nohash for nohash in heading if '#' not in nohash]

    # drop data that is too difficult
    spl_listList = [nondifficult for nondifficult in spl_listList if len(nondifficult) == len(heading)]

    # NEW FUNCTION TO CREATE A DF BASED ON VARIABLE COLUMNS             

    numCols = len(heading)
    listOfLists = []
    for i in range(numCols):
        tempList = []
        for line in spl_listList:
            tempList.append(line[i])
        listOfLists.append(tempList)

    ziptied = zip(heading, listOfLists)

    df_dict = {key: value for key, value in ziptied}

    results_df = pd.DataFrame(df_dict)

    return results_df


def extract_meet_results(meet_id):  
    html = requests.get(f"https://ny.milesplit.com/meets/{meet_id}/results")
    soup = BeautifulSoup(html.content, 'html.parser')

    fileList = soup.find('ul', id='resultFileList')
    raw = soup.find('small', class_='disclaimer')


    if fileList is not None:
        file_list = fileList.find_all('a')

        link1_list = []
        for race in file_list:
            link = race.get('href')
            link1_list.append(link)

        link_list =[]
        for link in link1_list:
            link2 = link.replace('formatted', 'raw')
            link_list.append(link2)

    if raw is not None:
        raw_link = raw.find('a')
        link_list = []
        link = raw_link.get('href')
        link_list.append(link)

    temp_df_list = []
    for link in link_list:
        temp_df = race_results_from_link(link)
        temp_df_list.append(temp_df)

    meet_df = pd.concat(temp_df_list)

    return meet_df

for meet in meet_id_list:
    temp = extract_meet_results(meet)
    temp.to_csv(f'{meet}.csv', index=False)

chsaa = race_results_from_link(chsaa_link)
chsaa.to_csv('578154.csv')

        

    