from sbdataextraction.sbdataextraction import fetch_matches_for_season, fetch_seasons_for_league # noqa
from sbdataextraction.sbdataextraction import get_shots_for_season, get_shots_for_league # noqa
from sbdataextraction.sbdataextraction import draw_pitch, plot_shot_freeze_frame # noqa
import matplotlib.pyplot as plt
import pandas as pd

season_11_37 = fetch_matches_for_season(11, 37)
league_43 = fetch_seasons_for_league(43)


def test_fetch_matches_for_season():
    # check that season 37 of comp 11 has 7 matches
    assert len(season_11_37) == 7, \
        """season id 37 of competition id 11 has 7 matches"""
    # check that assertion error is thrown for invalid inputs
    try:
        fetch_matches_for_season(11, 100)
    except AssertionError:
        pass
    try:
        fetch_matches_for_season(100, 100)
    except AssertionError:
        pass


def test_get_shots_for_season():
    # check that shots data frame has correct number of columns
    shots_df = get_shots_for_season(season_11_37)
    assert isinstance(shots_df, pd.DataFrame), \
        """get_shots_for_season should return a pandas data frame"""
    assert shots_df.shape[1] == 18, \
        """Shots data frame returned by get_shots_for_season
        should have 18 columns"""


def test_draw_pitch():
    # check that draw_pitch returns correct object
    fig, ax = plt.subplots(1, 1)
    type_ = str(type(draw_pitch(ax)))
    assert type_ == "<class 'matplotlib.axes._subplots.AxesSubplot'>", \
        """draw_pitch should return matplotlib axis object"""


def test_plot_shot_freeze_frame():
    # check that plot_shot_freeze_frame returns correct object
    fig, ax = plt.subplots(1, 1)
    splot = plot_shot_freeze_frame(season_11_37[69153],
                                   "7799b3d3-eb47-4d1f-9a38-2a9891bd991e",
                                   ax)
    type_ = str(type(splot))
    assert type_ == "<class 'matplotlib.axes._subplots.AxesSubplot'>", \
        """draw_pitch should return matplotlib axis object"""


def test_get_shots_for_game():
    # check that shots data frame has correct number of columns
    shots_df = season_11_37[69153].get_shots_for_game()
    assert isinstance(shots_df, pd.DataFrame), \
        """get_shots_for_game should return a pandas data frame"""
    assert shots_df.shape[1] == 17, \
        """Shots data frame returned by get_shots_for_game
        should have 17 columns"""


def test_check_btwn_shot_goal():
    # check if test_check_btwn_shot_goal is working properly
    my_game = season_11_37[69153]
    assert my_game.check_player_btwn_shot_and_goal(100, 40, 110, 40), \
        """Should return True for specified inputs"""
    assert not my_game.check_player_btwn_shot_and_goal(100, 40, 100, 70), \
        """Should return False for specified inputs"""


def test_get_events_for_game():
    # check that events data frame has correct number of columns
    events_df = season_11_37[69153].get_events_for_game()
    assert isinstance(events_df, pd.DataFrame), \
        """get_events_for_game should return a pandas data frame"""
    assert events_df.shape[1] == 11, \
        """Events data frame returned by get_events_for_game
        should have 11 columns"""


def test_fetch_seasons_for_league():
    # check that season 37 of comp 11 has 7 matches
    assert len(league_43) == 1, \
        """league id 43 has 1 season"""
    # check that assertion error is thrown for invalid inputs
    try:
        fetch_seasons_for_league(1000)
    except AssertionError:
        pass


def test_get_shots_for_league():
    # check that shots data frame has correct number of columns
    shots_df = get_shots_for_league(league_43)
    assert isinstance(shots_df, pd.DataFrame), \
        """get_shots_for_league should return a pandas data frame"""
    assert shots_df.shape[1] == 19, \
        """Shots data frame returned by get_shots_for_league
        should have 19 columns"""
