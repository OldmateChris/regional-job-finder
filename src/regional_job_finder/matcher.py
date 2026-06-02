"""
Job matching and scoring helpers for Regional Job Finder.

This module gives each job a match score based on broad skill categories
from your master resume. It is intentionally broad so the app can find
related roles, not just exact job titles.
"""

from __future__ import annotations

SKILL_CATEGORIES = {
    "quality": [
        "quality assurance",
        "quality control",
        "qa",
        "qc",
        "inspection",
        "inspector",
        "testing",
        "food safety",
        "haccp",
        "quality systems",
        "non-conformance",
        "corrective action",
        "audit",
        "auditing",
        "product integrity",
    ],
    "compliance": [
        "compliance",
        "regulatory",
        "regulation",
        "biosecurity",
        "export",
        "authorised officer",
        "authorized officer",
        "protocol",
        "work plan",
        "documentation control",
        "record keeping",
        "government",
        "risk management",
        "procedure",
        "standards",
    ],
    "logistics": [
        "logistics",
        "supply chain",
        "transport",
        "freight",
        "dispatch",
        "receiving",
        "distribution",
        "third-party",
        "supplier",
        "loading",
        "unloading",
        "yard",
        "materials handling",
        "coordination",
    ],
    "warehouse": [
        "warehouse",
        "storeperson",
        "forklift",
        "lf licence",
        "lf license",
        "inventory",
        "stock control",
        "stock management",
        "pallet",
        "palletising",
        "depalletising",
        "deliveries",
        "storage",
        "goods in",
        "goods out",
    ],
    "production": [
        "production",
        "manufacturing",
        "factory",
        "process operator",
        "machine operator",
        "plant operator",
        "equipment operation",
        "packaging",
        "processing",
        "bottling",
        "pasteurisation",
        "pasteurization",
        "machinery",
        "continuous improvement",
        "food production",
    ],
    "leadership_admin": [
        "supervisor",
        "team leader",
        "leadership",
        "training",
        "coordinator",
        "administrator",
        "admin",
        "scheduling",
        "reporting",
        "documentation",
        "customer service",
        "stakeholder",
        "staff",
        "workflow",
        "performance",
    ],
    "safety": [
        "safety",
        "workplace safety",
        "ohs",
        "whs",
        "hygiene",
        "sanitation",
        "confined space",
        "manual handling",
        "safe work",
        "risk assessment",
    ],
    "systems": [
        "sap",
        "pems",
        "myosh",
        "pos",
        "digital system",
        "data entry",
        "records",
        "reporting system",
        "production monitoring",
    ],
}


BROAD_JOB_TITLES = [
    "quality officer",
    "quality coordinator",
    "quality inspector",
    "compliance officer",
    "compliance coordinator",
    "operations officer",
    "operations coordinator",
    "logistics coordinator",
    "warehouse supervisor",
    "warehouse coordinator",
    "inventory controller",
    "production supervisor",
    "production coordinator",
    "site coordinator",
    "dispatch coordinator",
    "safety officer",
    "food safety officer",
    "supply chain coordinator",
]


def _normalise(value: object) -> str:
    """Convert a value to lowercase searchable text."""
    if value is None:
        return ""
    return str(value).lower()


def job_to_text(job: dict) -> str:
    """
    Combine the most useful Adzuna job fields into one searchable text block.
    Missing fields are handled safely.
    """
    parts = [
        job.get("title", ""),
        job.get("description", ""),
        job.get("contract_time", ""),
        job.get("contract_type", ""),
        job.get("category", {}).get("label", ""),
        job.get("company", {}).get("display_name", ""),
        job.get("location", {}).get("display_name", ""),
    ]

    return " ".join(_normalise(part) for part in parts)


def match_job(job: dict) -> dict:
    """
    Score a single job and return a copy of the job with match information.

    Scoring:
    - +3 if a broad target title appears in the job title
    - +2 for each matched skill/category term
    - +1 if salary information exists
    - +1 if contract information exists
    - +2 bonus if the job matches 3 or more categories
    """
    job_text = job_to_text(job)
    title_text = _normalise(job.get("title", ""))

    matched_skills = []
    matched_categories = []

    score = 0

    for category, skills in SKILL_CATEGORIES.items():
        category_matches = []

        for skill in skills:
            if skill.lower() in job_text:
                category_matches.append(skill)

        if category_matches:
            matched_categories.append(category)
            matched_skills.extend(category_matches)
            score += len(category_matches) * 2

    matched_titles = [
        title for title in BROAD_JOB_TITLES if title.lower() in title_text
    ]

    if matched_titles:
        score += 3

    if job.get("salary_min") or job.get("salary_max"):
        score += 1

    if job.get("contract_time") or job.get("contract_type"):
        score += 1

    if len(matched_categories) >= 3:
        score += 2

    # Remove duplicate matched skills while keeping the original order.
    unique_skills = list(dict.fromkeys(matched_skills))

    matched_job = job.copy()
    matched_job["match_score"] = score
    matched_job["matched_skills"] = unique_skills
    matched_job["matched_categories"] = matched_categories
    matched_job["matched_titles"] = matched_titles

    return matched_job


def score_jobs(jobs: list[dict]) -> list[dict]:
    """Score all jobs and return them from best match to weakest match."""
    scored_jobs = [match_job(job) for job in jobs]
    return sorted(
        scored_jobs,
        key=lambda job: job.get("match_score", 0),
        reverse=True,
    )


def filter_jobs_by_score(jobs: list[dict], min_score: int = 0) -> list[dict]:
    """Keep only jobs with a match score greater than or equal to min_score."""
    return [job for job in jobs if job.get("match_score", 0) >= min_score]


def get_search_keywords() -> list[str]:
    """
    Return broad keywords that can be used for API searches.

    These are broad enough to find related work, while still being connected
    to your resume background.
    """
    return [
        "quality",
        "compliance",
        "inspection",
        "logistics",
        "warehouse",
        "forklift",
        "production",
        "manufacturing",
        "operations",
        "supervisor",
        "coordinator",
        "admin",
        "safety",
        "inventory",
        "dispatch",
        "food safety",
        "supply chain",
    ]
