from riotwatcher import LolWatcher, ApiError
import json
import get_summoner


def get_history(region, summoner, lol_watcher, number_of_games):
    game_champion = {}
    history = lol_watcher.match.matchlist_by_account(region, summoner, {420}, end_index=number_of_games)
    for i in range(history.get('endIndex')):
        game_champion.setdefault(history['matches'][i]['gameId'], history['matches'][i]['champion'])
    return game_champion


def player_win_loss(my_region, game_champion, lol_watcher):
    wins = 0
    losses = 0
    for gameId, champion in game_champion.items():
        game = lol_watcher.match.by_id(my_region, gameId)
        if game['teams'][0]['win'] == 'Win':
            red_win = False
            blue_win = True
        else:
            red_win = True
            blue_win = False
        if red_win:
            print('red won')
            for participantId in game['participants']:
                if participantId['championId'] == champion and participantId['teamId'] == 200:
                    wins += 1
                    print('and you were red side, so you won')
                elif participantId['championId'] == champion and participantId['teamId'] == 100:
                    losses += 1
        elif blue_win:
            print('blue won')
            for participantId in game['participants']:
                if participantId['championId'] == champion and participantId['teamId'] == 200:
                    losses += 1
                elif participantId['championId'] == champion and participantId['teamId'] == 100:
                    wins += 1
                    print('and you were blue side, so you won')
    return wins, losses


def consecutive_win_loss(my_region, game_champion, win_loss, lol_watcher):
    for gameId, champion in game_champion.items():
        game = lol_watcher.match.by_id(my_region, gameId)
        if game['teams'][0]['win'] == 'Win':
            red_win = False
            blue_win = True
        else:
            red_win = True
            blue_win = False
        if red_win:
            print('red won')
            for participantId in game['participants']:
                if participantId['championId'] == champion and participantId['teamId'] == 200:
                    wins += 1
                    print('and you were red side, so you won')
                elif participantId['championId'] == champion and participantId['teamId'] == 100:
                    losses += 1
        elif blue_win:
            print('blue won')
            for participantId in game['participants']:
                if participantId['championId'] == champion and participantId['teamId'] == 200:
                    losses += 1
                elif participantId['championId'] == champion and participantId['teamId'] == 100:
                    wins += 1
                    print('and you were blue side, so you won')
    return consecutive_wins, consecutive_losses