from scraping import range_team_results_to_df

df = range_team_results_to_df(10977, 11838, 'ny', 'boys', '2023')
df.to_csv('2023_outdoor_boys.csv')

