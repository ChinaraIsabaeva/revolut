from flask import Flask, request
from flask_restful import Resource, Api, abort

from util import create_final_dict


app = Flask(__name__)
api = Api(app)


class Nested(Resource):
    def post(self):
        if not request.args.get('keys'):
            abort(400, message="Missing keys to create dict")
        else:
            keys = request.args.get('keys', '').split(',')
            output = create_final_dict(request.json, keys)
            return output


api.add_resource(Nested, '/')


if __name__ == '__main__':
    app.run(debug=True)
