from bs4 import BeautifulSoup
from ctft.souper import souper
import html2text
from ctft.formatter import formatter

async def github_scraper(url):
    soup = await souper(url)
    article = soup.find("article")
    if article:
        markdwn = formatter(article)
        return markdwn
