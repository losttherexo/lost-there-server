from flask import jsonify, make_response
from flask_restful import Resource

from config import api, app

class Home(Resource):

    def get(self):
        return 'mahalo'

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5555, debug=True)