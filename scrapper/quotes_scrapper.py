
import time

from bs4 import BeautifulSoup
from datetime import datetime,timezone
from urllib.parse import urljoin
from scrapper.session import create_session

class QuotesScrapper:
    def __init__(self,url):
        self.url=url
        self.session=create_session()

    def scrape(self):
        all_quotes=[]

        while self.url:
            time.sleep(0.5)
            response=self.session.get(self.url)
            soup=BeautifulSoup(response.text,"html.parser")
            quotes=soup.find_all("div",class_="quote")
            for quote in quotes:
                title=quote.span.text
                author=quote.find("small",class_="author").text
                tags=[]
                for tag in quote.find_all("a",class_="tag"):
                    tags.append(tag.text)
                

                new_data={
                    "source":"Quotes to Scrape",
                    "source_url":urljoin(self.url,quote.a["href"]),
                    "name_or_title":title,
                    "category":"Quotes",
                    "price":None,
                    "rating":None,
                    "author":author,
                    "tags":";".join(tags),
                    "description":None,
                    "scraped_at":datetime.now(timezone.utc).isoformat()

                    }
                all_quotes.append(new_data)
                
            next=soup.find("li",class_="next")
            if next:
                self.url=urljoin(self.url,next.a["href"])
            else:
                self.url=None
        
        return all_quotes