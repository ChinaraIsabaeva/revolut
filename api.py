from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api, abort

from logging import FileHandler, DEBUG

from util import create_final_dict, validate_keys_name


app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)


file_handler = FileHandler('error.log')
file_handler.setLevel(DEBUG)

app.logger.addHandler(file_handler)

users = {
    "admin": "admin",
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    return "Server started"


class Nested(Resource):
    @auth.login_required
    def post(self):
        if not request.args.get('keys'):
            abort(400, message="Missing keys to create dict")
        else:
            keys = request.args.get('keys', '').split(',')
            data = request.json
            validate_keys_name(keys, data[0])
            output = create_final_dict(data, keys)
            return output


api.add_resource(Nested, '/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
