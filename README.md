# Regional Job Finder

A clean, minimal Python CLI tool for searching jobs in regional Victoria using the Adzuna API.

---

## 📌 Overview

Regional Job Finder is a command-line application that:

* Searches for jobs across multiple regional locations
* Uses predefined keywords (logistics, QA, compliance, etc.)
* Fetches results from the Adzuna API
* Displays jobs in a clean terminal format
* Optionally exports results to CSV

The project is structured using modern Python practices (`src/` layout, `pyproject.toml`, `uv`), and is designed to be simple, extendable, and practical.

---

## 🚀 Features

* Multi-location job search
* Keyword-based querying
* Duplicate job removal
* Clean CLI output
* Optional CSV export
* Timestamped output files
* Environment-based API configuration
* Basic test coverage (duplicate handling)

---

## 🧱 Project Structure

```text
regional-job-finder/
│
├── src/
│   └── regional_job_finder/
│       ├── main.py        # CLI entry point
│       ├── jobs.py        # API calls and job fetching
│       ├── config.py      # Default locations and keywords
│       └── output.py      # Terminal output and CSV export
│
├── tests/
│   └── test_jobs.py       # Basic test (duplicate removal)
│
├── pyproject.toml         # Project config (uv-managed)
├── uv.lock                # Locked dependencies
├── .gitignore
├── resume.txt             # Optional (future use)
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/regional-job-finder.git
cd regional-job-finder
```

### 2. Install dependencies (using uv)

```bash
uv sync
```

---

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

Get API credentials here:
https://developer.adzuna.com/

---

## ▶️ Running the Application

### Recommended (CLI command)

```bash
uv run job-finder
```

### Alternative

```bash
uv run python -m regional_job_finder.main
```

---

## 💾 CSV Export

Save results to CSV:

```bash
uv run job-finder --csv
```

Custom output directory:

```bash
uv run job-finder --csv --output-dir results
```

Output example:

```text
output/job_results_2026-05-01_16-30-12.csv
```

---

## 🧩 CLI Options

| Option         | Description                               |
| -------------- | ----------------------------------------- |
| `--csv`        | Save results to a CSV file                |
| `--output-dir` | Set output directory (default: `output/`) |

---

## 📍 Default Configuration

Defined in:

```text
src/regional_job_finder/config.py
```

### Locations

* Mildura
* Red Cliffs
* Merbein
* Robinvale

### Keywords

* export officer
* biosecurity
* grain inspector
* QA officer
* compliance officer

---

## 🧪 Running Tests

```bash
uv run pytest
```

Current test coverage includes:

* Duplicate job removal logic

---

## ⚠️ Current Limitations

* Resume is loaded but not used in matching yet
* Search is based on fixed keywords
* No ranking or filtering of results
* No JSON export
* CLI options are minimal

---

## 🔮 Planned Improvements

* Resume keyword extraction
* Job ranking by relevance
* Filtering (location, salary, type)
* JSON export
* Custom CLI options (keywords, locations)
* UI (optional)

---

## 🧠 Purpose

This project was built to:

* Practice clean Python project structure
* Work with external APIs
* Use modern tooling (`uv`, `pyproject.toml`)
* Build a practical CLI tool
* Incrementally improve functionality

---

## 📄 License

MIT License
