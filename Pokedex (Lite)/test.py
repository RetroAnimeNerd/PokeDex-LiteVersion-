import requests

def getPokemonEntry(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)

    # Establishing a connection to the API....
    if response.status_code == 200:
        data = response.json()
        print("Connection Successful")
    else:
        print(f"Connection unsuccesful {response.status_code}")

    pokemon_name = data['name'].capitalize()
    pokemon_id = data['id']
    height = data['height']
    weight = data['weight']
    primaryType = data['types'][0]['type']['name'].capitalize()
    imageData = data['sprites']['front_default']

    statCount = 0
    statString = f"---Base Stats---\n"

    for stat in data['stats']:
        statString += f"{data['stats'][statCount]['stat']['name'].capitalize()}: {data['stats'][statCount]['base_stat']}\n"
        statCount += 1

# Not all pokemon have secondary types. Using try catch to check first
    try:
        secondaryType = data['types'][1]['type']['name'].capitalize()
    except IndexError:
        secondaryType = 'None'

    return pokemon_name, pokemon_id, height, weight, primaryType, secondaryType, imageData, statString


string = getPokemonEntry('Gengar')
print(string)
        