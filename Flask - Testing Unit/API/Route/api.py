from flask import Flask, request
from flask_restful import Api, Resource
from model import db, Routes

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class RouteRegistration(Resource):
    def get(self):
        RouteRegistration = Routes.query.all()
        return {'Route': list(x.json() for x in RouteRegistration)}

    def post(self):
        data = request.get_json()
        new_RouteRegistration = Routes(data['RouteName'], data['RouteCode'], data['StartPoint'], data['EndPoint'], data['DriverLicence'], data['VehicleLicence'], data['AssemblePoint'])

        db.session.add(new_RouteRegistration)
        db.session.commit()

        return new_RouteRegistration.json(), 201


class RouteProfile(Resource):
    def get(self, id):
        RouteProfile = Routes.query.filter_by(id=id).first()
        if RouteProfile:
            return RouteProfile.json()
        return {'message': 'Route not Found'}, 404

    def put(self, id):
        data = request.get_json()
        RouteProfile = Routes.query.filter_by(id=id).first()

        if RouteProfile:
            RouteProfile.RouteName = data['RouteName']
            RouteProfile.RouteCode = data['RouteCode']
            RouteProfile.StartPoint = data['StartPoint']
            RouteProfile.EndPoint = data['EndPoint']
            RouteProfile.DriverLicence = data['DriverLicence']
            RouteProfile.VehicleLicence = data['VehicleLicence']
            RouteProfile.AssemblePoint = data['AssemblePoint']
        else:
            RouteProfile = Routes(id=id, **data)

        db.session.add(RouteProfile)
        db.session.commit()

        return RouteProfile.json()

    def delete(self, id):
       RouteProfile = Routes.query.filter_by(id=id).first()

       if RouteProfile:
           db.session.delete(RouteProfile)
           db.session.commit()
           return {'message': 'Deleted'}
       else:
            return {'message': 'Route not Found'}, 404 

api.add_resource(RouteRegistration, '/routeregistration')
api.add_resource(RouteProfile, '/routeregistration/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)