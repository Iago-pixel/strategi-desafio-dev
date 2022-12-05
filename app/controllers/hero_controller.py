from flask import request, current_app, jsonify
import requests

def get_hero(hero_id):
    url = f'https://gateway.marvel.com/v1/public/characters/{hero_id}?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

    response = requests.get(url).json()

    data = {
        'id': response["data"]["results"][0]["id"], 
        "name": response["data"]["results"][0]["name"], 
        "description": response["data"]["results"][0]["description"]
    }

    return jsonify(data), 200

def get_all_heros():
    url = 'https://gateway.marvel.com/v1/public/characters?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

    data = response = requests.get(url).json()

    heros = response["data"]["results"]

    serializer = [
        {
            "id": hero["id"],
            "name": hero["name"],
            "description": hero["description"]
        } for hero in heros
    ]

    return {"heros": serializer}, 200