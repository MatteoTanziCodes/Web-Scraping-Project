from tkinter import CURRENT
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import re

## Create Data Frame
column_name = ['Name', 'Title', 'Department', 'Education']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Emory_Faculty_guide.csv'
url = 'http://catalog.college.emory.edu/department-program/faculty.php'

page_content = requests.get(url, timeout=10)
page_soup = BeautifulSoup(page_content.content, 'html5lib')
container = page_soup.find('div', attrs={'class':'tab-content'})
links = container.find_all('div', attrs={'class':'faculty well'})

for link in links:
    try:
        name = link.find('span', attrs={'class':'faculty-name'})
        name = name.getText()
    except:
        name = ''
    
    try:
        education_array = []
        education_header = link.find('dl', attrs={'class':'dl-horizontal faculty-education'})
        educations = education_header.find_all('dd')
        for education_text in educations:
            education_array.append(education_text.getText())
        education = '\n'.join(education_array)
    except:
        education = ''

    try:
        title = link.find('li', attrs={'class':'title'})
        title = title.getText()
    except:
        title = ''
    
    try:
        department_array = []
        department_header = link.find('dl', attrs={'class':'dl-horizontal faculty-department'})
        departments = department_header.find_all('dd')
        for department_text in departments:
            department_array.append(department_text.getText())
        department = '\n'.join(department_array)
    except:
        department = ''
    
    dataframe_entry_point = len(data_frame) + 1
    data_frame.loc[dataframe_entry_point] = [name, title, department, education]

data_frame.to_csv(file_name, index=False)
print("Data Frame Compiled")