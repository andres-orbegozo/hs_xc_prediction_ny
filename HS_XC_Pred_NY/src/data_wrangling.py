import pandas as pd

def bool_search_df_for_string(df, string):
    output = df.apply(lambda c: c.map(lambda d: string in d.lower() if isinstance(d, str) else False)).any().any()
    return output


def section_identifier(df):
    iding_teams = {'saratoga': '2', 'liverpool': '3', 'bronxville': '1', 'brooklyn': 'P', 'peru': '7', 'irondequoit': '5', 'aurora': '6', 'cornwall': '9', 'northport': '11', 'brushton': '10', 'corning': '4', 'xavier': 'C', 'collegiate': 'I', 'syosset': '8'}
    teams = iding_teams.keys()
    for team in teams:
        boolin = bool_search_df_for_string(df, team)
        if boolin == True:
            section_id = iding_teams[team]
            n = len(df[list(df.columns)[0]])
            df['Section'] = [section_id] * n
            break
    return df

# IDENTIFY STATES N FEDS MANUALLY

def extract_place(string):
    new = string[0:4]
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    place = ''
    for i in range(4):
        for num in nums:
            if new[i] == num:
                place = place + num
                break
    final = string.replace(place, '')
    return [place, final]

def remove_nums(string):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str_len = len(string)
    new = ''
    for i in range(str_len):
        if string[i] not in nums:
            new = new + string[i]
    return new

def to_first_last(string):
    # check if string has a comma
    str_len = len(string)
    chars = list(string)
    final = ''
    if ',' in chars:
        comma_index = string.index(',')
        sur = string[:comma_index]
        first = string[(comma_index+1):]
        final = ''.join(first+sur)
        final = final.replace('"', '')
    else:
        final = string
    return final
    

def place_name_extract(df):
    # check if all of col1 is ints
    cols = list(df.columns)
    col1_name = cols[0]
    col1 = df[col1_name]
    boolin = col1.apply(lambda x: isinstance(x, int)).all()
    # if true
    if boolin == True:
        df.rename(columns={col1_name: 'Place', cols[1]: 'Name'}, inplace=True)

    # if false
    else:
        lol = col1.apply(lambda x: extract_place(x))
        places = []
        names = []
        for lst in lol:
            places.append(lst[0])
            names.append(lst[1])
        df.rename(columns={col1_name: 'Name'}, inplace=True)
        df['Name'] = names
        df.insert(0, 'Place', places)

    # remove numbers from string and remove commas
    no_num = df['Name'].apply(lambda x: remove_nums(x))
    df['Name'] = no_num
    final_names = df['Name'].apply(lambda x: to_first_last(x))
    df['Name'] = final_names

    # turn places into ints
    as_int = df['Place'].apply(lambda x: int(x))
    df['Place'] = as_int

    return df

def asterisk_sameplace_diffrace(dataframe):
    place_list = dataframe['Place'].apply(lambda x: str(x))
    final_list = []
    while len(place_list) > 0:
        list_len = len(place_list)
        non_repeat = []
        print(len(place_list))
        for i in range(list_len):
            if list_len == 1: #end the loop
                final_list.append(place_list[i])
                place_list = []
                break
            if place_list[i] not in non_repeat:
                non_repeat.append(place_list[i])
            else: #when repetition occurs, add an asterisk to all others
                final_list = final_list + non_repeat 
                place_list = pd.Series(place_list[i:])
                place_list = place_list.apply(lambda x: x+'*')
                place_list = list(place_list) #make place list the remaining repeated places to shorten list
                break
    
    dataframe['Place'] = final_list

    return dataframe

def team_standard(dataframe):
    cols = pd.Series(dataframe.columns)
    flags = ['SCHOOL', 'TEAM']
    cols_up = cols.apply(lambda x: x.upper())
    i=0
    for col in cols_up:
        for flag in flags:
            if flag in col: # remove class identifiers
                team = dataframe[cols[i]].apply(lambda x: x.replace('FR', ''))
                team = team.apply(lambda x: x.replace('SO', ''))
                team = team.apply(lambda x: x.replace('JR', ''))
                team = team.apply(lambda x: x.replace('SR', ''))
                dataframe[cols[i]] = team
                dataframe.rename(columns={cols[i]: 'Team'}, inplace = True)
        i = i+1
    return dataframe



def xc_standardizer(dataframe):
    if '' in dataframe.columns:
        dataframe.drop('', axis=1)
    
    # organize and standardize
    dataframe = section_identifier(dataframe)
    dataframe = place_name_extract(dataframe)
    dataframe = asterisk_sameplace_diffrace(dataframe)
    dataframe = team_standard(dataframe)

    place = dataframe['Place']
    name = dataframe['Name']
    team = dataframe['Team']
    section = dataframe['Section']

    # make dataframe smaller
    dataframe = pd.DataFrame({'Place': place, 'Name': name, 'Team': team, 'Section': section})

    return dataframe

def athlete_id_assigner_track(dataframe):
    num_entries = len(dataframe['Name'])
    holder = [0] * num_entries
    dataframe['AthleteID'] = holder # initialize athleteID col as zeroes
    id = 1 #initialized ids
    for row in range(num_entries):
        if dataframe['AthleteID'][row] == 0:
            dataframe.loc[row, 'AthleteID'] = id
            # splitting data to search
            already_done = dataframe.iloc[:row, :]
            current = dataframe.iloc[row, :]
            to_search = dataframe.iloc[row+1:, :]
            # searching for same person
            same_team = to_search[to_search['TeamID'] == current['TeamID']]
            same_grade_st = same_team[same_team['Grade'] == current['Grade']]
            same = same_grade_st[same_grade_st['Name'] == current['Name']]
            # giving same athlete same ids
            for ind in same.index:
                dataframe.loc[ind, 'AthleteID'] = id
            id = id+1
    return dataframe

        
def tidy_track_data(dataframe):
    dataframe = dataframe.drop(columns=[''])


    