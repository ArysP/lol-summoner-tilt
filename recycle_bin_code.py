champion_version = current_version['n']['champion']  #
champions_list = lol_watcher.data_dragon.champions(champion_version)
items_list = lol_watcher.data_dragon.items(champion_version)


print(current_version)
print(champion_version)
print(champions_list)

for v in champions_list.values():
    print('value = ', v)

for k in champions_list.keys():
    print('key = ', k)

for i in champions_list.items():
    print('item = ', i)
print()
print('champions ')
print(champions_list['data'].get('Ahri', ''))
print()
print('Items list')
print(items_list)
print()
print('Summoner: ')
print(me)
print()
print('Summoner ID: ')
print(get_summoner_id(my_region, 'Slayre'))
myid = (get_summoner_id(my_region, 'Slayre'))
print()
print(lol_watcher.clash.by_summoner(my_region, myid))