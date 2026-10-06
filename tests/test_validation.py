from processing.validation import Validation


def test_valid_record():
    validator = Validation()

    record = {
        "source": "Books to Scrape",
        "name_or_title": "Example Book",
        "source_url": "https://books.toscrape.com/catalogue/example",
        "price": 25.99,
        "rating": 4
    }

    assert validator.validate_record(record) == []


def test_unknown_source():
    validator = Validation()

    record = {
        "source": "Unknown Source",
        "name_or_title": "Example Book",
        "source_url": "https://example.com",
        "price": 25.99,
        "rating": 4
    }

    problems = validator.validate_record(record)

    assert "unknown_source" in problems


def test_missing_name():
    validator = Validation()

    record = {
        "source": "Books to Scrape",
        "name_or_title": None,
        "source_url": "https://example.com",
        "price": 25.99,
        "rating": 4
    }

    problems = validator.validate_record(record)

    assert "missing_name" in problems


def test_invalid_url():
    validator = Validation()

    record = {
        "source": "Books to Scrape",
        "name_or_title": "Example Book",
        "source_url": "invalid-url",
        "price": 25.99,
        "rating": 4
    }

    problems = validator.validate_record(record)

    assert "invalid_url" in problems


def test_invalid_price():
    validator = Validation()

    record = {
        "source": "Books to Scrape",
        "name_or_title": "Example Book",
        "source_url": "https://example.com",
        "price": -10,
        "rating": 4
    }

    problems = validator.validate_record(record)

    assert "invalid_price" in problems


def test_invalid_rating():
    validator = Validation()

    record = {
        "source": "Books to Scrape",
        "name_or_title": "Example Book",
        "source_url": "https://example.com",
        "price": 25.99,
        "rating": 6
    }

    problems = validator.validate_record(record)

    assert "invalid_rating" in problems