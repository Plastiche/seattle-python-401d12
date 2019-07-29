from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(ConfigClass):

    app = Flask(__name__)

    app.config.from_object(ConfigClass)

    db.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():

        #######################################
        ##   Band CRUD    #####################
        #######################################

        @app.route("/bands", methods=["GET"])
        def all_bands():
            bands = [band.to_dict() for band in Band.query.all()]
            return jsonify(bands)

        @app.route("/bands/<int:id>")
        def one_band(id):
            band = Band.query.get(id)
            return jsonify(band.to_dict())

        @app.route("/bands", methods=["POST"])
        def create_band():
            band_info = request.json or request.form
            band = Band(name=band_info.get("name"))
            db.session.add(band)
            db.session.commit()

            return jsonify(band.to_dict())

        @app.route("/bands/<int:id>", methods=["DELETE"])
        def delete_band(id):
            pass

        @app.route("/bands/<int:id>", methods=["PUT"])
        def update_band(id):
            pass

        #######################################
        ##   Artist CRUD  #####################
        #######################################
        @app.route("/artists", methods=["GET"])
        def all_artists():
            artists = [artist.to_dict() for artist in Artist.query.all()]
            return jsonify(artists)

        @app.route("/artists/<int:id>")
        def one_artist(id):
            artist = Artist.query.get(id)
            return jsonify(artist.to_dict())

        @app.route("/artists", methods=["POST"])
        def create_artist():
            artist_info = request.json or request.form
            artist = Artist(name=artist_info.get("name"), band_id=artist_info.get("band"))
            db.session.add(artist)
            db.session.commit()

            return jsonify(artist.to_dict())

        @app.route("/artists/<int:id>", methods=["DELETE"])
        def delete_artist(id):
            pass

        @app.route("/artists/<int:id>", methods=["PUT"])
        def update_artist(id):
            pass

        @app.route("/bands/<int:id>/artists")
        def get_artists_in_band(id):
            artists = [artist.to_dict() for artist in Band.query.get(id).artists]
            return jsonify(artists)

        return app


from app.models import Band, Artist
