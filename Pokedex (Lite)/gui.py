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
    details, image_src, primaryType = m.getPokemonEntry(pokemon_name)
    advantage, disadvantage = m.checkTypeAdvantage(str(primaryType))
    photo = loadImage(image_src)

    global tk_img
    tk_img = ImageTk.PhotoImage(photo)

    label_0.config(text=details)
    label_1.config(image=tk_img)
    label_2.config(text=advantage)
    label_3.config(text=disadvantage)

def show_frame(frame):
    frame.tkraise()

# Tkinter setup
root = tk.Tk()
root.title("PokeDex Lite")
root.geometry("600x500")

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
pokedex_container.pack(expand=True)

btn_return = tk.Button(pokedex_container, text="Return to Main Menu", command=lambda: show_frame(main_frame))
btn_return.pack(pady=5)

label_box = tk.Frame(pokedex_container)
label_box.pack(pady=5)

label_0 = tk.Label(pokedex_container, text="Enter a Pokémon name...", font=("Arial", 14))
label_0.pack(pady=5)

label_1 = tk.Label(pokedex_container)  # Image label
label_1.pack()

label_2 = tk.Label(pokedex_container, font=("Arial", 14))
label_2.pack(pady=5)

label_3 = tk.Label(pokedex_container, font=("Arial", 14))
label_3.pack(pady=5)

entry = tk.Entry(pokedex_container, width=30)
entry.pack(pady=5)

btn_submit = tk.Button(pokedex_container, text="Submit", command=runScript)
btn_submit.pack(pady=5)

# Type Advantage Calculator Frame
advantage_container = tk.Frame(advantage_calc)
advantage_container.pack(expand=True)

btn_return2 = tk.Button(advantage_container, text="Return to Main Menu", command=lambda: show_frame(main_frame))
btn_return2.pack(pady=5)

typeAdv_Label = tk.Label(advantage_container, text="Functionality coming soon...", font=("Arial", 12))
typeAdv_Label.pack(pady=5)

# Show the main menu initially
show_frame(main_frame)
root.mainloop()
