import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
wiki = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population"
page = requests.get(wiki).text
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()
title_page = soup.title.string 
right_table = soup.find("table", {"class": 'wikitable sortable'})
list_a, list_b, list_c = [], [], []

for row in right_table.findAll('tr'):
    
    cells = row.findAll('td')
    
    # Skips rows that aren't 10 columns long (like the heading)
    if len(cells) != 12:
        continue

    # This catches when the name cells stops having a link
    #  and ends, skipping the last (summary rows)
    try:
        list_a.append(cells[2].find('a').text)
        list_b.append(cells[3].find(text=True))
        list_c.append(cells[4].find(text=True))
    except:
        break
my_df = pd.DataFrame(index = list_a)
my_df.index.name = 'State'
my_df['Population Estimate'] = list_b
my_df['Census Population'] = list_c