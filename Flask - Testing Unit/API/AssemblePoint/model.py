from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AssemblePoints(db.Model):
    __tableName__ = 'AssemblePoints'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    R_Name = db.Column(db.String)
    R_Code = db.Column(db.String)
    R_Location = db.Column(db.String(length=10))
    Time = db.Column(db.String)
    AssemblePoints = db.Column(db.String)

    def __init__ (self, R_Name, R_Code, R_Location, Time, AssemblePoints):
        self.R_Name = R_Name
        self.R_Code = R_Code
        self.R_Location = R_Location
        self.Time = Time
        self.AssemblePoints = AssemblePoints

    def __repr__(self):
        return f"{self.R_Name}:{self.R_Code}:{self.R_Location}:{self.Time}:{self.AssemblePoints}"
    
    def json(self):
        return {"R_Name": self.R_Name, "R_Code": self.R_Code, "R_Location": self.R_Location, "Time": self.Time, "AssemblePoints": self.AssemblePoints}