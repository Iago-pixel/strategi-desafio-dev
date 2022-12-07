from flask import request, current_app, jsonify
from app.models.team_model import TeamModel
from app.models.candidate_model import CandidateModel
from app.exc.DataError import DataError
from sqlalchemy.exc import IntegrityError

def add_team():
    session = current_app.db.session

    data = request.get_json()

    try:
        team = TeamModel(**{"name": data["name"]})

        session.add(team)
        session.commit()

        return jsonify(team), 201
    
    except DataError:
        return jsonify({"error": "Name should be `string` and not empty"}), 400

    except KeyError:
        return jsonify({"error": "key `name` not found"}), 400

def get_team(team_id):
    team = (
        TeamModel.query.get_or_404(team_id)
    )

    return jsonify(team), 200

def get_all_team():
    teams = (
        TeamModel.query.all()
    )

    serializer = [
        {
            "id": team.id,
            "name": team.name,
            "teams": team.heros
        } for team in teams
    ]

    return {"teams": serializer}, 200

def rename_team(team_id):

    try:
        session = current_app.db.session

        data = request.get_json()

        team = TeamModel.query.get_or_404(team_id)

        setattr(team, "name", data["name"])

        session.add(team)
        session.commit()

        return "", 204
    
    except DataError:
        return jsonify({"error": "Name should be `string` and not empty"}), 400

    except KeyError:
        return jsonify({"error": "key `name` not found"}), 400

def enter_in_team(team_id, candidate_id):
    session = current_app.db.session

    data = request.get_json()

    hero = CandidateModel.query.get(candidate_id)
    
    if hero is None:
        return jsonify({"error": "candidate id's is not found"}), 404

    try:
        setattr(hero, "team_id", team_id)

        session.add(hero)
        session.commit()

        return "", 204

    except IntegrityError:
        return jsonify({"error": "team id's is not found"}), 404

def del_team(team_id):
    session = current_app.db.session

    query = TeamModel.query.get_or_404(team_id)

    session.delete(query)
    session.commit()

    return "", 204