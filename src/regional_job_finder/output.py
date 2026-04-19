def print_jobs(jobs):
    if not jobs:
        print("No jobs found.")
        return

    for index, job in enumerate(jobs, start=1):
        title = job.get("title", "No title")
        company = job.get("company", {}).get("display_name", "Unknown company")
        location = job.get("location", {}).get("display_name", "Unknown location")
        link = job.get("redirect_url", "No link available")

        print(f"{index}. {title}")
        print(f"   Company: {company}")
        print(f"   Location: {location}")
        print(f"   Link: {link}\n")