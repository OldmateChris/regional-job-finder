from regional_job_finder.jobs import get_jobs
from regional_job_finder.matcher import (
    filter_jobs_by_score,
    match_job,
    score_jobs,
)
from regional_job_finder.resume import extract_resume_skills, get_resume_search_keywords


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


def test_qa_job_scores_well():
    job = {
        "title": "Quality Assurance Officer",
        "description": "Quality assurance, audit, compliance and HACCP responsibilities",
    }

    result = match_job(job)

    assert result["match_score"] > 0
    assert "quality" in result["matched_categories"]


def test_unrelated_job_scores_low():
    job = {
        "title": "Hairdresser",
        "description": "Cutting and styling hair",
    }

    result = match_job(job)

    assert result["match_score"] <= 2


def test_jobs_sorted_by_score():
    jobs = [
        {
            "title": "Hairdresser",
            "description": "Hair styling",
        },
        {
            "title": "Quality Assurance Officer",
            "description": "QA compliance HACCP audit",
        },
    ]

    results = score_jobs(jobs)

    assert results[0]["title"] == "Quality Assurance Officer"


def test_filter_jobs_by_score():
    jobs = [
        {"match_score": 10},
        {"match_score": 2},
    ]

    results = filter_jobs_by_score(jobs, min_score=5)

    assert len(results) == 1
    assert results[0]["match_score"] == 10


def test_extract_resume_skills_finds_known_skills():
    resume_text = """
    Experienced in Quality Assurance, HACCP, forklift operation,
    warehouse work, logistics, compliance and SAP reporting.
    """

    skills = extract_resume_skills(resume_text)

    assert "quality assurance" in skills
    assert "haccp" in skills
    assert "forklift" in skills
    assert "warehouse" in skills
    assert "logistics" in skills
    assert "compliance" in skills
    assert "sap" in skills


def test_extract_resume_skills_handles_empty_resume():
    skills = extract_resume_skills("")

    assert skills == []


def test_get_resume_search_keywords_limits_results():
    resume_text = """
    quality assurance compliance biosecurity export inspection audit
    forklift warehouse logistics production supervisor documentation
    """

    keywords = get_resume_search_keywords(resume_text, limit=5)

    assert len(keywords) == 5
