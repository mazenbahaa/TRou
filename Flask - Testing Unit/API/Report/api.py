from flask import Flask, request
from flask_restful import Api, Resource
from model import db, Reports

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Mezo2022@localhost:5432/finaldistination"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class SendReport(Resource):
    def get(self):
        SendReport = Reports.query.all()
        return {'Report': list(x.json() for x in SendReport)}

    def post(self):
        data = request.get_json()
        new_SendReport = Reports(data['Message'])

        db.session.add(new_SendReport)
        db.session.commit()

        return new_SendReport.json(), 201


class EditReport(Resource):
    def get(self, id):
        EditReport = Reports.query.filter_by(id=id).first()
        if EditReport:
            return EditReport.json()
        return {'message':'Report not Found'}, 404

    def put(self, id):
        data = request.get_json()
        EditReport = Reports.query.filter_by(id=id).first()

        if EditReport:
            EditReport.Message = data['Message']
        else:
            EditReport = Reports(id=id, **data)
        
        db.session.add(EditReport)
        db.session.commit()

        return EditReport.json()

    def delete(self, id):
        EditReport = Reports.query.filter_by(id=id).first()

        if EditReport:
            db.session.delete(EditReport)
            db.session.commit()
            return {'message': 'Report not Found'}, 404


api.add_resource(SendReport, '/report')
api.add_resource(EditReport, '/report/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)