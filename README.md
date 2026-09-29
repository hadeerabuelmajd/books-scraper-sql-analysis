# Books Scraping & SQL Analysis

## Overview

This project scrapes book data from Books to Scrape, saves the collected dataset into a CSV file, and performs SQL queries.

## Data Collected

- Title
- Price
- Rating
- Stock status
- Book URL

## Tech Stack
- **Language:** Python
- **Libraries:** `requests`, `beautifulsoup4`, `csv`
- **Database:** SQL Server

## Files

- `books_scraper.py` — Python web scraper
- `books.csv` — Extracted dataset
- `books_analysis_queries.sql` — SQL queries

---

## Challenges & Strategy

What took longer than expected was handling the HTML structure correctly.
I spent some time making sure the extracted data and URLs were accurate.
If the site started blocking me after 50 requests, I would slow down the requests.
I would add a delay between requests and handle failed or blocked responses.
I would also retry after waiting instead of sending requests continuously.
