# README

## Project Goal
This project tracks one summoner and provides average stats for the player, as well as keeping track of arbitrary conditions in order to help assist in knowing if the summoner should continue to play Ranked SoloQ in League of Legends. This is intended to be used by the player trying to climb in Ranked SoloQ and indicate potential 'tilt' factors.

### Setup
- Create a virtual environment in PyCharm.
- Install the project requirements using `pip install -r requirements.txt`
- Refresh the `RIOT_API_KEY` in the [Riot Developer Portal](https://developer.riotgames.com/) and set it as an environment variable.

### Potential Arbitrary Conditions
1. Number of losses in a row. If the user has 3 or more losses in a row, they are more likely to be tilted. 
2. Playing a champion the summoner has <10 games on.
3. Teammate is playing a champion that they have <10 games on.
4. Teammate is playing a champion with <45% winrate.
5. How long the summoner has been playing.
6. Rank and previous ranks of teammates.

### Process:
Acquire a summoners match history from the Riot Developer API.
