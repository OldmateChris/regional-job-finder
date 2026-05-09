from regional_job_finder.jobs import get_jobs


def test_get_jobs_removes_duplicates(monkeypatch):
    def fake_fetch_jobs(location, keyword, results_per_page):
        return [
            {"id": "1", "title": "Job A"},
            {"id": "1", "title": "Job A"},  # duplicate
            {"id": "2", "title": "Job B"},
        ]

    # Replace real API call
    monkeypatch.setattr(
        "regional_job_finder.jobs.fetch_jobs_for_location",
        fake_fetch_jobs,
    )

    jobs = get_jobs(locations=["test"], keywords=["test"])

    assert len(jobs) == 2


def test_get_jobs_accepts_single_string_inputs(monkeypatch):
    calls = []

    def fake_fetch_jobs(location, keyword, results_per_page):
        calls.append((location, keyword))
        return [{"id": "1", "title": "Job A"}]

    monkeypatch.setattr(
        "regional_job_finder.jobs.fetch_jobs_for_location",
        fake_fetch_jobs,
    )

    jobs = get_jobs(locations="Mildura", keywords="admin")

    assert len(jobs) == 1
    assert calls == [("Mildura", "admin")]
