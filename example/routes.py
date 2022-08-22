import json
import pandas as pd
from werkzeug.exceptions import HTTPException
from flask import current_app as app, jsonify, redirect, request, abort, url_for
from example.models import Users, UserSchema
from example import db

userOne = UserSchema()
userMany = UserSchema(many=True)

@app.route('/')
def home():
    return jsonify('ty')

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        users = Users.query.all()
        return jsonify(userMany.dump(users)), 200

    if request.method == 'POST':
        if request.is_json:
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

@app.route('/load')
def load():
    users = Users.query.all()
    if not users:
        df = pd.read_csv('./data.csv')
        for val in df['name']:
            user = Users(name=str(val))
            db.session.add(user)
            db.session.commit()

        new_users = Users.query.all()
        return jsonify(userMany.dump(new_users)), 200

    return redirect(url_for('home'))

@app.errorhandler(HTTPException)
def handle_exception(err):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = err.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": err.code,
        "name": err.name,
        "message": err.description
    })
    response.content_type = "application/json"
    return response