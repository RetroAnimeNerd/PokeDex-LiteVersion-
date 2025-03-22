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
    details, image_src = m.getPokemonEntry(pokemon_name)
    photo = loadImage(image_src)

    global tk_img
    tk_img = ImageTk.PhotoImage(photo)

    label_0.config(text=details)
    label_1.config(image=tk_img)

def show_frame(frame):
    frame.tkraise()


# Tkinter code
root = tk.Tk()
root.title = ("PokeDex Lite")
root.geometry("300x350")

# Initializing the frames that will be used...
main_frame = tk.Frame(root)
pokedex_frame = tk.Frame(root)
advantage_calc = tk.Frame(root)

frames_array = [main_frame, pokedex_frame, advantage_calc]

for frame in frames_array:
    frame.grid(row=0, column=0, sticky="nsew")

# Main frame attributes...
label_main = tk.Label(main_frame, text="Main menu")
label_main.pack(pady=10)

btn_pokedex = tk.Button(main_frame, text="Use Pokedex", command=lambda: show_frame(pokedex_frame))
btn_pokedex.pack()

btn_advantageCalc = tk.Button(main_frame, text="Compare Pokemon", command=lambda: show_frame(advantage_calc))
btn_advantageCalc.pack()

# Pokedex Frame attributes (adding a return to main menu button)...
btn_return = tk.Button(pokedex_frame, text="Return to main menu", command=lambda: show_frame(main_frame))
btn_return.pack()

label_0 = tk.Label(pokedex_frame, text="Enter a pokemon name...")
label_0.pack()

label_1 = tk.Label(pokedex_frame)
label_1.pack()

entry = tk.Entry(pokedex_frame, width=30)
entry.pack()

btn_submit = tk.Button(pokedex_frame, text="Submit", command=runScript)
btn_submit.pack(pady=5)

# Type advantage calculator...

btn_return2 = tk.Button(advantage_calc, text="Return to main menu", command=lambda: show_frame(main_frame))
btn_return2.pack()

typeAdv_Label = tk.Label(advantage_calc, text="Functionality comming soon...")
typeAdv_Label.pack()

show_frame(main_frame)
root.mainloop()

