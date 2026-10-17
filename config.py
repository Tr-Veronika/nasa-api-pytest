import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

APOD_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"
NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed"
IMAGE_URL = "https://images-api.nasa.gov/search"
EXOPLANET_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

TIMEOUT = 15

APOD_DATE = "2026-09-11"
NEO_DATE = "2026-08-06"
