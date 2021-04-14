from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class Scrape:

    def __init__(self):
        pass

    def scrape_news(self):
        news_list = []
        req = Request('https://www.theblockcrypto.com/', headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        bs = BeautifulSoup(html, 'html.parser')
        
        storyfeed = bs.find("div", class_="storyFeed").find_all("article")
        
        for story in storyfeed:
            title = story.find("div", class_="align-items-start").h3.text
            description = story.find("div", class_="align-items-start").div.text
            
            news_list.append({"title": title, "description": description})
        
        return news_list