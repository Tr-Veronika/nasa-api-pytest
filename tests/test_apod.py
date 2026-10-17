"""  APOD: Astronomy Picture of the Day  """

def test_apod_returns_successful_response(apod_data):
    """APOD endpoint returns a non-empty JSON response."""
    assert apod_data is not None


def test_apod_contains_required_fields(apod_data):
    """APOD response contains required publication fields."""
    assert isinstance(apod_data, list), (
        f"Expected a list, got {type(apod_data).__name__}"
    )
    assert apod_data, "APOD response is empty"

    required_fields = {
        "date",
        "title",
        "media_type",
        "explanation",
        "url",
    }

    assert required_fields.issubset(apod_data[0].keys())


def test_apod_fields_have_correct_types(apod_data):
    """APOD publication fields have the expected types."""
    assert isinstance(apod_data, list)
    assert apod_data, "APOD response is empty"

    apod = apod_data[0]

    assert isinstance(apod["date"], str)
    assert isinstance(apod["title"], str)
    assert isinstance(apod["media_type"], str)
    assert isinstance(apod["explanation"], str)
    assert isinstance(apod["url"], str)
