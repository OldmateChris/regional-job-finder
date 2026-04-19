from pathlib import Path

from regional_job_finder.jobs import get_jobs
from regional_job_finder.output import print_jobs


def load_resume():
    try:
        return Path("resume.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("resume.txt not found.")
        return ""


def main():
    print("Loading resume...")
    resume = load_resume()

    if not resume:
        print("Could not load resume.")
        return

    print("Resume loaded successfully.\n")
    print("Searching for jobs...\n")

    jobs = get_jobs()
    print_jobs(jobs)


if __name__ == "__main__":
    main()