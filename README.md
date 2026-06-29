# Python Job Listings Scraper

A beginner-friendly web scraping project built with Python that collects job listings from the Fake Python Jobs website using Requests and BeautifulSoup.

## Features

- Scrapes all available job listings
- Extracts:
  - Job Title
  - Company Name
  - Location
  - Job Detail URL
- Stores the data in a CSV file
- Handles missing fields gracefully
- Uses clean and readable Python code

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- CSV Module

## Project Structure

```
python-job-listings-scraper/
│
├── main.py
├── jobs.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/python-job-listings-scraper.git
```

Move into the project

```bash
cd python-job-listings-scraper
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the scraper

```bash
python main.py
```

## Output

The scraper creates a file named

```
jobs.csv
```

Example:

| Job Title | Company | Location | URL |
| ---------- | ------- | -------- | --- |
| Python Developer | ABC Company | New York | https://... |

## Learning Outcomes

This project demonstrates:

- HTTP requests using Requests
- HTML parsing with BeautifulSoup
- Extracting structured data
- Working with Lists and Dictionaries
- Writing CSV files
- Basic error handling

## Future Improvements

- Pagination support
- Export to JSON
- Command-line arguments
- Logging
- Filtering by location or company
- Unit tests

## Data Source

https://realpython.github.io/fake-jobs/


https://roadmap.sh/projects/job-listings-scraper
This website is provided by Real Python specifically for learning web scraping.
