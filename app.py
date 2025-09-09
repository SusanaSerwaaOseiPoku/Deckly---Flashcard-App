##We need to first import the necessary libraries

import tkinter as tk
import requests
import json

##This creates a main window for your application
root=tk.Tk()
root.title("Deckly")
root.geometry("400x300") ##This sets the size of the window

##These variables will show which cards are being shown   and also store the flashcards
current_index=0
flashcards=[]


##We are creating a function that is connected to the locsl web browser
def fetch_flashcards():
    global flashcards  ##This tells python to use the global variable flashcards
    try:
        response=requests.get("http://localhost:8000/flashcards") ##
        response.raise_for_status() ##This checks if the request was successful
        flashcards=response.json() ##This converts the response to a json object
        if flashcards:
         show_flashcards(0) ##This shows the first flashcard
    except requests.exceptions.RequestException as e:
       print(f"Error fetching flashcards: {e}")
       error_label=tk.Label(root, text="Error loading flashcards", font=("Helvetica", 12), bg="beige", fg="pink")
       error_label.pack(pady=50)

    ##This functions updates the texts on the screen.
    # It gets the current flashcard and updates our list and sets the texts of our labels to the question.
    def show_flashcards(index):
       global current_index
       current_index = index
       card = flashcards[current_index]
       card_label.config(text=card["question"])
       flip_button.config(state=tk.NORMAL)


## This function checks if the current card is a question or answer
def flip_card():
   card=flashcards[current_index]  ##This points to the exact card you need
   if card_label.cget("text")==card["question"]:
      card_label.config(text=card["answer"])     
   else:
      card_label.config(text=card["question"])

def next_card():
    global current_index
    if flashcards:
        current_index = (current_index + 1) % len(flashcards)
        show_flashcards(current_index)

 ##Next step is to create the UI widgets
 #Pack automatically places the widgets inside the window
card_frame=tk.Frame(root, bg="beige",width=300, height=150, bd=2, relief="groove")    
card_frame.pack(pady=20) #This adds some space around the frame
card_frame.pack_propagate(False)##This prevents the frame from resizing to fit its contents

#Create a label that can hold text and put it inside the card_frame. The label's text will be empty at first. If the text is longer than a specific width,
#  it will automatically wrap to the next line. The text will be in the Helvetica font and have a size of 18."
card_label=tk.Label(card_frame, text="", wraplength=280, font=("Helvetica", 16))
card_label.place(relx=0.5, rely=0.5, anchor="center")## This centers the label in the frame


flip_button= tk.Button(root, text="flip card", command=flip_card, state=tk.DISABLED)
flip_button.pack(pady=10)##This adds some space around the button
next_button=tk.Button(root, text="Next card", command=next_card)
next_button.pack(pady=10)##This adds some space around the button

fetch_flashcards() ##This fetches the data from our backend
root.mainloop() ##This starts the tkinter event loop