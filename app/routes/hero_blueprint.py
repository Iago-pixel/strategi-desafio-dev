from flask import Blueprint
from app.controllers.hero_controller import get_all_heros, get_hero

bp_hero = Blueprint("bp_hero", __name__, url_prefix="/hero")

bp_hero.get("/<int:hero_id>")(get_hero)
bp_hero.get("")(get_all_heros)