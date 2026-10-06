# Multi-Source Web Scraping & Data Consolidation

A Python web scraping pipeline that collects data from:

• Books to Scrape
• Quotes to Scrape

## Workflow

Books to Scrape ──┐
                  ├── Scraping
Quotes to Scrape ─┘
                      ↓
                   Cleaning
                      ↓
                  Validation
                      ↓
                 Deduplication
                      ↓
              Final Dataset

## Technologies

Python
Requests
BeautifulSoup
Pandas
Pytest

## Features

✓ Pagination
✓ Data cleaning
✓ Validation
✓ Duplicate detection
✓ Error handling
✓ Retry mechanism
✓ Logging
✓ CSV output
✓ JSON summary report
✓ Unit tests

## How to Run

1. Clone the repository
2. Create virtual environment
3. Install requirements
4. Run main.py
5. Run tests

## Output

final_dataset.csv
summary_report.json
scraping.log
