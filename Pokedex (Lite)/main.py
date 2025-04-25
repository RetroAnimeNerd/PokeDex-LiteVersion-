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
        "Fairy": {"Fighting", "Dragon", "Dark"},
        "None": {}
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
        "Fairy": {"Poison", "Steel"},
        "None": {}       
    }


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
    baseStatTotal = 0
    statString = f"--------Base Stats--------\n"

    for stat in data['stats']:
        baseStatValue = int(data['stats'][statCount]['base_stat'])
        baseStatTitle = data['stats'][statCount]['stat']['name'].capitalize()
        statString += f"{baseStatTitle}: {baseStatValue}\n"
        baseStatTotal += baseStatValue
        statCount += 1

# Not all pokemon have secondary types. Using try catch to check first
    try:
        secondaryType = data['types'][1]['type']['name'].capitalize()
    except IndexError:
        secondaryType = 'None'

    return pokemon_name, pokemon_id, height, weight, primaryType, secondaryType, statString, baseStatTotal, imageData



def checkTypeAdvantage(pokemonPrimaryType, pokemonSecondaryType):

    advantageList = []
    disadvantageList = []
    a_string = ""
    d_string = ""

    a_count = 0
    d_count = 0

    if pokemonPrimaryType or pokemonSecondaryType in type_disadvantage:
        for pokeType in type_disadvantage[pokemonPrimaryType]:
            disadvantageList.append(pokeType)
        if pokemonSecondaryType != 'None':
            for pokeType in type_disadvantage[pokemonSecondaryType]:
                disadvantageList.append(pokeType)

    if pokemonPrimaryType or pokemonSecondaryType in type_advantage:
        for pokeType in type_advantage[pokemonPrimaryType]:
            advantageList.append(pokeType)
        
        if pokemonSecondaryType != 'None': 
            for pokeType in type_advantage[pokemonSecondaryType]:
                advantageList.append(pokeType)

    
    for a in advantageList:
        a_length = len(advantageList)
        if a_length == 1:
            a_string += f"{a}"
            break
        if a_count == a_length - 1 and a_length > 1:
            a_string += f"and, {a}"
        else: 
            a_count += 1
            a_string += f"{a}, "
    advantage = f"This pokemon is strong against {a_string} type pokemon"


    for d in disadvantageList:
        d_length = len(disadvantageList)
        if d_length == 1: 
            d_string += f"{d}"
            break
        if d_length > 1 and d_count == d_length - 1:
            d_string += f"and, {d}"
        else:
            d_string += f"{d}, "
            d_count += 1
    disadvantage = f"This pokemon is weak against {d_string} type pokemon"

    return advantage, disadvantage




def comparePokemon(Pokemon1, Pokemon2):
    f_name, f_id, f_height, f_weight, f_primaryType, f_secondaryType, f_statString, f_baseStatTotal,  f_imageData = getPokemonEntry(Pokemon1)
    s_name, s_id, s_height, s_weight, s_primaryType, s_secondaryType, s_statString, s_baseStatTotal, s_imageData = getPokemonEntry(Pokemon2)

    f_pokemonString = f"-------Pokedex Entry------\nPokeDex ID: {f_id}\nPokemon Name: {f_name}\nHeight: {f_height} meters\nWeight: {f_weight} pounds(lb)\nPrimary Type: {f_primaryType}\nSecondary Type: {f_secondaryType}\n{f_statString}\nBase Total: {f_baseStatTotal}"
    s_pokemonString = f"-------Pokedex Entry------\nPokeDex ID: {s_id}\nPokemon Name: {s_name}\nHeight: {s_height} meters\nWeight: {s_weight} pounds(lb)\nPrimary Type: {s_primaryType}\nSecondary Type: {s_secondaryType}\n{s_statString}\nBase Total: {s_baseStatTotal}"

    # Compare the two pokemon
    f_hasAdvantage = False
    s_hasAdvantage = False
    typeAdvantageResults = ""

    if f_id == s_id:
        typeAdvantageResults = f"These pokemon are the same do not piss me off!"
        return f_pokemonString, s_pokemonString, typeAdvantageResults
    else:
        if f_primaryType in type_disadvantage[s_primaryType] or f_primaryType in type_disadvantage[s_secondaryType]:
            f_hasAdvantage = True
        if f_secondaryType in type_disadvantage[s_primaryType] or f_secondaryType in type_disadvantage[s_secondaryType]:
            f_hasAdvantage = True                 
        if s_primaryType in type_disadvantage[f_primaryType] or s_primaryType in type_disadvantage[f_secondaryType]:
            s_hasAdvantage = True
        if s_secondaryType in type_disadvantage[f_primaryType] or s_secondaryType in type_disadvantage[f_secondaryType]:
            s_hasAdvantage = True
        
        if f_hasAdvantage == True: 
            string = f"{f_name} has a type advantage over {s_name}\n"
            typeAdvantageResults += string
        if s_hasAdvantage == True:
            string = f"{s_name} has a type advantage over {f_name}\n"
            typeAdvantageResults += string
   
        return f_pokemonString, s_pokemonString, typeAdvantageResults


    
    