import requests
from pprint import pprint

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url, timeout=5)
if resp.status_code == 200:
    resp_json = resp.json()
else:
    print('Ошибка!')

heroes_list = ['Hulk', 'Captain America', 'Thanos']
heroes_tuple = {}
for some_hero in resp_json:
    for name in some_hero.keys():
        if name == 'name' and some_hero[name] in heroes_list:
            intelligence = int(some_hero['powerstats']['intelligence'])
            heroes_tuple[some_hero[name]] = intelligence

print(f"У персонажа {max(heroes_tuple)} самый высокий интеллект = {heroes_tuple[max(heroes_tuple)]}")


