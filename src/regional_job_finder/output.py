import csv
from datetime import datetime
from pathlib import Path


def print_jobs(jobs):
    if not jobs:
        print("No jobs found.")
        return

    for index, job in enumerate(jobs, start=1):
        title = job.get("title", "No title")
        company = job.get("company", {}).get("display_name", "Unknown company")
        location = job.get("location", {}).get("display_name", "Unknown location")
        score = job.get("match_score", 0)
        matched_skills = job.get("matched_skills", [])
        link = job.get("redirect_url", "No link available")

        print(f"{index}. {title}")
        print(f"   Company: {company}")
        print(f"   Location: {location}")
        print(f"   Match Score: {score}")
        print(f"   Matched Skills: {', '.join(matched_skills)}")
        print(f"   Link: {link}\n")


def save_jobs_to_csv(jobs, output_dir="output"):
    if not jobs:
        print("No jobs to save.")
        return None

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    csv_path = output_path / f"job_results_{timestamp}.csv"

    fieldnames = [
        "id",
        "title",
        "company",
        "location",
        "salary_min",
        "salary_max",
        "contract_time",
        "contract_type",
        "created",
        "description",
        "redirect_url",
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for job in jobs:
            writer.writerow(
                {
                    "id": job.get("id", ""),
                    "title": job.get("title", ""),
                    "company": job.get("company", {}).get("display_name", ""),
                    "location": job.get("location", {}).get("display_name", ""),
                    "salary_min": job.get("salary_min", ""),
                    "salary_max": job.get("salary_max", ""),
                    "contract_time": job.get("contract_time", ""),
                    "contract_type": job.get("contract_type", ""),
                    "created": job.get("created", ""),
                    "description": job.get("description", ""),
                    "redirect_url": job.get("redirect_url", ""),
                }
            )

    print(f"Saved {len(jobs)} jobs to {csv_path.resolve()}")
    return csv_path
