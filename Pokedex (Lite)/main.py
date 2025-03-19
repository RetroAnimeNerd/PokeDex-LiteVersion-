import requests 

# Custom function for getting pokemon data....
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
    imageData = data['sprites']['front_shiny']

# Not all pokemon have secondary types. Using try catch to check first
    try:
        secondaryType = data['types'][1]['type']['name'].capitalize()
    except IndexError:
        secondaryType = 'None'
        
    returnString = f"-------Pokedex Entery------\nPokeDex ID: {pokemon_id}\nPokemon Name: {pokemon_name}\nHeight: {height}\nWeight: {weight}\nPrimary Type: {primaryType}\nSecondaryType: {secondaryType}\n"
    
    return returnString, imageData