from sbdataextraction.sbdataextraction import fetch_matches_for_season
from sbdataextraction.sbdataextraction import get_shots_for_season

season_11_37 = fetch_matches_for_season(11, 37)


def test_fetch_matches_for_season():
    # check that season 37 of comp 11 has 7 matches
    assert len(season_11_37) == 7, \
        """season id 37 of competition id 11 has 7 matches"""


def test_get_shots_for_season():
    # check that shots data frame has correct number of columns
    shots_df = get_shots_for_season(season_11_37)
    assert shots_df.shape[1] == 18, \
        """Shots data frame returned by get_shots_for_season
        should have 18 columns"""
