import requests 

global type_advantage, type_disadvantage

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

    return pokemon_name, pokemon_id, height, weight, primaryType, secondaryType, imageData



def checkTypeAdvantage(pokemonType):
    
    if pokemonType in type_advantage:
        advantage = f"This pokemon is strong against {type_advantage[pokemonType]} type pokemon"
    else:
        advantage = f"{pokemonType} pokemon Type Not Found"
        
    if pokemonType in type_disadvantage:
        disadvantage = f"This pokemon is weakest against {type_disadvantage[pokemonType]} type pokemon"
    else: 
        disadvantage = f"{pokemonType} pokemon type Not Found"

    return advantage, disadvantage

def comparePokemon(Pokemon1, Pokemon2):
    f_name, f_id, f_height, f_weight, f_primaryType, f_secondaryType, f_imageData = getPokemonEntry(Pokemon1)
    s_name, s_id, s_height, s_weight, s_primaryType, s_secondaryType, s_imageData = getPokemonEntry(Pokemon2)

    f_pokemonString = f"-------Pokedex Entry------\nPokeDex ID: {f_id}\nPokemon Name: {f_name}\nHeight: {f_height} inches\nWeight: {f_weight} pounds(lb)\nPrimary Type: {f_primaryType}\nSecondary Type: {f_secondaryType}\n"
    s_pokemonString = f"-------Pokedex Entry------\nPokeDex ID: {s_id}\nPokemon Name: {s_name}\nHeight: {s_height} inches\nWeight: {s_weight} pounds(lb)\nPrimary Type: {s_primaryType}\nSecondary Type: {s_secondaryType}\n"

    # Compare the two pokemon
    if f_id == s_id:
        typeAdvantageResults = f"These pokemon are the same do not piss me off!"
        return f_pokemonString, s_pokemonString, typeAdvantageResults
    
    else:
        if f_primaryType in type_disadvantage[s_primaryType]:
            typeAdvantageResults = f"{f_name} is strong against {s_name}"
        if f_primaryType in type_advantage[s_primaryType]:
            typeAdvantageResults = f"{s_name} is strong against {f_name}"
        else:
            typeAdvantageResults = f"No distinct type advantage between {f_name} and {s_name}"
            
        return f_pokemonString, s_pokemonString, typeAdvantageResults


    
    