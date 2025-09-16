# We need to first import the necessary libraries

import tkinter as tk
import requests
import json

# This creates the main window for your application
root = tk.Tk()
root.title("Deckly")
root.geometry("400x300")  # This sets the size of the window

# These variables show which card is being displayed and also store the flashcards
current_index = 0
flashcards = []

# This function connects to the local web server and fetches flashcards
def fetch_flashcards():
    global flashcards  # This tells Python to use the global variable flashcards
    try:
        response = requests.get("http://localhost:8000/flashcards")
        response.raise_for_status()  # This checks if the request was successful
        flashcards = response.json()  # This converts the response to a JSON object
        if flashcards:
            show_flashcards(0)  # This shows the first flashcard
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flashcards: {e}")
        error_label = tk.Label(root, text="Error loading flashcards", font=("Helvetica", 12), bg="beige", fg="pink")
        error_label.pack(pady=50)

# This function updates the text on the screen.
# It gets the current flashcard, updates our index, and sets the label text to the question.
def show_flashcards(index):
    global current_index
    current_index = index
    card = flashcards[current_index]
    card_label.config(text=card["question"])
    flip_button.config(state=tk.NORMAL)

def flip_card():
    if not flashcards or current_index >= len(flashcards):
        return
    card = flashcards[current_index]  # This points to the exact card you need
    if card_label.cget("text") == card["question"]:
        card_label.config(text=card["answer"])
    else:
        card_label.config(text=card["question"])

def next_card():
    global current_index
    if flashcards:
        current_index = (current_index + 1) % len(flashcards)
        show_flashcards(current_index)

# Next, create the UI widgets
# pack() automatically places the widgets inside the window
card_frame = tk.Frame(root, bg="beige", width=300, height=150, bd=2, relief="groove")
card_frame.pack(pady=20)  # This adds some space around the frame
card_frame.pack_propagate(False)  # This prevents the frame from resizing to fit its contents

# Create a label that can hold text and put it inside the card_frame.
# The label's text will be empty at first. If the text is longer than a specific width,
# it will automatically wrap to the next line. The text will be in the Helvetica font, size 16.
card_label = tk.Label(card_frame, text="", wraplength=280, font=("Helvetica", 16))
card_label.place(relx=0.5, rely=0.5, anchor="center")  # This centers the label in the frame

flip_button = tk.Button(root, text="Flip card", command=flip_card)
flip_button.pack(pady=10)  # This adds some space around the button
next_button = tk.Button(root, text="Next card", command=next_card)
next_button.pack(pady=10)  # This adds some space around the button

fetch_flashcards()  # This fetches the data from our backend
root.mainloop()  # This starts the tkinter event loop