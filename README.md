# Regional Job Finder

A simple Python CLI application that searches for jobs in regional Victoria using the Adzuna API.

---

## 📌 Overview

This project is a command-line tool that:

* Searches for jobs across multiple regional locations
* Uses predefined keywords relevant to logistics, QA, and compliance roles
* Fetches results from the Adzuna jobs API
* Displays job listings in a clean, readable format in the terminal
* Optionally exports job results to a timestamped CSV file

---

## 🚀 Features

* Multi-location job search
* Customisable keywords and locations
* Duplicate job removal
* Clean CLI output
* Optional CSV export
* Timestamped output files
* Environment-based API configuration

---

## 🧱 Project Structure

```text
regional-job-finder/
│
├── src/
│   └── regional_job_finder/
│       ├── main.py        # Entry point and CLI arguments
│       ├── jobs.py        # API calls and job fetching
│       ├── config.py      # Default settings
│       └── output.py      # Terminal output and CSV export
│
├── tests/                 # (Currently empty)
├── .env                   # API keys (not committed)
├── .env.example           # Example environment file
├── resume.txt             # Resume file (used for future enhancements)
├── pyproject.toml         # Project configuration
├── uv.lock                # Dependency lock file
└── README.md

⚙️ Setup
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/regional-job-finder.git
cd regional-job-finder
2. Install dependencies (using uv)
uv sync
3. Set up environment variables

Create a .env file in the root directory:

ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key

You can get API credentials from:

https://developer.adzuna.com/

▶️ Running the application
Standard run
uv run python -m regional_job_finder.main

This will search for jobs and print the results to the terminal.

Save results to CSV
uv run python -m regional_job_finder.main --csv

This will:

Print the jobs to the terminal
Create an output/ folder if it does not already exist
Save a timestamped CSV file inside it

Example output file:

output/job_results_2026-04-19_22-15-03.csv
Save CSV to a custom folder
uv run python -m regional_job_finder.main --csv --output-dir results

This will save the CSV file into the results/ folder instead of output/.

🧩 CLI Options
--csv

Saves the fetched job results to a CSV file.

--output-dir

Sets the folder where the CSV file should be saved.

Default:

output

Example:

uv run python -m regional_job_finder.main --csv --output-dir results
📍 Default Configuration
Locations
Mildura
Red Cliffs
Merbein
Robinvale
Keywords
export officer
biosecurity
grain inspector
QA officer
compliance officer

You can modify these in:

src/regional_job_finder/config.py
📄 CSV Output Fields

When CSV export is enabled, the file includes fields like:

id
title
company
location
salary_min
salary_max
contract_time
contract_type
created
description
redirect_url
⚠️ Current Limitations
Resume is loaded but not yet used in job matching
Search is still based on fixed keywords by default
No filtering or ranking of job results yet
No JSON export yet
Tests are still empty
🔮 Future Improvements
Extract keywords from resume automatically
Rank jobs based on relevance
Add filtering (location, salary, job type)
Add JSON export
Add CLI options for custom keywords and locations
Build a simple UI
🧠 Purpose

This project was built as a learning exercise to:

Practice Python project structure
Work with APIs
Use modern tooling (uv, pyproject.toml)
Build a real-world CLI tool
Improve the project incrementally with practical features like export support
📄 License

This project is open-source and available under the MIT License.
