from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/ping')
def ping():
    return 'pong'

@app.route('/testsnack')
def testsnack():
    twix = Snack(name='twix', rank=23)
    db.session.add(twix)
    db.session.commit()

    return twix.name

@app.route('/api/v1/snacks')
def all_snacks():
    snacks = [snack.to_dict() for snack in Snack.query.all()]

    return jsonify(snacks)

@app.route('/api/v1/snacks/<string:name>')
def get_snack_by_name(name):
    snack = Snack.query.filter_by(name=name).first()
    return jsonify(snack.to_dict())

from app.models import Snack