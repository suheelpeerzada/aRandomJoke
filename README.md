🎉 Random Joke API + Favourites (FastAPI + JS Frontend)

A simple backend + frontend project that:

Fetches random jokes from an external API

Saves your favourite jokes locally

Lists all saved jokes

Allows deleting favourite jokes

Includes a lightweight HTML/JS UI

Is ready to be containerized with Docker

Perfect for learning FastAPI, REST APIs, CRUD, frontend fetch(), and Docker basics.

🚀 Features
Backend (FastAPI)

GET /joke/random → Fetch a random joke

POST /favourites → Save a favourite joke

GET /favourites → List all favourite jokes

DELETE /favourites/{id} → Delete a favourite joke

Stores favourites inside data/favjokes.json

Clean architecture (CRUD, external API layer, router layer)

CORS enabled (for HTML frontend)

Frontend (HTML + CSS + JavaScript)

Click button to fetch a random joke

Save joke to favourites

Display list of favourites

Delete favourite joke

Uses simple fetch() calls to the backend
