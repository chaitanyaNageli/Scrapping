from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from datetime import datetime, timezone
from scrapper.session import create_session

class BooksScrapper:
    def __init__(self,url):
        self.url=url
        self.session=create_session()

    def scrape(self):
        all_books=[]

        while self.url:
            time.sleep(0.5)
            response=self.session.get(self.url)
            soup=BeautifulSoup(response.text,"html.parser")
            books=soup.find_all("article",class_="product_pod")
            
            for book in books:
                title=book.h3.a["title"]
                price=book.find("p",class_="price_color").text
                rating=book.find("p",class_="star-rating")["class"][1]
                link=urljoin(self.url,book.h3.a["href"])

                inner_response=self.session.get(link)
                inner_soup=BeautifulSoup(inner_response.text,"html.parser")

                category_data=inner_soup.find("ul",class_="breadcrumb")
                category=category_data.find_all("li")[2].text
                description_header = inner_soup.find("div", id="product_description")
                description = description_header.find_next("p").text.strip()
                

                
                new_data={
                    "source":"Books to Scrape",
                    "source_url":link,
                    "name_or_title":title,
                    "category":category,
                    "price":price,
                    "rating":rating,
                    "author":None,
                    "tags":None,
                    "description":description if description else None,
                    "scraped_at":datetime.now(timezone.utc).isoformat()
    
                }
                # print(new_data)
                
                all_books.append(new_data)
            # next=soup.find("li",class_="next")
            # if next:
            #     self.url=urljoin(self.url,next.a["href"])
            # else:
            #     self.url=None
            self.url=None
        return all_books
         
        




        


