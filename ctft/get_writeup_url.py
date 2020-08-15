import re
from souper import souper
import inquirer
from get_event_url import find_ctf_url
from inquirer.themes import GreenPassion
from ctftime_scrape import ctftime_scraper
import asyncio
import aiohttp
import time

base = "https://ctftime.org"

async def list_writeups(name):
    
    #Find matching event
    url = await find_ctf_url(name)
    if not url:
        return
    
    names = []
    links = []
    
    print(" Accessing event writeups")    
    soup = await souper(url)


    #Get all writeup names ad number of writeups
    rows = soup.find_all("tr")
    if not rows:
        print(soup.find('div',{'class':'well'}).text)
        return  
    for row in rows[1:]:
        td = row.find_all('td')
        st = td[0].text+","+(td[3].text+" writeups").rjust(50-len(td[0].text))
        names.append((st,td[0].a['href']))
    
    #Prompt to select tasks
    questions = [
        inquirer.Checkbox('ctfs',
        message="Choose tasks for writeups(Right arrow to select)",
        choices=names)
    ]
    ans = inquirer.prompt(questions,theme=GreenPassion())
   
    #Find highest rated writeup for each task
    print(" Getting highest rated writeups")
    
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session:
        hrefs = [base+href for href in ans['ctfs']]
        writeup_soups = await asyncio.gather(*[souper(href,session) for href in hrefs])
        for writeup_soup in writeup_soups:
            rating = {}
            trs = writeup_soup.find_all("tr")
            for tr in trs[1:]:
                rat = tr.find('div').text
                if rat == "not rated":
                    rat='0'
                rating[tr.find('a')['href']] = rat
            if not rating:
                continue 
            writeup_link = max(rating, key=rating.get)
            links.append(base+writeup_link)
    
    #Scrape all writeups
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session: 
        await asyncio.gather(*[ctftime_scraper(link,session) for link in links])

    
