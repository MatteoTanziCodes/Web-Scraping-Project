from tkinter import CURRENT
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import re

## Create Data Frame
column_name = ['Name', 'Title', 'Phone Number', 'Department', 'Email']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Buffalo_Faculty_guide.csv'

url = 'https://www.buffalo.edu/search/search.html?query=%2BpeopleAffiliation%3AFaculty+%2BpeopleAffiliation%3Aor+%2BpeopleAffiliation%3AStaff&f.Tabs%7Cdb-people=People&searchUrl=https%3A%2F%2Fwww.buffalo.edu%2Fsearch%2Fsearch.html&collection=meta-search&sort=metapeopleLastFirstName&start_rank='

current_rank = 1
ENDRANK = 7931

def scraper(url, dataframe, current_rank, ENDRANK):

    num = 1
    while (current_rank != ENDRANK + 10):

        new_url = url + str(current_rank)
        try:
            page_content = requests.get(new_url, timeout=10)
        except:
            None
        page_soup = BeautifulSoup(page_content.content, 'html5lib')
        container = page_soup.find('div', attrs={'class':'search-results-container'})
        links = container.find_all('div', attrs={'search-result search-result-people'})

        for link in links:
            text = link.getText()
            text = text.replace("\n","")
            text = re.split(r'\s{2,}', text)

            # get name
            name = text[1]

            # get title
            title = text[2]

            # get Department
            department = text[3]

            # get email and phone
            for x in range(len(text)):
                if "@buffalo.edu" in text[x]:
                    email = text[x]
                if "716" in text[x]:
                    phone_num = text[x]

            print("person complete")
            dataframe_entry_point = len(data_frame) + 1
            data_frame.loc[dataframe_entry_point] = [name, title, phone_num, department, email]
        
        current_rank = current_rank + 10
        print("page: " + str(num) + " complete, Rank:" + str(current_rank))
        num = num + 1
            
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

scraper(url, data_frame, current_rank, ENDRANK)