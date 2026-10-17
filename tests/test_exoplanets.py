"""  NASA Exoplanet Archive  """

def test_exoplanet_returns_list(exoplanet_data):
    """Exoplanet Archive returns a JSON list."""
    assert isinstance(exoplanet_data, list)


def test_exoplanet_contains_planet_data(exoplanet_data):
    """Exoplanet records contain valid planet names."""
    assert exoplanet_data, "No exoplanet records returned"

    planet = exoplanet_data[0]

    assert "pl_name" in planet
    assert isinstance(planet["pl_name"], str)
    assert planet["pl_name"].strip()
