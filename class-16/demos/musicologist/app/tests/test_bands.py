import json


def test_get_no_bands(client):

    res = client.get("/bands")

    assert res.status_code == 200

    assert json.loads(res.data.decode()) == []


def test_create_band(client):

    res = client.post("/bands", data={"name": "The Stooges"})

    assert res.status_code == 200


def test_sample_band(sample_band):

    assert sample_band.id == 1

    assert sample_band.name == "The Stooges"


def test_create_band_and_fetch(client, sample_band):

    res = client.get(f"/bands/{sample_band.id}")

    assert res.status_code == 200

    band_dict = json.loads(res.data.decode())

    assert band_dict["name"] == "The Stooges"

