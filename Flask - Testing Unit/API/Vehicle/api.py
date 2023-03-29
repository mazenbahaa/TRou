from flask import Flask, request
from flask_restful import Api, Resource
from model import db, Vehicles

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class VehicleRegistration(Resource):
    def get(self):
        VehicleRegistration = Vehicles.query.all()
        return {'Vehicle': list(x.json() for x in VehicleRegistration)}

    def post(self):
        data = request.get_json()
        new_VehicleRegistration = Vehicles(data['VehicleModel'], data['VehicleCapacity'], data['Licence'], data['EndLicence'])

        db.session.add(new_VehicleRegistration)
        db.session.commit()

        return new_VehicleRegistration.json(), 201


class VehicleProfile(Resource):
    def get(self, id):
        VehicleProfile = Vehicles.query.filter_by(id=id).first()
        if VehicleProfile:
            return VehicleProfile.json()
        return {'message': 'Vehicle not Found'}, 404
    
    def post(self, id):
        data = request.get_json()
        VehicleProfile = Vehicles.query.filter_by(id=id).first()

        if VehicleProfile:
            VehicleProfile.VehicleModel = data['VehicleModel']
            VehicleProfile.VehilceCapacity = data['VehicleCapacity']
            VehicleProfile.Licence = data['Licence']
            VehicleProfile.EndLicence = data['EndLicence']
        else:
            VehicleProfile = Vehicles(id=id, **data)
        
        db.session.add(VehicleProfile)
        db.sessoin.commit()
        return VehicleProfile.json()

    def delete(self, id):
        VehicleProfile = Vehicles.query.filter_by(id=id).first()

        if VehicleProfile:
            db.session.delete(VehicleProfile)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'Vehilce not Found'}, 404

api.add_resource(VehicleRegistration, '/vehicle')
api.add_resource(VehicleProfile, '/vehicle/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)