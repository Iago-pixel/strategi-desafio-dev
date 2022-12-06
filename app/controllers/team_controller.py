from flask import request, current_app, jsonify
from app.models.team_model import TeamModel

def add_team():
    session = current_app.db.session

    data = request.get_json()

    team = TeamModel(**data)

    session.add(team)
    session.commit()

    return jsonify(team), 201