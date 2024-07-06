import pytest
import pandas as pd
from tests import section_identifier, place_name_extract, bool_search_df_for_string

def test_bool_search_df_for_string():
    test_df = pd.DataFrame({'colA': ['abc', 'def', 'ghi'], 'colB': ['jkl', 'mno', 'pqr'], 'colC': ['stu', 'vwx', 'yz']})
    expected = True
    assert bool_search_df_for_string(test_df, 'pq') == expected

def test_section_identifier(): #states and feds need to be done outside function #use inside standardizer
    # test dfs
    sec2df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'SaratogaSp'],'Pace':['2', '3'],'Time':['4', '5']})
    sec3df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Liverpool', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    sec1df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Bronxville'],'Pace':['2', '3'],'Time':['4', '5']}) 
    psal_df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['BrooklynL', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    sec7df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Peru'],'Pace':['2', '3'],'Time':['4', '5']})
    sec5df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Irondequoit', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    sec6df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'EstAurora'],'Pace':['2', '3'],'Time':['4', '5']})
    sec9df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Cornwall', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    sec11df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Northport'],'Pace':['2', '3'],'Time':['4', '5']})
    sec10df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Brushton', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    sec4df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Corning'],'Pace':['2', '3'],'Time':['4', '5']})
    chsaa_df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Xavier', 'c'],'Pace':['2', '3'],'Time':['4', '5']})
    ais_df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Collegiate'],'Pace':['2', '3'],'Time':['4', '5']})
    sec8df = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Syosset', 'c'],'Pace':['2', '3'],'Time':['4', '5']})

    # expected result dfs
    sec2df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'SaratogaSp'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['2', '2']})
    sec3df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Liverpool', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['3', '3']})
    sec1df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Bronxville'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['1', '1']}) 
    psal_df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['BrooklynL', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['P', 'P']})
    sec7df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Peru'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['7', '7']})
    sec5df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Irondequoit', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['5', '5']})
    sec6df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'EstAurora'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['6', '6']})
    sec9df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Cornwall', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['9', '9']})
    sec11df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Northport'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['11', '11']})
    sec10df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Brushton', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['10', '10']})
    sec4df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Corning'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['4', '4']})
    chsaa_df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Xavier', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['C', 'C']})
    ais_df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['c', 'Collegiate'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['I', 'I']})
    sec8df_exp = pd.DataFrame({'Place':[1, 26],'Name':['a', 'b'],'Team':['Syosset', 'c'],'Pace':['2', '3'],'Time':['4', '5'], 'Section':['8', '8']})
    
    pd.testing.assert_frame_equal(section_identifier(sec1df), sec1df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec2df), sec2df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec3df), sec3df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec4df), sec4df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec5df), sec5df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec6df), sec6df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec7df), sec7df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec8df), sec8df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec9df), sec9df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec10df), sec10df_exp)
    pd.testing.assert_frame_equal(section_identifier(sec11df), sec11df_exp)
    pd.testing.assert_frame_equal(section_identifier(psal_df), psal_df_exp)
    pd.testing.assert_frame_equal(section_identifier(chsaa_df), chsaa_df_exp)
    pd.testing.assert_frame_equal(section_identifier(ais_df), ais_df_exp)

def test_place_name_extract(): #use in xc standardizer #is always first two cols i believe
    inputA = pd.DataFrame({
        'Place':[4],
        'Name': ['abc'],
    })
    inputB = pd.DataFrame({
        'PLACE': [4],
        'PTSNAME': ['2abc'],
    })
    inputC = pd.DataFrame({
        'PlAthlete': ['4abc'],
    })
    inputD = pd.DataFrame({
        'Name': ['4abc'],
    })
    inputE = pd.DataFrame({
        'NAME': [4],
        'YR': ['abc']
    })
    inputF = pd.DataFrame({
        'PlAthlete': ['"4bc,a"']
    })
    inputG = pd.DataFrame({
        "O'AllPlace": [4],
        'Name': ['abc']
    })
    inputH = pd.DataFrame({
        'Name': ['"4bc,a"'],
        'YearSchool': ['def']
    })
    inputI = pd.DataFrame({
        'PlaceTmPlNo.':[4],
        'Name':['34abc']
    })
    inputJ = pd.DataFrame({
        'PL': [4],
        'NAME': ['abc']
    })

    expected_df = pd.DataFrame({
        'Place': [4],
        'Name': ['abc']
    })

    pd.testing.assert_frame_equal(place_name_extract(inputA), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputB), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputC), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputD), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputE), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputF), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputG), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputH), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputI), expected_df)
    pd.testing.assert_frame_equal(place_name_extract(inputJ), expected_df)

