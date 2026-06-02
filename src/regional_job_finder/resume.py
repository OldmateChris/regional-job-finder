from pathlib import Path

KNOWN_RESUME_SKILLS = [
    "quality assurance",
    "quality control",
    "qa",
    "compliance",
    "regulatory compliance",
    "biosecurity",
    "export",
    "inspection",
    "inspector",
    "audit",
    "haccp",
    "food safety",
    "forklift",
    "warehouse",
    "logistics",
    "supply chain",
    "dispatch",
    "inventory",
    "stock control",
    "production",
    "manufacturing",
    "machine operator",
    "plant operator",
    "process operator",
    "supervisor",
    "team leader",
    "training",
    "admin",
    "administrator",
    "documentation",
    "reporting",
    "safety",
    "sap",
    "pems",
    "myosh",
]


def load_resume(path="resume.txt"):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def extract_resume_skills(resume_text):
    resume_text = resume_text.lower()

    matched_skills = []

    for skill in KNOWN_RESUME_SKILLS:
        if skill.lower() in resume_text:
            matched_skills.append(skill)

    return matched_skills


def get_resume_search_keywords(resume_text, limit=10):
    skills = extract_resume_skills(resume_text)

    if not skills:
        return []

    return skills[:limit]
