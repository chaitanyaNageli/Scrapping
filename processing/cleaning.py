import re

class Cleaning:
    def __init__(self):
        self.RATING_MAP = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

    def clean_text(self,value):
        if value is None:
            return None
        
        text = " ".join(value.replace("\x80", " ").split()) 
        return text or None                                   

    def clean_price(self,raw):
        if not raw:
            return None
        match = re.search(r"\d+(?:\.\d+)?", raw.replace(",", ""))
        return float(match.group()) if match else None

    def clean_rating(self,raw):
        for word in (raw or "").lower().split():
            if word in self.RATING_MAP:
                return self.RATING_MAP[word]
        return None