from web_scraping import range_team_results_to_df

# create a dataframe of all outdoor distance results from NY state boys teams in 2023
df = range_team_results_to_df(10977, 11838, 'ny', 'boys', '2023')
df.to_csv('2023_outdoor_boys.csv')

