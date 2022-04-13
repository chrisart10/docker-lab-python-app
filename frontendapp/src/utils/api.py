import requests
import json

def mypost(id:int,mensaje:str):
    network = 'backend:80'
    url = 'http://{}/items/{}?mensaje={}'.format(network,id,mensaje)
    response = requests.get(url)
    response = json.loads(response.content)

    return response