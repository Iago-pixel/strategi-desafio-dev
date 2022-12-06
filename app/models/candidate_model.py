from app.configs.database import db
from sqlalchemy import Integer, String, Column, ForeignKey
from dataclasses import dataclass

@dataclass
class CandidateModel(db.Model):
    id: int
    name: str
    description: str
    image: str

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)

    name = Column(String(50), nullable=False)
    description = Column(String(), nullable=False)
    image = Column(String(), nullable=False)

    team_id = db.Column(Integer, ForeignKey('teams.id'))