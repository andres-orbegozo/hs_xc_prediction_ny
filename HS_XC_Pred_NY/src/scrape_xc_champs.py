from bs4 import BeautifulSoup
import requests
import pandas as pd

meet_id_list = ['563515', '578154', '563514', '579610', '563689', '563523', '563513', '566096', '580363', '566109', '567388', '564844', '566097', '567648', '567649', '563096']

def race_results_from_link(link):
    site = requests.get(link)
    soupy = BeautifulSoup(site.content, 'html.parser')
    results = soupy.find('div', id='meetResultsBody')
    results_text = results.find('pre').text

    noise_gone = results_text.replace('-','').replace('=','').replace('  ','##').replace(' ','').replace('##',' ')
    splitted = noise_gone.split('\r\n')

    spl_listList = []
    for obj in splitted:
        temp = obj.split(' ')
        spl_listList.append(temp)

    # removes empty and space strings to make all sublists to have the same amount of elements
    for i in range(len(spl_listList)):
        j=0
        while j < len(spl_listList[i]):
            # print(i, j)
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
    int_list = [i for i in range(1, 501)]
    str_int_list = [str(num) for num in int_list]

    # remove random 4th col number
    for i in range(len(spl_listList)):
        if spl_listList[i][3] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            del spl_listList[i][3]
        elif spl_listList[i][2] in str_int_list:
            del spl_listList[i][2]
    spl_listList = [correct for correct in spl_listList if len(correct) <= 6]

    #heading extraction
    heading = spl_listList.pop(0)
    heading = [scoreless for scoreless in heading if scoreless != 'Score']

    # drop data that is too difficult
    spl_listList = [nondifficult for nondifficult in spl_listList if len(nondifficult) == len(heading)]

    spl_listList

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

    results_df  

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

df = extract_meet_results('563515')
print(df)

        

    