# def standardize_teamname_and_time():
#     assert ...

def test_asterisk_sameplace_diffrace(): # use in xc standardizer # give all asterisks at first repetition and repeat for each new repeat
    test_df = pd.DataFrame({
        'Place': [1, 3, 4, 1, 4, 12, 4, 12, 15, 1, 1, 1, 1, 1, 1, 1],
        'Name': ['qwe', 'rty', 'uio', 'pas', 'dfg', 'hjk', 'lzx', 'cvb', 'nmq', 'wer', 'tyu', 'iop', 'asd', 'fgh', 'jkl', 'zxc']
    })
    expected_df = pd.DataFrame({
        'Place': ['1', '3', '4', '1*', '4*', '12*', '4**', '12**', '15**', '1***', '1****', '1*****', '1******', '1*******', '1********', '1*********'],
        'Name': ['qwe', 'rty', 'uio', 'pas', 'dfg', 'hjk', 'lzx', 'cvb', 'nmq', 'wer', 'tyu', 'iop', 'asd', 'fgh', 'jkl', 'zxc']
    })
    pd.testing.assert_frame_equal(asterisk_sameplace_diffrace(test_df), expected_df)


def test_xc_standardizer(): #drop unnamed first columns #join outside function!!!!!!
    messedup_df = pd.DataFrame({
        'PLnmE': ['"26Lyons,Mark"', '"26Davis,Mike"'],
        'YRtEm': ['JRRyansville', 'SOGeorgian'],
        'TaYme': ['14:45.76', '19:43.22'],
        'Pace': ['4:45/MI', '6:20/MI'],
        'KmPace': ['2:57.15', '3:56.64']
    })
    messedup_df2 = pd.DataFrame({
        'PlaYCe': [26, 26],
        'NmEPt': ['124MarkLyons', '161MikeDavis'],
        'YRtEm': ['JRRyansville', 'SOGeorgian'],
        'TaYme': ['14:45.76', '19:43.22'],
        'Pace': ['4:45/MI', '6:20/MI'],
        'KmPace': ['2:57.15', '3:56.64']
    })
    expected_df = pd.DataFrame({
        'Place': ['26', '26*'],
        'Name': ['MarkLyons', 'MikeDavis'],
        'Team': ['Ryansville', 'Georgian']
    })
    pd.testing.assert_frame_equal(xc_standardizer(messedup_df), expected_df)
    pd.testing.assert_frame_equal(xc_standardizer(messedup_df2), expected_df)

