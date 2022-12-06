from app.configs.database import db
from sqlalchemy import Integer, String, Column
from dataclasses import dataclass
from app.models.candidate_model import CandidateModel

@dataclass
class TeamModel(db.Model):
    id: int
    name: str
    heros: list[CandidateModel]

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)

    name = Column(String(50), nullable=False)
    
    heros = db.relationship("CandidateModel", backref="team", uselist=True)