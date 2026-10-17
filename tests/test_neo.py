"""  NeoWs: Near Earth Object Web Service  """


def test_neo_feed_returns_successful_response(neo_data):
    """NeoWs returns a valid JSON object."""
    assert isinstance(neo_data, dict)


def test_neo_feed_contains_required_fields(neo_data):
    """NeoWs response contains the required top-level fields."""
    assert "near_earth_objects" in neo_data
    assert "element_count" in neo_data

    assert isinstance(neo_data["near_earth_objects"], dict)
    assert isinstance(neo_data["element_count"], int)


def test_neo_feed_contains_asteroid_data(neo_data):
    """Asteroid records contain the expected fields and types."""
    asteroids_by_date = neo_data["near_earth_objects"]

    assert asteroids_by_date, "No asteroid dates found in the response"

    asteroids = next(iter(asteroids_by_date.values()))

    assert isinstance(asteroids, list)
    assert asteroids, "No asteroid records found for the selected date"

    asteroid = asteroids[0]

    assert "id" in asteroid
    assert "name" in asteroid
    assert "is_potentially_hazardous_asteroid" in asteroid

    assert isinstance(asteroid["id"], str)
    assert isinstance(asteroid["name"], str)
    assert isinstance(
        asteroid["is_potentially_hazardous_asteroid"],
        bool,
    )
