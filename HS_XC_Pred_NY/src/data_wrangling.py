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
            if list_len == 1:
                final_list.append(place_list[i])
                place_list = []
                break
            if place_list[i] not in non_repeat:
                non_repeat.append(place_list[i])
            else:
                final_list = final_list + non_repeat
                place_list = pd.Series(place_list[i:])
                place_list = place_list.apply(lambda x: x+'*')
                place_list = list(place_list)
                break
    
    dataframe['Place'] = final_list

    return dataframe

# asterisk_sameplace_diffrace(pd.DataFrame({
#         'Place': [1, 3, 4, 1, 4, 12, 4, 12, 15, 1, 1, 1, 1, 1, 1, 1],
#         'Name': ['qwe', 'rty', 'uio', 'pas', 'dfg', 'hjk', 'lzx', 'cvb', 'nmq', 'wer', 'tyu', 'iop', 'asd', 'fgh', 'jkl', 'zxc']
#     }))