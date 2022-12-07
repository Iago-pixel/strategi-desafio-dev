from app.configs.database import db
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import validates
from dataclasses import dataclass
from app.models.candidate_model import CandidateModel
from app.exc.DataError import DataError

@dataclass
class TeamModel(db.Model):
    id: int
    name: str
    heros: list[CandidateModel]

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)

    name = Column(String(50), nullable=False)
    
    heros = db.relationship("CandidateModel", backref="team", uselist=True)

    @validates("name")
    def validate_name(self, key, name):
        if type(name) != str or len(name) == 0:
            raise DataError("Name should be `string` and not empty")

        return name