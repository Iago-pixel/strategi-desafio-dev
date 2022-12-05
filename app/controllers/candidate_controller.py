from flask import request, current_app, jsonify
from app.models.candidate_model import CandidateModel
import requests

def add_candidate(candidate_id):
    url = f'https://gateway.marvel.com/v1/public/characters/{candidate_id}?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

    response = requests.get(url).json()

    data = {
        'id': response["data"]["results"][0]["id"], 
        "name": response["data"]["results"][0]["name"], 
        "description": response["data"]["results"][0]["description"]
    }

    hero = CandidateModel(**data)

    current_app.db.session.add(hero)
    current_app.db.session.commit()

    return jsonify(hero), 201

def get_candidate(candidate_id):
    hero = (
        CandidateModel.query.get(candidate_id)
    )

    return jsonify(hero), 200

def get_all_candidates():
    heros = (
        CandidateModel.query.all()
    )

    serializer = [
        {
            "id": hero.id,
            "name": hero.name,
            "description": hero.description
        } for hero in heros
    ]

    return {"candidates": serializer}, 200

def del_candidate(candidate_id):
    query = CandidateModel.query.get(candidate_id)

    current_app.db.session.delete(query)
    current_app.db.session.commit()

    return "", 204