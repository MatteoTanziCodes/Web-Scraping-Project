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

# scraper for math, law and comms
def scraper_mcc(math_url, chem_url, comms_url, data_frame):
    math_page_content = requests.get(math_url)
    math_page_soup = BeautifulSoup(math_page_content.content, 'html5lib')

    chem_page_content = requests.get(chem_url)
    chem_page_soup = BeautifulSoup(chem_page_content.content, 'html5lib')

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
    edu_page_content = requests.get(edu_url)
    edu_page_soup = BeautifulSoup(edu_page_content.content, 'html5lib')

    history_page_content = requests.get(history_url)
    history_page_soup = BeautifulSoup(history_page_content.content, 'html5lib')

    polisci_page_content = requests.get(polisci_url)
    polisci_page_soup = BeautifulSoup(polisci_page_content.content, 'html5lib')

def dataframe_to_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

## Function Calls
scraper_l(law_url)
scraper_mcc(math_url, chem_url, comms_url)
scraper_ehp(edu_url, history_url, polisci_url)
scraper_rp(robinson_url, policy_url)
dataframe_to_csv(data_frame, file_name)