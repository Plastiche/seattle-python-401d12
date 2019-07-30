from app import db
from app.models import Band, Artist


def test_band(client):
    band = Band(name="The Band")
    db.session.add(band)
    db.session.commit()
    assert Band.query.first().name == "The Band"


def test_artist(client):
    artist = Artist(name="Otis Redding")
    db.session.add(artist)
    db.session.commit()
    assert Artist.query.first().name == "Otis Redding"


def test_artist_in_band(client):
    band = Band(name="The Skatalites")
    artist = Artist(name="Roland Alphonso", band=band)
    db.session.add(artist)
    db.session.commit()
    assert Band.query.first().name == "The Skatalites"
    assert Artist.query.first().name == "Roland Alphonso"
    # hmmm, adding artist with associated band does not require
    # the band to be added to session
    artists_in_band = Band.query.first().artists
    assert artists_in_band[0].name == "Roland Alphonso"
    assert artists_in_band[0].band.name == "The Skatalites"


