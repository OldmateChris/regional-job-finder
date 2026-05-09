import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_LOCATIONS = ["Mildura", "Red Cliffs", "Merbein", "Robinvale"]

DEFAULT_KEYWORDS = [
    "export officer",
    "biosecurity",
    "grain inspector",
    "QA officer",
    "compliance officer",
    "admin",
    "warehouse",
]

RESULTS_PER_SEARCH = 5

ADZUNA_URL = "https://api.adzuna.com/v1/api/jobs/au/search/1"


def get_api_credentials():
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")
    return app_id, app_key
