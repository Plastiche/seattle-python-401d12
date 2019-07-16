from models.location import Location
import json


def test_location():
    with open('tests/mock-location.json') as f:
        mock_location = json.loads(f.read())

    location = Location('barcelona', mock_location['results'][0])
    assert location.search_query == 'barcelona'
    assert location.formatted_query == 'Barcelona, Spain'
    assert location.latitude == 41.3850639
    assert location.longitude == 2.1734035
