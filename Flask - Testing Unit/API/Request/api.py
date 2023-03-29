from flask import Flask, request
from flask_restful import Api, Resource
from model import db, Requests

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class SendRequest(Resource):
    def get(self):
        SendRequest = request.query.all()
        return {'Request': list(x.json() for x in SendRequest)}

    def post(self):
        data = request.get_json()
        new_SendRequest = Requests(data['R_Names'], data['R_Codes'], data['AssembleDestination_Current'], data['AssembleDestination_Request'])

        db.session.add(new_SendRequest)
        db.session.commit()
        return new_SendRequest.json(), 201


class EditRequest(Resource):
    def get(self, id):
        EditRequest = Requests.query.filter_by(id=id).first()
        if EditRequest:
            return EditRequest.json()
        return {'message': 'Request not Found'}, 404

    def put(self, id):
        data = request.get_json()
        EditRequest = Requests.query.filter_by(id=id).first()

        if EditRequest:
            EditRequest.R_Names = data['R_Names']
            EditRequest.R_Codes = data['R_Codes']
            EditRequest.AssembleDestination_Current = data['AssembleDestination_Current']
            EditRequest.AssembleDestination_Request = data['AssembleDestination_Request']
        else:
            EditRequest = Requests(id=id, **data)
        
        db.session.add(EditRequest)
        db.session.commit()

        return EditRequest.json()

    def delete(self, id):
        EditRequest = Requests.query.filter_by(id=id).first()

        if EditRequest:
            db.session.delete(EditRequest)
            db.session.commit()
            return {'message': 'Request not Found'}, 404

api.add_resource(SendRequest, '/request')
api.add_resource(EditRequest, '/request/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)