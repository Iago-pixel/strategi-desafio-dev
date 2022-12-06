from flask import Flask
from app.routes.candidate_blueprint import bp_candidate
from app.routes.hero_blueprint import bp_hero
from app.routes.team_blueprint import bp_team

def init_app(app: Flask):
    app.register_blueprint(bp_candidate)
    app.register_blueprint(bp_hero)
    app.register_blueprint(bp_team)