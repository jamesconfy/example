from example import db
import json
from werkzeug.exceptions import HTTPException
from flask import current_app as app, jsonify, request, abort
from example.models import Users, UserSchema

userOne = UserSchema()
userMany = UserSchema(many=True)

@app.route('/')
def home():
    return 'Trying'

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        users = Users.query.all()
        return jsonify(userMany.dump(users)), 200

    if request.method == 'POST':
        if request.is_json:
            id = request.json.get('id')
            name = request.json.get('name')
            user = Users(name=name)

            db.session.add(user)
            db.session.commit()

            response = {
                "code": 200,
                "description": 'OK'
            }

            return jsonify(response), 200

        else:
            abort(400, description='Content-Type must be application/json')


@app.route('/users/<user_id>')
def user(user_id):
    user = Users.query.get_or_404(user_id)
    return jsonify(userOne.dump(user)), 200


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "message": e.description
    })
    response.content_type = "application/json"
    return response