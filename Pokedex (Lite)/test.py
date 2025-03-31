def checkTypeAdvantage(pokemonType, inquery):
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

    if inquery == "advantage":
        for a in type_advantage:
            if a == pokemonType:
                print(f"This {pokemonType} type pokemon is strong against {type_advantage[pokemonType]} type pokemon")
            




checkTypeAdvantage("Ghost", "advantage")

