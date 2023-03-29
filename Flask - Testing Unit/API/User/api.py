from flask import Flask, request
from flask_restful import Api, Resource
from model import Users, db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class UserRegistration(Resource):
    def get(self):
        UserRegistration = Users.query.all()
        return {'Users': list(x.json() for x in UserRegistration)}

    def post(self):
        data=request.get_json()
        new_UserRegistration = Users(data['UserName'], data['Email'], data['Location'], data['Address'], data['Password'])

        db.session.add(new_UserRegistration)
        db.session.commit()

        return new_UserRegistration.json(), 201


class UserProfile(Resource):
    def get(self, id):
        UserProfile = Users.query.filter_by(id=id).first()
        if UserProfile:
            return UserProfile.json()
        return {'message': 'User not Found'}, 404

    def put(self, id):
        data= request.get_json()
        UserProfile = Users.query.filter_by(id=id).first()

        if UserProfile:
            UserProfile.UserName = data['UserName']
            UserProfile.Email = data['Email']
            UserProfile.Location = data['Location']
            UserProfile.Address = data['Address']
            UserProfile.Password = data['Password']
        else:
            UserProfile = Users(id=id, **data)

        db.session.add(UserProfile)
        db.session.commit()

        return UserProfile.json()

    def delete(self, id):
        UserProfile = Users.query.filter_by(id=id).first()

        if UserProfile:
            db.session.delete(UserProfile)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'User not Found'}, 404 


api.add_resource(UserRegistration, '/userregistration')
api.add_resource(UserProfile, '/userregistration/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)