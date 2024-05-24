import pytest
import requests
import pandas as pd
from tests import time_to_secs, get_team_event_results, full_team_distance_results_joiner, range_team_results_to_df

def test_time_to_secs():
    test = '4:56.78'
    expected = 296.78
    assert time_to_secs(test) == expected

def test_team_mile_results():
    test_df = pd.DataFrame({'Name': ['GriffinBrown', 'AlexDorrington', 'ADENDOWNEY'], 'Grade':['2026', '2026', '2025'], 'Team':['Geneva', 'Geneva', 'Geneva'],'Time':[273.02, 307.4, 354.72], 'TeamID':['11250', '11250', '11250']})
    actual_df = get_team_event_results('11250', 'ny', 'boys', '2024', '1600')
    pd.testing.assert_frame_equal(
        actual_df,
        test_df
    )

def test_team_twomile_results():
    test_df = pd.DataFrame({'Name': ['GriffinBrown'], 'Grade':['2026'], 'Team':['Geneva'],'Time':[622.52], 'TeamID':['11250']})
    actual_df = get_team_event_results('11250', 'ny', 'boys', '2024', '3200')
    pd.testing.assert_frame_equal(
        actual_df,
        test_df
    )

def test_empty_sc_result():
    test_df = pd.DataFrame({'Name':[], 'Grade':[], 'Team':[], 'Time':[], 'TeamID':[]})
    actual_df = get_team_event_results('11000', 'ny', 'boys', '2023', '3000', sc=True)
    pd.testing.assert_frame_equal(
        test_df,
        actual_df
    )

def test_team_results():
    test_df = pd.DataFrame({'Name':['BlakeBoon', 'TristenHill', 'BlakeBoon', 'TristenHill', 'SeanWiepert', 'DerekFreitas', 'SeanWiepert'], 'Grade':['2026', '2026', '2026', '2026', '2025', '2025', '2025'], 'Team':['AquinasInstitute', 'AquinasInstitute', 'AquinasInstitute', 'AquinasInstitute', 'AquinasInstitute', 'AquinasInstitute', 'AquinasInstitute'], 'Time':[137.32,173.41, 292.13, 361.07, 370.15, 376.66, 782.23], 'TeamID':['11000','11000', '11000', '11000', '11000', '11000', '11000']})
    actual_df = full_team_distance_results_joiner('11000', 'ny', 'boys', '2023')
    pd.testing.assert_frame_equal(
        test_df,
        actual_df
    )

def test_range_results_basic():
    test_df = pd.DataFrame({'Name': ['MUHAMMADGADIO', 'RileyKing', 'RileyKing'], 'Grade':['2025', '2025', '2025'], 'Team':['MurryBergtraum', 'MynderseAcademy', 'MynderseAcademy'], 'Time':[169.40, 141.46, 311.09], 'TeamID':['11499', '11500', '11500']})
    actual_df = range_team_results_to_df(11499, 11500, 'ny', 'boys', '2023')
    pd.testing.assert_frame_equal(
        test_df,
        actual_df
    )

def test_empty_team():
    test_df = pd.DataFrame({'Name':[], 'Grade':[], 'Team':[], 'Time':[], 'TeamID':[]})
    actual_df = full_team_distance_results_joiner('11680', 'ny', 'boys', '2023')
    pd.testing.assert_frame_equal(
        test_df,
        actual_df
    )

