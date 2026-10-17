"""  NASA Image and Video Library  """

from api_client import get_json
from config import IMAGE_URL


def test_image_search_returns_successful_response(image_search_data):
    """Image search response contains the expected structure."""
    assert "collection" in image_search_data
    assert isinstance(image_search_data["collection"], dict)
    assert "items" in image_search_data["collection"]
    assert isinstance(image_search_data["collection"]["items"], list)


def test_image_search_returns_items_with_metadata(image_search_data):
    """Search results contain item metadata."""
    items = image_search_data["collection"]["items"]

    assert items, "No image search results found"

    first_item = items[0]

    assert "data" in first_item
    assert isinstance(first_item["data"], list)
    assert first_item["data"], "Item metadata is empty"

    metadata = first_item["data"][0]

    assert "title" in metadata
    assert isinstance(metadata["title"], str)
    assert metadata["title"].strip()


def test_image_search_with_unlikely_query_returns_no_results():
    """An unlikely search query returns an empty result list."""
    data = get_json(
        IMAGE_URL,
        params={
            "q": "zzzxxyy_no_matching_nasa_asset_987654321",
            "page_size": 1,
        },
    )

    assert "collection" in data
    assert data["collection"]["items"] == []
