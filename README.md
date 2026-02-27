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

## 🧩 Backend Setup

### Install Dependencies
pip install -r requirements.txt

## Run FastAPI Server
uvicorn main:app --reload
