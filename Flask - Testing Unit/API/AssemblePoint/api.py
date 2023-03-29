from flask import Flask, request
from flask_restful import Api, Resource
from model import db, AssemblePoints

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class AddAssemblePoint(Resource):
    def get(self):
        AddAssemblePoint = AssemblePoints.query.all()
        return {'AssemblePoints': list(x.json() for x in AddAssemblePoint)}

    def post(self):
        data = request.get_json()
        new_AssemblePoint = AssemblePoints(data['R_Name'], data['R_Code'], data['R_Location'], data['Time'], data['AssemblePoints'])

        db.session.add(new_AssemblePoint)
        db.session.commit()
        return new_AssemblePoint.json(), 201


class EditAssemblePoint(Resource):
    def get(self, id):
        AssemblePoint = AssemblePoints.query.filter_by(id=id).first()

        if AssemblePoint:
            return AssemblePoint.json()
        return {'message': 'AssemblePoint not Found'}, 404

    def put(self, id):
        data = request.get_json()
        AssemblePoint = AssemblePoints.query.filter_by(id=id).first()

        if AssemblePoint:
            AssemblePoint.R_Name = data['R_Name']
            AssemblePoint.R_Code = data['R_Code']
            AssemblePoint.R_Location = data['R_Location']
            AssemblePoint.Time = data['Time']
            AssemblePoint.AssemblePoints = data['AssemblePoints']
        else:
            AssemblePoint = AssemblePoints(id=id, **data)
        
        db.session.add(AssemblePoint)
        db.session.commit()
        return AssemblePoint.json()
    
    def delete(self, id):
        AssemblePoint = AssemblePoints.query.filter_by(id=id).first()

        if AssemblePoint:
            db.session.delete(AssemblePoint)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'AssemblePoint not Found'}


api.add_resource(AddAssemblePoint, '/assemblePoint')
api.add_resource(EditAssemblePoint, '/assemblePoint/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)