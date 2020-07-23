from riotwatcher import LolWatcher, ApiError

from get_match import get_history, player_win_loss
from get_summoner import get_summoner_accountId


if __name__ == '__main__':
    lol_watcher = LolWatcher('')  # Get lolwatcher with riot API key
    my_region = 'na1'
    summoner_name = 'Slayre'
    number_of_games = 5
    me_dict = lol_watcher.summoner.by_name(my_region, 'Slayre')
    current_version = lol_watcher.data_dragon.versions_for_region(my_region)  # Check for current version on na1 server

    my_summoner_accountId = get_summoner_accountId(my_region, summoner_name, lol_watcher)
    print(lol_watcher.summoner.by_name(my_region, summoner_name))

    print(lol_watcher.match.matchlist_by_account(my_region, my_summoner_accountId, {420}, end_index=number_of_games))
    match2 = lol_watcher.match.matchlist_by_account(my_region, my_summoner_accountId, {420}, end_index=number_of_games)
    match = lol_watcher.match.by_id(my_region, 3502265420)

    print(match)
    print(match['teams'][0]['teamId'])
    print(match['teams'][0]['win'])
    print(match)

    for participantId in match['participants']:
        if participantId['championId'] == 15:
            print('hi')
            print(participantId)

    for i in range(match2.get('endIndex')):
        print(match2['matches'][i]['gameId'])

    print()
    last_three_games = get_history(my_region, my_summoner_accountId, lol_watcher, number_of_games)
    print(last_three_games)
    wins, losses = player_win_loss(my_region, last_three_games, lol_watcher)
    print(wins)
    print(losses)