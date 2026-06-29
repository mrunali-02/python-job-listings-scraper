import csv
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:

        title_tag = job.find("h2", class_="title is-5")
        company_tag = job.find("h3", class_="subtitle is-6 company")
        location_tag = job.find("p", class_="location")
        link_tag = job.find("a")

        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        company = company_tag.get_text(strip=True) if company_tag else "N/A"
        location = location_tag.get_text(strip=True) if location_tag else "N/A"
        link = link_tag["href"] if link_tag else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "url": link
        })

    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Job Title", "Company", "Location", "URL"])

        for job in jobs:
            writer.writerow([
                job["title"],
                job["company"],
                job["location"],
                job["url"]
            ])

    print(f"Successfully scraped {len(jobs)} jobs.")
    print("Data saved to jobs.csv")

else:
    print(f"Failed to fetch the webpage. Status Code: {response.status_code}")