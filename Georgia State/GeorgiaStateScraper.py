import pandas as pd
import requests
from bs4 import BeautifulSoup

# URLS for main Directories
page_urls = ['https://law.gsu.edu/about/directory/', 'https://mathstat.gsu.edu/directory/', 'https://chemistry.gsu.edu/directory/', 'https://communication.gsu.edu/directory/',
'https://education.gsu.edu/directory/', 'https://history.gsu.edu/directory/', 'https://politicalscience.gsu.edu/directory/', 'https://robinson.gsu.edu/profile/', 'https://aysps.gsu.edu/department/department-of-economics/']

# Create Data Frame
column_name = ['Name', 'Title', 'Email', 'Phone Number', 'Unit', 'Department', 'URL']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'GeorgiaState_Faculty_guide.csv'

def scraper(url ,dataframe):

    page_content = requests.get(url)
    page_soup = BeautifulSoup(page_content.content, 'html5lib')
    container = page_soup.find('div', attrs={'class':'site-container'})
    links = container.find_all('a')
    for link in links:
        prof_url = link.get('href')
        try:
            if('edu/profile/' in prof_url and prof_url is not 'https://aysps.gsu.edu/profile/'):
                print(prof_url)
        except:
            None

# Scrape profile for department, title, email, phone number
def profile_scrape(url, unit, data_frame):
    what = 0

# Create CSV from dataframe
def dataframe_to_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

## Function Calls
for url in page_urls:
    scraper(url, data_frame)

dataframe_to_csv(data_frame, file_name)