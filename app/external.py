#this file is used to encapsulate all HTTP requests to outside APIs
#we can put as many external APIs here as we want
import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    joke = requests.get(url)

    if joke.status_code != 200:
        return {"error": "Could not fetch joke"}
    
    y = joke.json()
    return {'setup':y["setup"], 'punchline':y["punchline"]}