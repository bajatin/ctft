from bs4 import BeautifulSoup
from ctft.souper import souper
import html2text
import re
from ctft.formatter import formatter
from ctft.github_scrape import github_scraper
import os

home = os.getenv("HOME")
path = os.path.join(home,"ctft_writeups")


async def ctftime_scraper(url,session):
    print("Parsing {}".format(url))
    soup = await souper(url,session)
    
    #Make event directory
    ul = soup.find('ul',{'class':'breadcrumb'})
    if not ul:
        print("No ul"+url)
    li = ul.find_all('li')
    d = os.path.join(path,li[2].text)
    if not os.path.exists(d):
        os.mkdir(d)
    os.chdir(d)

    #Writeup content
    container = soup.find_all("div",{"class":"container"})[1]

    #Configure html2text
    h = html2text.HTML2Text()
    h.ignore_links = False

    #Write headings and tags to file
    heading = container.find('div',{'class':'page-header'})
    f = open(heading.h2.text.strip(),"w")
    head = heading.prettify()
    f.write(h.handle(head))
    f.write("\n")

    tags = container.find('div',{'class':'span7'})
    t = tags.prettify()
    f.write(h.handle(t))
    f.write("\n")

    #Find writeup content and format it
    writeup_html = soup.find_all('div',{'class':'well'})
    if len(writeup_html) > 1:
        f.write(h.handle(writeup_html[-1].prettify()))
    
    f.close()
    if writeup_html[-1].a:
        if re.match('https?:\/\/github.com\/.*',writeup_html[-1].a['href']):
            markdwn = await github_scraper(writeup_html[-1].a['href'])
        else:
            markdwn = formatter(writeup_html[0])
    elif re.search("Original writeup",writeup_html[0].text) and re.match('https?:\/\/github.com\/.*',writeup_html[0].a['href']):
        markdwn = await github_scraper(writeup_html[0].a['href'])
    else:
        markdwn = formatter(writeup_html[0])
    
    #Save data in a file
    f = open(heading.h2.text.strip(),"a")
    if markdwn:
        f.write(markdwn)
    f.close()
    print("Writeup for {} saved in {}".format(heading.h2.text.strip(),d))
    
