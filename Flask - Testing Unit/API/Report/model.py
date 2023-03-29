from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reports(db.Model):
    __tableName__ = 'Reports'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    U_Id = db.Column(db.Integer)
    Message = db.Column(db.String(length=500))

    def __init(self, Message):
        self.Message = Message

    def __repr__(self):
        return f'{self.Message}'
    
    def json(self):
        return {"Message": self.Message}