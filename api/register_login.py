from flask import jsonify
from flask_restful import Resource, reqparse, abort
from app import app

parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)


class RegisterRes(Resource):
    def post(self):
        args = parser.parse_args()
        created_user = app.user_repo_request_create(args['username'], args['password'])
        if created_user is None:
            abort(400, message='diplicated username')
        return jsonify(created_user)  # дописать


class LoginRes(Resource):
    def post(self):
        args = parser.parse_args()
        user, error = app.user_repo_autorize(args['username'], args['password'])
        if user is None:
            abort(400, message=error)
        return jsonify(user)  # доделать (возвращают ответный токен)
