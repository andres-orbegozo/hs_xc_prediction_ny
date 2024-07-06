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

def place_name_extract(df):
    cols = list(df.columns)
    col1 = cols[0]
    
    return ...