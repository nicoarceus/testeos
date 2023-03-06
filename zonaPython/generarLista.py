import os
os.system('cls')

import requests

x = requests.get('https://pokeapi.co/api/v2/berry/1/')    

print(x.text)
