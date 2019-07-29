import pytest
from app import create_app, db
from config import Config
from app.models import Band, Artist


class TestConfig(Config):
    # in memory database for testing
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture
def client():

    app = create_app(TestConfig)

    app_context = app.app_context()

    app_context.push()

    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()

    db.drop_all()

    app_context.pop()


@pytest.fixture
def sample_band(client):
    band = Band(name="The Stooges")
    db.session.add(band)
    db.session.commit()
    return band


@pytest.fixture
def sample_artist(sample_band):
    artist = Artist(name="Iggy Pop", band=sample_band)
    db.session.add(artist)
    db.session.commit()
    return artist


@pytest.fixture
def solo_artist(client):
    artist = Artist(name="Etta James")
    db.session.add(artist)
    db.session.commit()
    return artist
