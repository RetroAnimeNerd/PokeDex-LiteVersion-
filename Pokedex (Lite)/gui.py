import tkinter as tk
import main as m
import requests
from PIL import Image, ImageTk
from io import BytesIO

def loadImage(image_src):
    response = requests.get(image_src)
    imgData = response.content
    img = Image.open(BytesIO(imgData))
    return img

# Functions 
def runScript():
    pokemon_name = entry.get()
    pokemon_name, pokemon_id, height, weight, primaryType, secondaryType, imageData = m.getPokemonEntry(pokemon_name)
    advantage, disadvantage = m.checkTypeAdvantage(str(primaryType))
    photo = loadImage(imageData)

    global tk_img
    tk_img = ImageTk.PhotoImage(photo)

    label_0.config(text=f"-------Pokedex Entry------\nPokeDex ID: {pokemon_id}\nPokemon Name: {pokemon_name}\nHeight: {height} inches\nWeight: {weight} pounds(lb)\nPrimary Type: {primaryType}\nSecondary Type: {secondaryType}\n", font=("Arial", 14))
    label_1.config(image=tk_img)
    label_2.config(text=advantage)
    label_3.config(text=disadvantage)

def show_frame(frame):
    frame.tkraise()

def compareThesePokemon():
    firstPokemon = firstPokemonEntry.get()
    secondPokemon = secondPokemonEntry.get()



    first, second, comparison_result = m.comparePokemon(firstPokemon, secondPokemon)


    firstPokemonResults.config(text=first)
    secondPokemonResults.config(text=second)
    comparisonResults_lbl.config(text=comparison_result)




# Tkinter setup
root = tk.Tk()
root.title("PokeDex Lite")
root.geometry("500x500")

# Configure grid layout to center frames
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frames
main_frame = tk.Frame(root)
pokedex_frame = tk.Frame(root)
advantage_calc = tk.Frame(root)

for frame in (main_frame, pokedex_frame, advantage_calc):
    frame.grid(row=0, column=0, sticky="nsew")




# Main Menu
label_main = tk.Label(main_frame, text="Main Menu", font=("Arial", 14))
label_main.pack(pady=10)

btn_pokedex = tk.Button(main_frame, text="Use Pokedex", command=lambda: show_frame(pokedex_frame))
btn_pokedex.pack(pady=5)

btn_advantageCalc = tk.Button(main_frame, text="Compare Pokemon", command=lambda: show_frame(advantage_calc))
btn_advantageCalc.pack(pady=5)







# Pokedex Frame
pokedex_container = tk.Frame(pokedex_frame)
pokedex_container.pack(expand=False)

btn_return = tk.Button(pokedex_container, text="Return to Main Menu", command=lambda: show_frame(main_frame))
btn_return.pack()

label_0 = tk.Label(pokedex_container, text="Enter a Pokémon name...", font=("Arial", 14))
label_0.pack()

label_1 = tk.Label(pokedex_container)  # Image label
label_1.pack()

label_2 = tk.Label(pokedex_container, font=("Arial", 14))
label_2.pack()

label_3 = tk.Label(pokedex_container, font=("Arial", 14))
label_3.pack()

entry = tk.Entry(pokedex_container, width=30)
entry.pack()

btn_submit = tk.Button(pokedex_container, text="Submit", command=runScript)
btn_submit.pack()








# Type Advantage Calculator Frame
advantage_container = tk.Frame(advantage_calc)
advantage_container.pack(expand=False)

btn_return2 = tk.Button(advantage_container, text="Return to Main Menu", command=lambda: show_frame(main_frame))
btn_return2.pack(pady=5)

firstPokemonEntry = tk.Entry(advantage_container, width=30)
firstPokemonEntry.pack(pady=2)

secondPokemonEntry = tk.Entry(advantage_container, width=30)    
secondPokemonEntry.pack(pady=2)

# Side by side comparison of the two quried pokemon

firstPokemonSection = tk.Frame(advantage_container, pady=10, padx=10, relief=tk.RIDGE, borderwidth=2)
firstPokemonSection.pack(side=tk.LEFT)
firstPokemonResults = tk.Label(firstPokemonSection)
firstPokemonResults.pack()

secondPokemonSection = tk.Frame(advantage_container, pady=10, padx=10, relief=tk.RIDGE, borderwidth=2)
secondPokemonSection.pack(side=tk.RIGHT)
secondPokemonResults = tk.Label(secondPokemonSection)
secondPokemonResults.pack()

comparisonResults_lbl = tk.Label(advantage_calc)
comparisonResults_lbl.pack(pady=2)

btn_compare = tk.Button(advantage_container, text="Compare", command=compareThesePokemon)
btn_compare.pack(pady=5)


# Show the main menu initially
show_frame(main_frame)
root.mainloop()
