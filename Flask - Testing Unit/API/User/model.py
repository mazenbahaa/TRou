from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    UserName = db.Column(db.String(40))
    Email = db.Column(db.String(100))
    Location = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    Password = db.Column(db.String(20))

    def __init__(self, UserName, Email, Location, Address, Password):
        self.UserName = UserName
        self.Email = Email
        self.Location = Location
        self.Address = Address
        self.Password = Password

    def __repr__(self):
        return f"{self.UserName}:{self.Email}:{self.Location}:{self.Address}:{self.Password}"

    def json(self):
        return {"UserName": self.UserName, "Email": self.Email, "Location": self.Location, "Address": self.Address, "Password": self.Password}
