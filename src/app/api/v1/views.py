from app.api.v1 import route
from flask import jsonify


@route.route('/', methods=['GET'])
def approve_comment():
    return jsonify({'status': 'ok'})
