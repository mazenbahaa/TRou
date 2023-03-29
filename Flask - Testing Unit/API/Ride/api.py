from flask import Flask, request
from flask_restful import Api, Resource
from model import db, Rides

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class RideRegistration(Resource):
    def get(self):
        RideRegistration = Rides.query.all()
        return {'Rides': list(x.json() for x in RideRegistration)}

    def post(self):
        data = request.get_json()
        new_RideRegistration = Rides(data['UserId'], data['RideName'], data['RideCode'], data['AssembleDestination'])

        db.session.add(new_RideRegistration)
        db.session.commit()

        return new_RideRegistration.json(), 201


class RideProfile(Resource):
    def get(self, id):
        RideProfile = Rides.query.filter_by(id=id).first()
        if RideProfile:
            return RideProfile.json()
        return {'message': 'Ride not Found'}, 404

    def put(self, id):
        data = request.get_json()
        RideProfile = Rides.query.filter_by(id=id).first()

        if RideProfile:
            RideProfile.UserId = data['UserId']
            RideProfile.RideName = data['RideName']
            RideProfile.RideCode = data['RideCode']
            RideProfile.AssembleDestination = data['AssembleDestination']
        else:
            RideProfile = Rides(id=id, **data)

        db.session.add(RideProfile)
        db.session.commit()
        return RideProfile.json()

    def delete(self, id):
        RideProfile = Rides.query.filter_by(id=id).first()

        if RideProfile:
            db.session.delete(RideProfile)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'Ride not Found'}, 404


api.add_resource(RideRegistration, '/rideregistration')
api.add_resource(RideProfile, '/rideregistration/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)