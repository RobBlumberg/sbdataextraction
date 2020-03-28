## sbdataextraction 

![](https://github.com/RobBlumberg/sbdataextraction/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/RobBlumberg/sbdataextraction/branch/master/graph/badge.svg)](https://codecov.io/gh/RobBlumberg/sbdataextraction) ![Release](https://github.com/RobBlumberg/sbdataextraction/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/sbdataextraction/badge/?version=latest)](https://sbdataextraction.readthedocs.io/en/latest/?badge=latest)

### Package description

This is a package to get statsbomb public data into python. Statsbomb themselves have their own pacakge called [statsbombpy](https://github.com/statsbomb/statsbombpy), which provides similar functionality. I made this package mostly for my own personal use, since I found I was often repeating the same data extraction steps across several projects (I also wrote a lot of these functions before the release of statsbombpy). I will continue to add functionality to this package as I work on new projects.

### Dependencies

- pandas 1.0.3
- requests 2.23.0
- numpy 1.18.2
- matplotlib 3.2.1

### Installation:

The package has been deployed to test pypi. If you do not have the dependencies listed above installed, please use the command below.
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple sbdataextraction
```

You may also install the package using the command below if the dependencies are already satisfied on your local machine.
```
pip install -i https://test.pypi.org/simple/ sbdataextraction
```

### Usage

Here is a typical workflow I use in my projects. First, I fetch all the data for a league using the `fetch_seasons_for_league` function.

```python
  from sbdataextraction import sbdataextraction as sbd
  # 43 is the competition id for the 2018 FIFA men's world cup
  wc_data = sbd.fetch_seasons_for_league(43) 
  >>> {'2018': {7562: <__main__.Game at 0x1302ddd10>,
                7549: <__main__.Game at 0x13125cad0>,
                7565: <__main__.Game at 0x132114210>,
                ...
                }
      }
```
This return a data structure mapping seasons to inner dictionaries. The inner dictionaries themselves map game id's to `Game` objects. 

A `Game` object has several attributes and methods. The first thing we can do is call the `get_shots_for_game` method.
```python
  game = wc_data["2018"][8656]
  game.get_shots_for_game()
  >>>
```
|shot id	| team_id	| team_name	| player_id	| player_name	| play pattern |	x start location |	y start location |	duration |	outcome |	technique	| first time |	x gk position |	y gk position |	type of shot |	num opponents within 5 yards |	num opponents between shot and goal|	statsbomb xg |
| :------ |:-------:| :--------:|:---------:|:-----------:|:------------:|:-----------------:|:-----------------:|:---------:|:--------:|:---------:|:----------:|:--------------:|:-------------:|:------------:|:----------------------------:|:-----------------------------------:|--------------:|
|6b09b997-06b0-43e7-a47f-13fddf502adc	|768	|England	|3308	|Kieran Trippier	|From Free Kick	|96|	43|	1.013	|Goal|	Normal	|FALSE|	120	|41	|Free Kick|	0|	3	|0.12567155|
|c4255cb9-bcbf-4271-9045-078c41fcac07	|768	|England	|3336|	Harry Maguire|	From Corner|	111|	37|	1.453	|Off T|	Normal	|FALSE|	120|	41|	Open Play	|4	|2	|0.021540243|

We can also call the `Game` object's `get_events_for_game` method. This will return not only return **shots**, but **passes**, **carries** and **ball receipts**. However, the number of features related to these events will be less than in the `get_shots_for_game` method.
```python
  game.get_events_for_game()
  >>>
```
|event id	|event name	|team_id	|team_name	|player_id	|player_name	|x start location	|y start location	|x end location	|y end location	|statsbomb xg	|related events|
| :------ |:---------:|:-------:|:---------:|:---------:|:-----------:|:---------------:|:---------------:|:-------------:|--------------:|:-----------:|-------------:|
|f15b138e-9893-4819-94a0-56a1b57e1442	|pass	|768	|England	|3094	|Bamidele Alli	|61	|41	|42	|32	|-1	|['ce490e3d-bee0-4133-89e6-c55854dfeb8b']|
|ce490e3d-bee0-4133-89e6-c55854dfeb8b	|ball receipt*|	768	|England	|3244	|John Stones	|42	|32	|-1	|-1	|-1	|['f15b138e-9893-4819-94a0-56a1b57e1442']|
|3467bb61-10ac-4992-8704-7b4dd8954463	|carry	|768	|England	|3244	|John Stones	|42	|32	|43	|32	|-1	|['722cc584-bbb5-4ac7-a8f6-32dc4d2f9117', 'ce490e3d-bee0-4133-89e6-c55854dfeb8b']|

Sometimes, I only want to get the data for a specific season, not all the data for a league. In the world cup case above, there was only 1 season. But if I wanted a specific season of Messi's la liga data, I could use the `fetch_matches_for_season` function.
```python
  # 11 is the competition id for la liga Messi data, and 37 is the season id for 2004/05
  season_11_37 = sbd.fetch_matches_for_season(11, 37) 
  >>> {69153: <__main__.Game at 0x12c24d2d0>,
       68313: <__main__.Game at 0x12c281c90>,
       68314: <__main__.Game at 0x12cd5d890>,
       68315: <__main__.Game at 0x12d732dd0>,
       ...
       }
```

Earlier, I showed it was possible to get the shots for a game using the Game object's `get_shots_for_game` method. There is another function I often use, called `get_shots_for_season` which gets the shots for all game in a season dictionary. The output of `fetch_matches_for_season` just needs to be passed in, as below.
```python
  sbd.get_shots_for_season(season_11_37)
  >>> 
```
|shot id	|team_id	|team_name	|player_id	|player_name	|play pattern	|x start location	|y start location	|duration	|outcome	|technique	|first time	|x gk position|	y gk position	|type of shot	|num opponents within 5 yards	|num opponents between shot and goal	|statsbomb xg	|game_id|
| :------ |:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:-------:|:---------:|:---------:|:-----------:|:---------------:|:---------------:|:---------:|:-------------:|--------------:|:-----------:|:--------:|-------------:|
|7799b3d3-eb47-4d1f-9a38-2a9891bd991e|	217|	Barcelona|	5216|	Andr√©s Iniesta Luj√°n	|Regular Play	|112.4	|51.6	|0.542347|	Goal|	Normal|	FALSE|	114.7|	49.4|	Open Play|	2|	0|	0.216037|	69153|
|be5b97e3-fca8-4fb9-99f8-af2e878c8b3b	|217|	Barcelona	|19298	|Samuel Eto"o Fils	|From Counter	|114.4|	59.1|	0.573428	|Saved	|Normal	|FALSE	|119.8	|43.2	|Open Play	|2	|0	|0.019256786	|69153|

A similar thing can be done with the `get_shots_for_league` function to get all shots for a league by passing in the league's dictionary of dictionaries, like `wc_data` from the earlier example.

### Documentation
The official documentation is hosted on Read the Docs: <https://sbdataextraction.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
