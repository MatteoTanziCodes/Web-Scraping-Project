import pandas as pd
import requests
from bs4 import BeautifulSoup

# URLS for main Directories
law_url = 'https://law.gsu.edu/about/directory/'

math_url = 'https://mathstat.gsu.edu/directory/'
chem_url = 'https://chemistry.gsu.edu/directory/'
comms_url = 'https://communication.gsu.edu/directory/'

edu_url = 'https://education.gsu.edu/directory/'
history_url = 'https://history.gsu.edu/directory/'
polisci_url = 'https://politicalscience.gsu.edu/directory/'

robinson_url = 'https://robinson.gsu.edu/profile/'
policy_url = 'https://aysps.gsu.edu/department/department-of-economics/'

# Create Data Frame
column_name = ['Name', 'Title', 'Email', 'Phone Number', 'Unit', 'Department', 'URL']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'GeorgiaState_Faculty_guide.csv'

# scraper for Law URL
def scraper_l(law_url, data_frame):
    law_page_content = requests.get(law_url)
    law_page_soup = BeautifulSoup(law_page_content.content, 'html5lib')
    law_container = law_page_soup.find('div', attrs={'class':'pf-content'})
    links = law_container.find_all('a', attrs={'class':'eg-invisiblebutton'})
    
    ## for each link in links, get href as prof_url, then scrape that site
    for link in links:
        prof_url = link.get('href')
        profile_scrape(prof_url, 'Law', data_frame)

# scraper for math, law and comms
def scraper_mcc(math_url, chem_url, comms_url, data_frame):
    math_page_content = requests.get(math_url)
    math_page_soup = BeautifulSoup(math_page_content.content, 'html5lib')
    math_container = math_page_soup.find('div', attrs={'class':'pf-content'})
    math_links = math_container.find_all('a')
    for link in math_links:
        math_prof_url = link.get('href')

    chem_page_content = requests.get(chem_url)
    chem_page_soup = BeautifulSoup(chem_page_content.content, 'html5lib')
    chem_container = chem_page_soup.find('div', attrs={'class':'pf-content'})
    chem_links = chem_container.find_all('a')
    for link in chem_links:
        chem_prof_url = link.get('href')

    comms_page_content = requests.get(comms_url)
    comms_page_soup = BeautifulSoup(comms_page_content.content, 'html5lib')


# scraper for education, history and polisci
def scraper_ehp(edu_url, history_url, polisci_url, data_frame):
    edu_page_content = requests.get(edu_url)
    edu_page_soup = BeautifulSoup(edu_page_content.content, 'html5lib')

    history_page_content = requests.get(history_url)
    history_page_soup = BeautifulSoup(history_page_content.content, 'html5lib')

    polisci_page_content = requests.get(polisci_url)
    polisci_page_soup = BeautifulSoup(polisci_page_content.content, 'html5lib')

# scraper for robinson and policy
def scraper_rp(robinson_url, policy_url, data_frame):
    robinson_page_content = requests.get(robinson_url)
    robinson_page_soup = BeautifulSoup(robinson_page_content.content, 'html5lib')

    policy_page_content = requests.get(policy_url)
    policy_page_soup = BeautifulSoup(policy_page_content.content, 'html5lib')

# Scrape profile for department, title, email, phone number
def profile_scrape(url, unit, data_frame):
    what = 0

# Create CSV from dataframe
def dataframe_to_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

## Function Calls
scraper_l(law_url, data_frame)
scraper_mcc(math_url, chem_url, comms_url, data_frame)
scraper_ehp(edu_url, history_url, polisci_url, data_frame)
scraper_rp(robinson_url, policy_url, data_frame)
dataframe_to_csv(data_frame, file_name)