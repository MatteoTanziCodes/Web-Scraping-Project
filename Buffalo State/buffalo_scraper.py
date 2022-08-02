from tkinter import CURRENT
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

## Create Data Frame
column_name = ['Name', 'Title', 'Phone Number', 'Department', 'Email']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Buffalo_Faculty_guide.csv'

url = 'https://www.buffalo.edu/search/search.html?query=%2BpeopleAffiliation%3AFaculty+%2BpeopleAffiliation%3Aor+%2BpeopleAffiliation%3AStaff&f.Tabs%7Cdb-people=People&searchUrl=https%3A%2F%2Fwww.buffalo.edu%2Fsearch%2Fsearch.html&collection=meta-search&sort=metapeopleLastFirstName&start_rank='

current_rank = 1
ENDRANK = 7931

def scraper(url, dataframe, current_rank, ENDRANK):

    while (current_rank != ENDRANK + 10):

        new_url = url + str(current_rank)
        
        page_content = requests.get(new_url)
        page_soup = BeautifulSoup(page_content.content, 'html5lib')
        container = page_soup.find('div', attrs={'class':'search-results-container'})
        links = container.find_all('div', attrs={'search-result search-result-people'})
        
        # get name

        # get title

        # get Phone Number

        # get Department

        # get email

        current_rank = current_rank + 10

scraper(url, data_frame, current_rank, ENDRANK)