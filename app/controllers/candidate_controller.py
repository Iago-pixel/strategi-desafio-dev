from flask import request, current_app, jsonify
from app.models.candidate_model import CandidateModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
import requests

def add_candidate(candidate_id):
    session = current_app.db.session

    url = f'https://gateway.marvel.com/v1/public/characters/{candidate_id}?apikey=59e51aa09b849f53fc6976dbdd4b1c05&hash=034d42ce78896ef4540fb52918a450c3&ts=1'

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

        hero = CandidateModel(**data)

        session.add(hero)
        session.commit()

        return jsonify(hero), 201
    
    except KeyError:
        return jsonify({"error": "Id not found"}), 404

    except IntegrityError:
        return jsonify({"error": "Id already exist"}), 409

def get_candidate(candidate_id):
    hero = (
        CandidateModel.query.get_or_404(candidate_id)
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
            "description": hero.description,
            "image": hero.image,
            "team_id": hero.team_id
        } for hero in heros
    ]

    return {"candidates": serializer}, 200

def remove_team(candidate_id):
    session = current_app.db.session

    hero = CandidateModel.query.get_or_404(candidate_id)

    setattr(hero, "team_id", None)

    session.add(hero)
    session.commit()

    return "", 204

def del_candidate(candidate_id):
    session = current_app.db.session

    query = CandidateModel.query.get_or_404(candidate_id)

    session.delete(query)
    session.commit()

    return "", 204