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

        @app.route("/bands/<int:id>", methods=["GET"])
        def one_band(id):
            band = Band.query.get(id)
            return jsonify(band.to_dict())

        @app.route("/bands/<string:name>", methods=["GET"])
        def one_band_by_name(name):
            band = Band.query.filter_by(name=name).first()
            return jsonify(band.to_dict())

        @app.route("/bands", methods=["POST"])
        def create_band():
            band_info = request.json or request.form
            band = Band(name=band_info.get("name"))
            db.session.add(band)
            db.session.commit()

            return jsonify(band.to_dict())

        @app.route("/bands/<int:id>", methods=["PUT"])
        def update_band(id):
            band_info = request.json or request.form

            # HIDDEN ASSUMPTION
            band_id = Band.query.filter_by(id=id).update(band_info)

            db.session.commit()
            return jsonify(band_id)

        @app.route("/bands/<int:id>", methods=["DELETE"])
        def delete_band(id):
            band = Band.query.get(id)
            db.session.delete(band)
            db.session.commit()
            return jsonify(id)




        


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
            artist = Artist(
                name=artist_info.get("name"), band_id=artist_info.get("band")
            )
            db.session.add(artist)
            db.session.commit()

            return jsonify(artist.to_dict())

        return app


from app.models import Band, Artist