def test_tidy_track_data(): # drop blank col first before func is run
    input_df = pd.DataFrame({
        'Name': ['AbcDef', 'AbcDef', 'AbcDef', 'AbcDef', 'AbcDef', 'HijKlmn', 'HijKlmn', 'HijKlmn', 'HijKlmn', 'OpqRst', 'OpqRst', 'UvwXyz'],
        'Grade': ['2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2024', '2025', '2025', '2023'],
        'Team': ['Qwerty', 'Qwerty', 'Qwerty', 'Qwerty', 'Qwerty', 'Qwerty', 'Qwerty', 'Qwerty', 'Uiop', 'Uiop', 'Uiop', 'Uiop'],
        'Time': [124.61, 280.42, 590.53, 602.26, 405.24, 135.22, 300.34, 422.31, 300.34, 296.54, 628.29, 265.66],
        'TeamID': ['11000', '11000', '11000', '11000', '11000', '11000', '11000', '11000', '11001', '11001', '11001', '11001'],
        'Event': ['800', '1600', '3200', '3000', '2000', '800', '1600', '2000', '1600', '1600', '3200', '1600']
    })
    expected_df = pd.DataFrame({
        'Name':['AbcDef', 'HijKlmn', 'HijKlmn', 'OpqRst'],
        'Grade': ['2024', '2024', '2024', '2025'],
        'Team': ['Qwerty', 'Qwerty', 'Uiop', 'Uiop'],
        '800': [124.61, 135.22, None, None],
        '1600': [280.42, 300.34, 300.34, 296.54],
        '3200': [590.23, None, None, 628.29],
        '3000': [602.26, None, None, None],
        '2000': [405.24, 422.31, None, None],
        'TeamID': ['11000', '11000', '11001', '11001'],
        'AthleteID': [1, 2, 3, 4]
    })
    pd.testing.assert_frame_equal(
        tidy_track_data(input_df),
        expected_df
    )

def test_team_id_assigner(): #done to xc data
    tidy_track_df = pd.DataFrame({
        'Name':['AbcDef', 'HijKlmn', 'HijKlmn', 'OpqRst'],
        'Grade': ['2024', '2024', '2024', '2025'],
        'Team': ['Qwerty', 'Qwerty', 'Uiop', 'Uiop'],
        '800': [124.61, 135.22, None, None],
        '1600': [280.42, 300.34, 300.34, 296.54],
        '3200': [590.23, None, None, 628.29],
        '3000': [602.26, None, None, None],
        '2000': [405.24, 422.31, None, None],
        'TeamID': ['11000', '11000', '11001', '11001'],
        'AthleteID': [1, 2, 3, 4]
    })
    std_xc_df = pd.DataFrame({
        'Place': ['25', '29'],
        'Name': ['MaxBlot', 'JamesBruh'],
        'Team': ['QWERTY', 'UIOp'],
        'Section': ['3', '5']
    })
    expected_df = pd.DataFrame({
        'Place': ['25', '29'],
        'Name': ['MaxBlot', 'JamesBruh'],
        'Team': ['QWERTY', 'UIOp'],
        'Section': ['3', '5'],
        'TeamID': ['11000', '11001']
        
    })
    
    pd.testing.assert_frame_equal(
        team_id_assigner(tidy_track_df, std_xc_df), 
        expected_df
    )


def test_athlete_id_assigner(): #use in tidy xc data
    tidy_track_df = pd.DataFrame({
        'Name':['AbcDef', 'HijKlmn', 'HijKlmn', 'OpqRst'],
        'Grade': ['2024', '2024', '2024', '2025'],
        'Team': ['Qwerty', 'Qwerty', 'Uiop', 'Uiop'],
        '800': [124.61, 135.22, None, None],
        '1600': [280.42, 300.34, 300.34, 296.54],
        '3200': [590.23, None, None, 628.29],
        '3000': [602.26, None, None, None],
        '2000': [405.24, 422.31, None, None],
        'TeamID': ['11000', '11000', '11001', '11001'],
        'AthleteID': [357, 995, 1234, 3340]
    })
    xc_df = pd.DataFrame({
        'Place': ['37', '49', '50'],
        'Name': ['AbcDef', 'OpqRst', 'ZxcVbnm'],
        'Team': ['QWERTY', 'UIOp', 'UIOp'],
        'Section': ['3', '5', '5'],
        'TeamID': ['11000', '11001', '11001']
    })
    expected_df = pd.DataFrame({
        'Place': ['37', '49', '50'],
        'Name': ['AbcDef', 'OpqRst', 'ZxcVbnm'],
        'Team': ['QWERTY', 'UIOp', 'UIOp'],
        'Section': ['3', '5', '5'],
        'TeamID': ['11000', '11001', '11001'],
        'AthleteID': [357, 3340, None]
    })

    pd.testing.assert_frame_equal(
        athlete_id_assigner(tidy_track_df, xc_df),
        expected_df
    )

