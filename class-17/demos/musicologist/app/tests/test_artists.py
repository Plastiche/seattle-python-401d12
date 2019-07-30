import json


def test_get_no_artists(client):
    res = client.get("/artists")
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []


def test_sample_artist_fixture(sample_artist):
    assert sample_artist.id == 1
    assert sample_artist.name == "Iggy Pop"


def test_solo_artist_fixture(solo_artist):
    assert solo_artist.id == 1
    assert solo_artist.name == "Etta James"


def test_create_artist_with_band(client, sample_band):

    artist_info = {"name": "Iggy Pop", "band": sample_band.id}

    res = client.post("/artists", data=artist_info)

    assert res.status_code == 200


def test_create_solo_artist(client):

    artist_info = {"name": "Etta James"}

    res = client.post("/artists", data=artist_info)

    assert res.status_code == 200

    res = client.get("/artists")

    artists = json.loads(res.data.decode())

    assert len(artists) == 1

    assert artists[0]['name'] == "Etta James"

    assert artists[0].get('band') is None


def test_get_one_artist(client, sample_artist):

    res = client.get(f"/artists/{sample_artist.id}")

    artist_dict = json.loads(res.data.decode())

    assert artist_dict["name"] == "Iggy Pop"
