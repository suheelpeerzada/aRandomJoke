#CRUD operations are here
import json
import os
from datetime import datetime
def add_favourite(joke:str):
    file = "data/favjokes.json"
    if os.path.exists(file):
        with open(file, 'r') as f:
            y = json.load(f)
        id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        myjoke = {
            'id': id,
            'content': joke
        }
        y.append(myjoke)
        with open(file, "w") as f:
            json.dump(y,f, indent=2)
    else:
        myjoke = {
            'id': datetime.now().strftime("%Y%m%d%H%M%S%f"),
            'content': joke
        }
        l1 = [myjoke]
        with open(file, 'w') as f:
            json.dump(l1, f, indent=2)
    return "success"
def list_fav():
    file = "data/favjokes.json"
    with open(file, 'r') as f:
        y = json.load(f)
    return y
def delete_fav(id):
    id = str(id)
    file = "data/favjokes.json"
    with open(file,'r') as f:
        y = json.load(f)
    for index, item in enumerate(y):
        if item['id'] == id:
            y.pop(index)
            break
    with open(file, 'w') as f:
        json.dump(y,f,indent=2)
    return "success"
