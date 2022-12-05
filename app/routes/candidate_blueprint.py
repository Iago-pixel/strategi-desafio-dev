from flask import Blueprint
from app.controllers.candidate_controller import add_candidate, get_candidate, get_all_candidates, del_candidate

bp_candidate = Blueprint("bp_candidate", __name__, url_prefix="/candidate")

bp_candidate.post("/<int:candidate_id>")(add_candidate)
bp_candidate.get("/<int:candidate_id>")(get_candidate)
bp_candidate.get("")(get_all_candidates)
bp_candidate.delete("<int:candidate_id>")(del_candidate)