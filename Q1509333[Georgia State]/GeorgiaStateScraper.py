import pandas as pd
import requests
from bs4 import BeautifulSoup

# URLS for main Directories
page_urls = ['https://law.gsu.edu/about/directory/', 'https://mathstat.gsu.edu/directory/', 'https://chemistry.gsu.edu/directory/', 'https://communication.gsu.edu/directory/', 'https://education.gsu.edu/directory/', 'https://history.gsu.edu/directory/', 'https://politicalscience.gsu.edu/directory/', 'https://robinson.gsu.edu/profile/', 'https://aysps.gsu.edu/department/department-of-economics/']

# Create Data Frame
column_name = ['Name', 'Title', 'Email', 'Phone Number', 'Unit', 'Department', 'Education', 'URL']
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
            if('edu/profile/' in prof_url and prof_url != 'https://aysps.gsu.edu/profile/'):
                name = prof_url.split("/")[4]
                name = name.replace('-', ' ')
                unit = prof_url.split("/")[2]
                unit = unit.split(".")[0]
                if unit == "law":
                    unit = 'Law'
                elif unit == "mathstat":
                    unit = 'Math'
                elif unit == 'communication':
                    unit = 'Journalism/Communications/Media'
                elif unit == 'robinson':
                    unit = 'Business School'
                elif unit == 'education':
                    unit = 'Education'
                elif unit == 'chemistry':
                    unit = 'Chemistry'
                elif unit == 'aysps':
                    unit = 'Econ'
                elif unit == 'politicalscience':
                    unit = 'PoliSci'
                elif unit == 'history':
                    unit = 'history'
                
                print('*****************')
                print(prof_url)
                print(name)
                print(unit)
                profile_scrape(prof_url, name, unit, data_frame)
                
                
        except:
            None
    print('******************** UNIT Complete ********************')

# Scrape profile for department, title, email, phone number
def profile_scrape(url, Name, Unit, data_frame):
    child_page_content = requests.get(url)
    child_page_soup = BeautifulSoup(child_page_content.content, 'html5lib')
    
    child_container1 = child_page_soup.find('div', attrs={'class':'site-container'})
    child_container3 = child_page_soup.find('div', attrs={'class':'rainbow'})

    links = child_container1.find_all('a')
    links2 = child_container1.find_all('dl')
    links3 = child_container3.find('header')
    
    
    Phone_Number = None
    for link in links:
        prof_data = link.get('href')
        try:
            if('mailto' in prof_data or 'tel' in prof_data) :
                if('mailto' in prof_data):
                    Email = prof_data
                    print(Email)
                if('tel:' in prof_data and prof_data != 'tel:+14044132000' and Phone_Number == None):
                    Phone_Number = prof_data
                    print(Phone_Number)
        except:
            None
    
    for link in links2:
        prof_data_header = link.find('dt')
        prof_data_header = prof_data_header.getText()
        try:
            if('Education' in prof_data_header):
                data = link.find('dd')
                Education = data.getText()
                print(Education)
                
        except:
            None
    
    try:
        Title_dept = links3.getText()
        Title_dept = Title_dept.split("\n",3)[3]
        Title_dept = Title_dept.replace(u'\xa0','/')
        Title_dept = Title_dept.split('/')
        Title = Title_dept[0]
        Title = Title.strip()
        print(Title)
        Department = Title_dept[4]
        Department = Department.strip()
        print(Department)
    except:
        None
    
    dataframe_entry_point = len(data_frame) + 1
    data_frame.loc[dataframe_entry_point] = [Name, Title, Email, Phone_Number, Unit, Department, Education, url]

# Create CSV from dataframe
def dataframe_to_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)
    print("Data Frame Compiled")

## Function Call
for url in page_urls:
    scraper(url, data_frame)

dataframe_to_csv(data_frame, file_name)