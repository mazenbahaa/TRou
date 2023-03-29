from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Requests(db.Model):
    __tableName__ = 'Requests'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    R_Names = db.Column(db.String)
    R_Codes = db.Column(db.String)
    AssembleDestination_Current = db.Column(db.String(length=100))
    AssembleDestination_Request = db.Column(db.String(length=100))

    def __init__(self, R_Names, R_Codes, AssembleDestination_Current, AssembleDestination_Request):
        self.R_Names = R_Names
        self.R_Codes = R_Codes
        self.AssembleDestination_Current = AssembleDestination_Current
        self.AssembleDestination_Request = AssembleDestination_Request

    def __repr__(self):
        return f"{self.R_Names}:{self.R_Codes}:{self.AssembleDestination_Current}:{self.AssembleDestination_Request}"

    def json(self):
        return {"R_Names": self.R_Names, "R_Code": self.R_Codes, "AssembleDestination_Current": self.AssembleDestination_Current, "AssembleDestination_Request": self.AssembleDestination_Request}