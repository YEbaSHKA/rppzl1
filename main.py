import requests

url = 'https://swapi.dev/api/starships/22/'

resp = requests.get(f"{url}")
f = open("Rppzl_1.txt", "wt")

for key, value in dict.items(resp.json()):
    f.write(key + " : " + str(value) + '\n')
f.close()