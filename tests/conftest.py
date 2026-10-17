import pytest

from config import (
    NASA_API_KEY,
    APOD_URL,
    NEO_URL,
    IMAGE_URL,
    EXOPLANET_URL,
    APOD_DATE,
    NEO_DATE,
)
from api_client import get_json


@pytest.fixture(scope="module")
def apod_data():
    """Return APOD data for a fixed date."""
    return get_json(
        APOD_URL,
        params={
            "start_date": APOD_DATE,
            "end_date": APOD_DATE,
            "api_key": NASA_API_KEY,
        },
    )


@pytest.fixture(scope="module")
def neo_data():
    """Return the near-Earth object feed for a fixed date."""
    return get_json(
        NEO_URL,
        params={
            "start_date": NEO_DATE,
            "end_date": NEO_DATE,
            "api_key": NASA_API_KEY,
        },
    )


@pytest.fixture(scope="module")
def image_search_data():
    """Return image search results for a known query."""
    return get_json(
        IMAGE_URL,
        params={
            "q": "apollo",
            "page_size": 1,
        },
    )


@pytest.fixture(scope="module")
def exoplanet_data():
    """Return a small sample of confirmed exoplanet names."""
    return get_json(
        EXOPLANET_URL,
        params={
            "query": (
                "select top 10 pl_name "
                "from pscomppars "
                "where pl_name is not null "
                "order by pl_name"
            ),
            "format": "json",
        },
    )
