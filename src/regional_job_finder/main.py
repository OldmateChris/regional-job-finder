import argparse
from pathlib import Path

from regional_job_finder.jobs import get_jobs
from regional_job_finder.matcher import filter_jobs_by_score, score_jobs
from regional_job_finder.output import print_jobs, save_jobs_to_csv


def load_resume():
    try:
        return Path("resume.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("resume.txt not found.")
        return ""


def parse_args():
    parser = argparse.ArgumentParser(
        description="Search for regional jobs using Adzuna API"
    )

    parser.add_argument(
        "--min-score",
        type=int,
        default=0,
        help="Only show jobs with this match score or higher",
    )

    parser.add_argument(
        "--csv",
        action="store_true",
        help="Save results to a CSV file",
    )

    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory to save CSV file (default: output)",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print("Loading resume...")
    resume = load_resume()

    if resume:
        print("Resume loaded successfully.\n")
    else:
        print("No resume loaded. Continuing without resume matching.\n")

    print("Searching for jobs...\n")

    jobs = get_jobs()
    jobs = score_jobs(jobs)
    jobs = filter_jobs_by_score(jobs, min_score=args.min_score)

    print_jobs(jobs)

    if args.csv:
        save_jobs_to_csv(jobs, output_dir=args.output_dir)


if __name__ == "__main__":
    main()
