from flask import Blueprint
from app.controllers.team_controller import add_team, get_team, get_all_team, rename_team, enter_in_team, del_team

bp_team = Blueprint("bp_team", __name__, url_prefix="/team")

bp_team.post("")(add_team)
bp_team.get("/<int:team_id>")(get_team)
bp_team.get("")(get_all_team)
bp_team.patch("/<int:team_id>")(rename_team)
bp_team.patch("/<int:team_id>/<int:candidate_id>")(enter_in_team)
bp_team.delete("/<int:team_id>")(del_team)