from riotwatcher import LolWatcher, ApiError
import json
import os

def save_json_from_url_link(url):
    # Get the latest champions.json and save it to the data dir for processing
    url = f"http://ddragon.leagueoflegends.com/cdn/{current_patch_version}.1/data/en_US/champions.json"
    new_data = json.load(urllib2.urlopen(url))
    print(f'Getting the latest "champions.json" file for version ({new_data["version"]}).')

    # Generalized path names
    main_root = os.path.dirname(os.path.realpath("__file__"))
    data_path = os.path.join(main_root, "data/")
    print("data_path: ", data_path)
    # Build the full path from the data directory
    full_path = data_path + "champions.json"
    print("[champions.json] output path", full_path)
    with open(full_path, "w") as outfile:
        json.dump(new_data, outfile)