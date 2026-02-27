# 🎉 Random Joke API + Favourites  
A simple backend + frontend project that lets you fetch random jokes, save them as favourites, view them, and delete them — built with **FastAPI**, **Python**, **HTML/CSS/JS**, and optionally **Docker**.

Perfect for learning:  
- FastAPI  
- CRUD operations  
- REST APIs  
- JSON storage  
- Frontend `fetch()`  
- Docker basics  

---

## 🚀 Features

### 🔹 Backend (FastAPI)
- `GET /joke/random` → Fetch a random joke from external API  
- `POST /favourites` → Save a favourite joke  
- `GET /favourites` → List all favourite jokes  
- `DELETE /favourites/{id}` → Delete a favourite joke  
- Stores favourites in `data/favjokes.json`  
- Proper router structure (`api.py`, `crud.py`, `external.py`)  
- CORS enabled for frontend

### 🔹 Frontend (HTML + CSS + JavaScript)
- Fetches and displays random jokes  
- Save joke to favourites  
- Load all favourites  
- Delete favourite joke  
- Uses simple `fetch()` calls to interact with backend  

---

## 📁 Project Structure
project/
│
├── app/
│ ├── api.py # API routes (router)
│ ├── crud.py # Add, list, delete favourite jokes
│ ├── external.py # Fetch jokes from external API
│ ├── main.py # FastAPI app + router + CORS
│ └── pycache/ # Ignored
│
├── data/
│ └── favjokes.json # User jokes (ignored in git)
│
├── frontend/
│ ├── index.html # UI page
│ ├── style.css # Page styling
│ └── script.js # Fetch logic
│
├── Dockerfile # Docker container definition
├── requirements.txt # Python dependencies
└── README.md # Documentation

---

## 🧩 Backend Setup

### Install Dependencies
pip install -r requirements.txt

## Run FastAPI Server
uvicorn main:app --reload
