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
    imageData = data['sprites']['front_default']

# Not all pokemon have secondary types. Using try catch to check first
    try:
        secondaryType = data['types'][1]['type']['name'].capitalize()
    except IndexError:
        secondaryType = 'None'
        
    returnString = f"-------Pokedex Entery------\nPokeDex ID: {pokemon_id}\nPokemon Name: {pokemon_name}\nHeight: {height} inches\nWeight: {weight} pounds(lb)\nPrimary Type: {primaryType}\nSecondaryType: {secondaryType}\n"
    
    return returnString, imageData, primaryType

def checkTypeAdvantage(pokemonType):
    type_advantage = {
        "Normal": {},
        "Fire": {"Grass", "Bug", "Ice", "Steel"},
        "Water": {"Fire", "Ground", "Rock"}, 
        "Grass": {"Water", "Ground", "Rock"},
        "Electric": {"Water", "Flying"},
        "Ice": {"Grass", "Ground", "Flying", "Dragon"},
        "Fighting": {"Normal", "Ice", "Rock", "Dark", "Steel"},
        "Poison": {"Grass", "Fairy"},
        "Ground": {"Fire", "Electric", "Poison", "Rock", "Steel"},
        "Flying": {"Grass", "Fighting", "Bug"},
        "Psychic": {"Fighting", "Poison"},
        "Bug": {"Grass", "Psychic"},
        "Rock": {"Fire", "Ice", "Flying", "Bug"},
        "Ghost": {"Psychic", "Ghost"},
        "Dragon":{"Dragon"},
        "Dark": {"Psychic", "Ghost"},
        "Steel":{"Ice", "Rock", "Fairy"},
        "Fairy": {"Fighting", "Dragon", "Dark"}
    }

    type_disadvantage = {
        "Normal": {"Fighting"},
        "Fire": {"Water", "Ground", "Rock"},
        "Water": {"Grass", "Electric"}, 
        "Grass": {"Fire", "Ice", "Poison", "Flying", "Bug"},
        "Electric": {"Ground"},
        "Ice": {"Fire", "Fighting", "Rock", "Steel"},
        "Fighting": {"Flying", "Psychic", "Fairy"},
        "Poison": {"Ground", "Psychic"},
        "Ground": {"Water", "Grass", "Ice", },
        "Flying": {"Electric", "Ice", "Rock"},
        "Psychic": {"Bug", "Ghost", "Steel"},
        "Bug": {"Fire", "Flying", "Rock"},
        "Rock": {"Water", "Grass", "Fighting", "Ground", "Steel"},
        "Ghost": {"Ghost", "Dark"},
        "Dragon":{"Ice", "Dragon", "Fairy"},
        "Dark": {"Fighting", "Bug", "Fairy"},
        "Steel":{"Fire", "Fighting", "Ground", },
        "Fairy": {"Poison", "Steel"}       
    }
    
    if pokemonType in type_advantage:
        advantage = f"This pokemon is strong against {type_advantage[pokemonType]} type pokemon"
    else:
        advantage = f"{pokemonType} pokemon Type Not Found"
        
    if pokemonType in type_disadvantage:
        disadvantage = f"This pokemon is weakest against {type_disadvantage[pokemonType]} type pokemon"
    else: 
        disadvantage = f"{pokemonType} pokemon type Not Found"

    return advantage, disadvantage
    
    