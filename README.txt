Deckly Flashcard App
====================

Description:
------------
Deckly is a simple flashcard application built with Python's tkinter for the user interface and FastAPI for the backend. 
It allows users to view, flip, navigate, and reshuffle flashcards.

How It Works:
-------------
- The backend (FastAPI) serves flashcard data via HTTP endpoints.
- The frontend (tkinter) fetches flashcards from the backend and displays them in a window.
- Users can flip cards to see answers, go to the next card, and reshuffle the deck.

Setup Instructions:
-------------------
1. Install required Python packages:
   - Open a terminal and run:
     pip install fastapi uvicorn requests

2. Start the FastAPI backend:
   - In your project folder, run:
     uvicorn main:app --reload
   - The backend will run on http://localhost:8000

3. Run the tkinter frontend:
   - In your project folder, run:
     python app.py

Usage:
------
- "Flip card" button: Shows the answer to the current flashcard.
- "Next card" button: Moves to the next flashcard in the deck.
- "Reshuffle card" button: Randomizes the order of the flashcards.

Troubleshooting:
----------------
- If flashcards do not appear, make sure the backend is running and accessible at http://localhost:8000/flashcards.
- If you see connection errors, check that you started the backend before running the frontend.

Files:
------
- main.py   : FastAPI backend serving flashcard data.
- app.py    : tkinter frontend for interacting with flashcards.

Author:
-------
Serwaa Osei-Poku
