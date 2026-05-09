import requests

from regional_job_finder.config import (
    ADZUNA_URL,
    DEFAULT_KEYWORDS,
    DEFAULT_LOCATIONS,
    RESULTS_PER_SEARCH,
    get_api_credentials,
)


def fetch_jobs_for_location(location, keyword, results_per_page):
    app_id, app_key = get_api_credentials()

    if not app_id or not app_key:
        print("Missing Adzuna API credentials in .env file.")
        return []

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "what": keyword,
        "where": location,
        "results_per_page": results_per_page,
    }

    try:
        response = requests.get(ADZUNA_URL, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.RequestException as error:
        print(f"Error fetching jobs for {location} / {keyword}: {error}")
        return []


def get_jobs(locations=None, keywords=None):
    locations = locations or DEFAULT_LOCATIONS
    keywords = keywords or DEFAULT_KEYWORDS

    if isinstance(locations, str):
        locations = [locations]

    if isinstance(keywords, str):
        keywords = [keywords]

    all_jobs = []

    for location in locations:
        for keyword in keywords:
            jobs = fetch_jobs_for_location(
                location, keyword, RESULTS_PER_SEARCH
            )
            all_jobs.extend(jobs)

    unique_jobs = {job["id"]: job for job in all_jobs if "id" in job}
    return list(unique_jobs.values())
