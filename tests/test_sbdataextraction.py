from sbdataextraction.sbdataextraction import fetch_matches_for_season

season_11_37 = fetch_matches_for_season(11, 37)

# check that season 37 of comp 11 has 7 matches
assert len(season_11_37) == 7, \
"""season id 37 of competition id 11 has 7 matches"""

