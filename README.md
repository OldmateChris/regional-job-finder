# Regional Job Finder

A simple Python CLI application that searches for jobs in regional Victoria using the Adzuna API.

---

## 📌 Overview

This project is a command-line tool that:

* Searches for jobs across multiple regional locations
* Uses predefined keywords relevant to logistics, QA, and compliance roles
* Fetches results from the Adzuna jobs API
* Displays job listings in a clean, readable format in the terminal

---

## 🚀 Features

* Multi-location job search
* Customisable keywords and locations
* Duplicate job removal
* Clean CLI output
* Environment-based API configuration

---

## 🧱 Project Structure

```
regional-job-finder/
│
├── src/
│   └── regional_job_finder/
│       ├── main.py        # Entry point
│       ├── jobs.py        # API calls and job fetching
│       ├── config.py      # Default settings
│       └── output.py      # Formatting and printing results
│
├── tests/                 # (Currently empty)
├── .env                   # API keys (not committed)
├── .env.example           # Example environment file
├── resume.txt             # Resume file (used for future enhancements)
├── pyproject.toml         # Project configuration
├── uv.lock                # Dependency lock file
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/regional-job-finder.git
cd regional-job-finder
```

---

### 2. Install dependencies (using uv)

```
uv sync
```

---

### 3. Set up environment variables

Create a `.env` file in the root directory:

```
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

You can get API credentials from:
https://developer.adzuna.com/

---

### 4. Run the application

```
uv run python -m regional_job_finder.main
```

---

## 📍 Default Configuration

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

You can modify these in:

```
src/regional_job_finder/config.py
```

---

## ⚠️ Current Limitations

* Resume is loaded but not yet used in job matching
* Search is based on fixed keywords (not dynamic)
* No filtering or ranking of job results
* Results are only printed (not saved/exported)

---

## 🔮 Future Improvements

* Extract keywords from resume automatically
* Rank jobs based on relevance
* Add filtering (location, salary, job type)
* Export results to CSV or JSON
* Build a simple UI

---

## 🧠 Purpose

This project was built as a learning exercise to:

* Practice Python project structure
* Work with APIs
* Use modern tooling (`uv`, `pyproject.toml`)
* Build a real-world CLI tool

---

## 📄 License

This project is open-source and available under the MIT License.
