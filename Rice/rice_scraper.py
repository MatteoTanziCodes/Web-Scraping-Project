import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

## Create Data Frame
column_name = ['Name', 'Title', 'Unit', 'Department', 'Education']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Rice_Faculty_guide.csv'

url = 'https://ga.rice.edu/administration-faculty/faculty/'


# Scraper Algorithm
page_content = requests.get(url)
page_soup = BeautifulSoup(page_content.content, 'html5lib')

container = page_soup.find('div', attrs={'id':'textcontainer', 'class':'page_content'})
text_containers = container.find_all('p')


