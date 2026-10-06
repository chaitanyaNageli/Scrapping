from scrapper.books_scrapper import BooksScrapper
from scrapper.quotes_scrapper import QuotesScrapper
from processing.cleaning import Cleaning
from processing.validation import Validation
from processing.deduplication import find_duplicates
import logging
import json
import pandas as pd


logging.basicConfig(
    filename="logs/scraping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Started Book scrapping")
booksObj = BooksScrapper("https://books.toscrape.com/catalogue/category/books_1/page-1.html")

books_data = booksObj.scrape()
logger.info("Ended Book scrapping")

logger.info("Started Book scrap cleaning")
cleaning = Cleaning()

for record in books_data:
    record["name_or_title"] = cleaning.clean_text(record["name_or_title"])

    record["category"] = cleaning.clean_text(record["category"])

    record["description"] = cleaning.clean_text(record["description"])

    record["price"] = cleaning.clean_price(record["price"])

    record["rating"] = cleaning.clean_rating(record["rating"])

logger.info("Ended Book scrap cleaning")
logger.info("Started Quotes scraping")
quotesObj = QuotesScrapper("https://quotes.toscrape.com/")

quotes_data = quotesObj.scrape()

logger.info("Ended Quotes scraping")
data = []

data.extend(books_data)
data.extend(quotes_data)

total_records = len(data)

validator = Validation()

valid_data = []
rejected_count = 0

for record in data:

    problems = validator.validate_record(record)

    if problems:
        rejected_count += 1
    else:
        valid_data.append(record)


unique_data, duplicate_data = find_duplicates(valid_data)

duplicates_detected = len(duplicate_data)
duplicates_removed = duplicates_detected

final_data = unique_data


df = pd.DataFrame(final_data)

df.to_csv("output/final_dataset.csv",index=False)
logger.info("CREATED CSV")




summary = {
    "total_records": total_records,

    "records_per_source": {
        "Books to Scrape": len(books_data),
        "Quotes to Scrape": len(quotes_data)
    },

    "records_after_cleaning": len(data),

    "rejected_validation_records": rejected_count,

    "duplicates_detected": duplicates_detected,

    "duplicates_removed": duplicates_removed,

    "final_record_count": len(final_data),

}


with open("output/summary_report.json","w",encoding="utf-8")as file:
    json.dump(summary,file,indent=4)


logger.info("CREATED REPORT")