# import packages from other places if needed
from src.web_scraping import time_to_secs, get_team_event_results, full_team_distance_results_joiner, range_team_results_to_df
from src.data_wrangling import section_identifier, place_name_extract, bool_search_df_for_string, extract_place, remove_nums, to_first_last, asterisk_sameplace_diffrace, team_standard, xc_standardizer