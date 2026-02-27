#fastAPI logic here.
from fastapi import APIRouter, Body
from app.crud import add_favourite, list_fav, delete_fav
from app.external import get_joke

route = APIRouter()
@route.get("/joke/random")
def random_joke():
    return get_joke()

@route.post("/favourites")
def add_fav(joke: str = Body(...)):
    return add_favourite(joke)

@route.get("/favourites")
def fav_jokes():
    return list_fav()

@route.delete("/favourites/{id}")
def del_joke(id:str):
    return delete_fav(id)