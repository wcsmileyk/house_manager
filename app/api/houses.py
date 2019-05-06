from flask import jsonify

from . import api


@api.route('/houses/')
def get_houses():
    return jsonify({'HouseName': 'Bostic'})