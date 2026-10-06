from processing.cleaning import Cleaning


def test_clean_text():
    cleaning = Cleaning()
    assert cleaning.clean_text("  Hello   World  ") == "Hello World"


def test_clean_text_with_none():
    cleaning = Cleaning()
    assert cleaning.clean_text(None) is None


def test_clean_text_with_empty_string():
    cleaning = Cleaning()
    assert cleaning.clean_text("   ") is None


def test_clean_price():
    cleaning = Cleaning()
    assert cleaning.clean_price("£51.77") == 51.77


def test_clean_price_with_comma():
    cleaning = Cleaning()
    assert cleaning.clean_price("1,250.50") == 1250.50


def test_clean_price_invalid():
    cleaning = Cleaning()
    assert cleaning.clean_price("Not Available") is None


def test_clean_rating():
    cleaning = Cleaning()
    assert cleaning.clean_rating("Three") == 3


def test_clean_rating_case_insensitive():
    cleaning = Cleaning()
    assert cleaning.clean_rating("FIVE") == 5


def test_clean_rating_invalid():
    cleaning = Cleaning()
    assert cleaning.clean_rating("Unknown") is None