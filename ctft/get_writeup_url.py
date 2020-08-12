import re
from souper import souper
import inquirer
from get_event_url import find_ctf_url
from inquirer.themes import GreenPassion
from ctftime_scrape import ctftime_scraper
import asyncio

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
        names.append((td[0].text+","+td[3].text+" writeups",td[0].a['href']))
    
    #Prompt to select tasks
    questions = [
        inquirer.Checkbox('ctfs',
        message="Choose tasks for writeups(Right arrow to select)",
        choices=names)
    ]
    ans = inquirer.prompt(questions,theme=GreenPassion())
    #Find highest rated writeup for each task
    print(" Getting highest rated writeups")
    hrefs = [base+href for href in ans['ctfs']]
    print(hrefs)
    writeup_soups = [souper(href) for href in hrefs ]
    for writeup_soup in asyncio.as_completed(writeup_soups):
        task_list = await writeup_soup
        rating = {}
        trs = task_list.find_all("tr")
        for tr in trs[1:]:
            rat = tr.find('div').text
            if rat == "not rated":
                rat='0'
            rating[tr.find('a')['href']] = rat
        writeup_link = max(rating, key=rating.get)
        links.append(base+writeup_link)
    
    #Scrape all writeups
    scrape = [ctftime_scraper(link) for link in links]
    for s in asyncio.as_completed(scrape):
        await s

    
