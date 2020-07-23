from riotwatcher import LolWatcher, ApiError
import json


def get_summoner_id(region, summoner, lol_watcher):
    summoner_info = lol_watcher.summoner.by_name(region, summoner)
    summoner_id = summoner_info.get('id')
    return summoner_id


def get_summoner_puuid(region, summoner, lol_watcher):
    summoner_info = lol_watcher.summoner.by_name(region, summoner)
    summoner_id = summoner_info.get('puuid')
    return summoner_id


def get_summoner_accountId(region, summoner, lol_watcher):
    summoner_info = lol_watcher.summoner.by_name(region, summoner)
    summoner_id = summoner_info.get('accountId')
    return summoner_id








