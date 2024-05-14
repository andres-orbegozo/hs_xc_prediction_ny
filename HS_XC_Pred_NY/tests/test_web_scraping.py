import pytest
import requests
import pandas as pd
from tests import time_to_secs, get_team_event_results

def test_time_to_secs():
    test = '4:56.78'
    expected = 296.78
    assert time_to_secs(test) == expected

def test_team_mile_results():
    test_df = pd.DataFrame({'Name': ['GriffinBrown', 'AlexDorrington', 'ADENDOWNEY'], 'Grade':['2026', '2026', '2025'], 'Team':['Geneva', 'Geneva', 'Geneva'],'Time':[274.41, 307.40, 354.72], 'TeamID':['11250', '11250', '11250']})
    actual_df = get_team_event_results('11250', 'ny', 'boys', '2024', '1600')
    pd.testing.assert_frame_equal(
        actual_df,
        test_df
    )

def test_team_twomile_results():
    test_df = pd.DataFrame({'Name': ['GriffinBrown'], 'Grade':['2026'], 'Team':['Geneva'],'Time':[623.85], 'TeamID':['11250']})
    actual_df = get_team_event_results('11250', 'ny', 'boys', '2024', '3200')
    pd.testing.assert_frame_equal(
        actual_df,
        test_df
    )
