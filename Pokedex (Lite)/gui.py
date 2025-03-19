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

    lable_0.config(text=details)
    lable_1.config(image=tk_img)


# Tkinter code
root = tk.Tk()
root.title("PokeDex")
root.geometry("325x300")

# Attributes 
lable_0 = tk.Label(root, text="Main Lable")
lable_0.pack()

lable_1 = tk.Label(root, image="")
lable_1.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Submit", command=runScript)
button.pack()

#Main Application Loop
root.mainloop()