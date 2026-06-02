# Regional Job Finder

A Python CLI application that searches for jobs using the Adzuna API and ranks them based on relevance to your professional background.

---

## 📌 Overview

Regional Job Finder is a command-line application that:

* Searches for jobs across multiple locations
* Uses configurable search keywords
* Fetches results from the Adzuna API
* Scores jobs against resume-inspired skill categories
* Ranks jobs by relevance
* Filters jobs using a minimum match score
* Displays match explanations in the terminal
* Optionally exports results to CSV

The project follows modern Python practices (`src/` layout, `pyproject.toml`, `uv`) and is designed to be practical, extensible, and easy to maintain.

---

## 🚀 Features

### Job Search

* Multi-location job search
* Keyword-based querying
* Adzuna API integration
* Duplicate job removal

### Resume-Aware Matching

* Resume-inspired skill matching
* Broad skill-category scoring
* Match score calculation
* Match category detection
* Match skill detection
* Job ranking by relevance
* Minimum-score filtering

### Output

* Clean terminal output
* Match explanations
* Optional CSV export
* Timestamped result files

### Reliability

* Environment-based configuration
* Unit test coverage
* Mocked API testing

---

## 🧱 Project Structure

```text
regional-job-finder/
│
├── src/
│   └── regional_job_finder/
│       ├── main.py        # CLI entry point
│       ├── jobs.py        # Job retrieval and deduplication
│       ├── matcher.py     # Resume-aware job scoring
│       ├── config.py      # Search configuration
│       └── output.py      # Terminal output and CSV export
│
├── tests/
│   └── test_jobs.py       # Job retrieval and matcher tests
│
├── pyproject.toml
├── uv.lock
├── resume.txt
└── README.md
```

---

## ⚙️ Setup

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/regional-job-finder.git
cd regional-job-finder
```

### Install dependencies

```bash
uv sync
```

### Configure Adzuna credentials

Create a `.env` file in the project root:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

Get API credentials:

https://developer.adzuna.com/

---

## ▶️ Running the Application

Standard run:

```bash
uv run job-finder
```

Show only stronger matches:

```bash
uv run job-finder --min-score 5
```

Alternative entry point:

```bash
uv run python -m regional_job_finder.main
```

---

## 🧩 CLI Options

| Option         | Description                                          |
| -------------- | ---------------------------------------------------- |
| `--csv`        | Save results to CSV                                  |
| `--output-dir` | Output directory for CSV files                       |
| `--min-score`  | Only show jobs at or above the specified match score |

---

## 📊 Example Output

```text
1. Quality Assurance Officer

   Company: Example Foods
   Location: Mildura
   Match Score: 18

   Matched Categories:
   quality, compliance

   Matched Skills:
   quality assurance, HACCP, audit, compliance

   Link:
   https://...
```

---

## 🧪 Running Tests

Run all tests:

```bash
uv run pytest
```

Current test coverage includes:

* Duplicate job removal
* Single-string input handling
* Match scoring
* Match filtering
* Job ranking
* Unrelated-job scoring

---

## ⚠️ Current Limitations

* Search keywords are still manually configured
* Resume parsing is not yet automatic
* Match scoring is rule-based rather than AI-driven
* CSV export does not yet include all match metadata
* No JSON export

---

## 🔮 Planned Improvements

* Automatic resume keyword extraction
* Dynamic search keyword generation
* Match-score export to CSV
* Salary filtering
* Location filtering
* Contract-type filtering
* JSON export
* Interactive TUI or GUI
* AI-assisted ranking and recommendations

---

## 🧠 Purpose

This project was built to:

* Practice modern Python development
* Work with external APIs
* Build a practical job-search tool
* Experiment with resume-aware job matching
* Incrementally develop a recommendation engine

---

## 📄 License

MIT License
