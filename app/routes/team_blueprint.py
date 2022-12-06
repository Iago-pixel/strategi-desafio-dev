from flask import Blueprint
from app.controllers.team_controller import add_team

bp_team = Blueprint("bp_team", __name__, url_prefix="/team")

bp_team.post("")(add_team)