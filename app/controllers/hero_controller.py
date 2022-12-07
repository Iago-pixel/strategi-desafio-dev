from flask import request, current_app, jsonify
import requests

def get_hero(hero_id):
    url = f'https://gateway.marvel.com/v1/public/characters/{hero_id}?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

    response = requests.get(url).json()

    try:
        result = response["data"]["results"][0]

        image = f'{result["thumbnail"]["path"]}/portrait_small.{result["thumbnail"]["extension"]}'

        data = {
            'id': result["id"], 
            "name": result["name"], 
            "description": result["description"],
            "image": image
        }

        return jsonify(data), 200
    
    except KeyError:
        return jsonify({"error": "Id not found"}), 404

def get_all_heros():
    url = 'https://gateway.marvel.com/v1/public/characters?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

    data = response = requests.get(url).json()

    heros = response["data"]["results"]

    serializer = [
        {
            "id": hero["id"],
            "name": hero["name"],
            "description": hero["description"],
            "image": f'{hero["thumbnail"]["path"]}/portrait_small.{hero["thumbnail"]["extension"]}'
        } for hero in heros
    ]

    return {"heros": serializer}, 200