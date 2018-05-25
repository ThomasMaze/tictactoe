from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class GridApi(Resource):
    def post(self):
        return 200

    def get(self):
        return {'status': 'success'}

api.add_resource(GridApi, '/fill_cell')

if __name__ == '__main__':
    app.run(port='5000', debug=True)