def test_tidy_up_xc_data(): #remove all with no athlete id
    input_df = pd.DataFrame({
        'Place': ['37', '49', '12**', '52', '24', '26', '27', '28', '12', '39', '42'],
        'Name': ['AbcDef', 'FrgCdfg', 'VdojHhsf', 'OpqRst', 'EcsdcJsbf', 'AbcDef', 'FrgCdfg', 'OpqRst', 'AbcDef', 'EcsdcJsbf', 'VdojHhsf'],
        'Team': ['QWERTY', 'QWERTY', 'Asdf', 'UIOp', 'BTech', 'QWERTY', 'QWERTY', 'UIOp', 'QWERTY', 'BTech', 'Asdf'],
        'Section': ['3', '3', '3', '5', 'P', 'S', 'S', 'S', 'F', 'F', 'F'],
        'TeamID': ['11000', '11000',  '10968', '11001', '11432', '11000', '11000', '11001', '11000', '11432', '10968'],
        'AthleteID': [357, None, 4493, 3340, 534, 357, None, 3340, 357, 534, 4493]
    })
    expected_df = pd.DataFrame({
        'Name': ['AbcDef', 'VdojHhsf', 'OpqRst', 'EcsdcJsbf'],
        'Team': ['QWERTY', 'Asdf', 'UIOp', 'BTech'],
        'Section':['3', '3', '5', 'P'],
        'TeamID':['11000', '10968', '11001', '11432'],
        'AthleteID':[357, 4493, 3340, 534],
        'Sectionals':['37', '12**', '52', '24'],
        'States':['26', None, '28', None],
        'Feds':['12', '42', None, '39']
    })
    pd.testing.assert_frame_equal(
        tidy_up_xc_data(input_df),
        expected_df
    )

def test_merge_xc_track(): #remove seniors
    xc_df = pd.DataFrame({
        'Name': ['AbcDef', 'VdojHhsf', 'OpqRst', 'EcsdcJsbf'],
        'Team': ['QWERTY', 'Asdf', 'UIOp', 'BTech'],
        'Section':['3', '3', '5', 'P'],
        'TeamID':['11000', '10968', '11001', '11432'],
        'AthleteID':[357, 4493, 3340, 534],
        'Sectionals':['37', '12**', '52', '24'],
        'States':['26', None, '28', None],
        'Feds':['12', '42', None, '39']
    })
    track_df = pd.DataFrame({
        'Name':['VdojHhsf', 'AbcDef', 'OpqRst', 'EcsdcJspf'],
        'Grade': ['2024', '2024', '2025', '2024'],
        'Team': ['Asdf', 'Qwerty', 'Uiop', 'BTech'],
        '800': [135.22, 124.61, None, None],
        '1600': [300.34, 280.42, 296.54, 300.34],
        '3200': [None, 590.23, 628.29, None],
        '3000': [None, 602.26, None, None],
        '2000': [422.31, 405.24, None, None],
        'TeamID': ['10968', '11000', '11001', '11432'],
        'AthleteID': [4493, 357, 3340, 534],
    })
    expected_df = pd.DataFrame({
        'Name':['VdojHhsf', 'AbcDef', 'OpqRst', 'EcsdcJspf'],
        'Grade': ['2024', '2024', '2025', '2024'],
        'Team': ['Asdf', 'Qwerty', 'Uiop', 'BTech'],
        '800': [135.22, 124.61, None, None],
        '1600': [300.34, 280.42, 296.54, 300.34],
        '3200': [None, 590.23, 628.29, None],
        '3000': [None, 602.26, None, None],
        '2000': [422.31, 405.24, None, None],
        'TeamID': ['10968', '11000', '11001', '11432'],
        'AthleteID': [4493, 357, 3340, 534],
        'Sectionals':['12**', '37', '52', '24'],
        'States':[None, '26', '28', None],
        'Feds':['42', '12', None, '39'],
    })
    pd.testing.assert_frame_equal(
        merge_xc_track(track_df, xc_df),
        expected_df
    )

