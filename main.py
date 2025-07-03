#!/usr/bin/env python
import argparse
import os
import random
import sys
import tkinter as tk
from tkinter import Label

from PIL import Image, ImageTk

# Define your positive good afternoon messages
MESSAGES = [
    "Goedemiddag, {name}!\n Ik hoop dat je dag net zo mooi is als je lach 😊",
    "Hey {name},\n ik wens jou een hele vrolijke middag!",
    "Zon of niet, {name}, jij laat mijn dag stralen ☀️",
    "Hoi {name}, ik wens jou een fijne rustige en productieve dag!",
    "Hallootjes, {name}!\nJij bent geweldig bezig 💪",
    "Wow {name},\nwat een mooie dag om te genieten van het leven!",
    "Goedemiddag, {name}!\nJij maakt de wereld een beetje mooier 🌍",
]

# Directory where background images are stored
IMAGE_DIR = "backgrounds"


def get_random_background() -> str:
    images = [
        f
        for f in os.listdir(IMAGE_DIR)
        if f.lower().endswith((".jpg", ".png", ".jpeg"))
    ]
    if not images:
        print("No background images found in the 'backgrounds/' directory.")
        sys.exit(1)
    return os.path.join(IMAGE_DIR, random.choice(images))


def show_gui(name):
    message = random.choice(MESSAGES).format(name=name)
    bg_path = get_random_background()

    root = tk.Tk()
    root.title("Goedemiddag topper!")

    # Set full screen size
    screen_width = int(root.winfo_screenwidth() / 2)
    screen_height = int(root.winfo_screenheight() / 2)
    root.geometry(f"{screen_width}x{screen_height}")

    # Load and resize image
    img = Image.open(bg_path)
    img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_img = ImageTk.PhotoImage(img)

    background_label = Label(root, image=bg_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add the message
    msg_label = Label(
        root, text=message, font=("Helvetica", 32), bg="#ffffff", fg="black"
    )
    msg_label.pack(pady=120)

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Toon een goedemiddag bericht")
    parser.add_argument("name", help="Wat is de naam van de persoon?")
    args = parser.parse_args()

    show_gui(args.name)


if __name__ == "__main__":
    main()
