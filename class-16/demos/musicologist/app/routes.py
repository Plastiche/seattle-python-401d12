from flask import jsonify, request, current_app
from app import db

@current_app.route('/bands', methods=['GET'])
def all_bands():
    bands = [band.to_dict() for band in Band.query.all()]
    return jsonify(bands)

@current_app.route('/bands/<int:id>')
def one_band(id):
    band = Band.query.get(id)
    return jsonify(band.to_dict())

@current_app.route('/bands', methods=['POST'])
def create_band():
    return 'yo'
    # info = request.form()
    # band = Band(name=info.get('name'))
    # db.session.add(band)
    # db.session.commit()

    # return jsonify(band)

from app.models import Band
