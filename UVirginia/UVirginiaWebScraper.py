import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

TOTALPAGES = 65

Base_url = "https://facultydirectory.virginia.edu/faculty?page="

## Create Data Frame
column_name = ['Name', 'Title', 'Email', 'Phone Number', 'Unit', 'Department']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'UViginia_Faculty_guide.csv'
i = 1

for page in range(1, TOTALPAGES+1):
    ## Get Page Content in Parent_Soup
    Parent_r = requests.get(Base_url + str(page))
    Parent_soup = BeautifulSoup(Parent_r.content, 'html.parser')

    ## Scrape Web Info
    Container = Parent_soup.find('div', attrs={'class':'results-index__results'})
    Individual_data = Container.find_all('div', attrs={'class':'searchresult__inner'})

    
    for item in Individual_data:
        Name = None
        Title = None
        Unit = None
        Phone_Number = None
        Department = None
        Email = None

        Name = item.find('h3', attrs={'class','searchresult__title'})
        Title = item.find('div', attrs={'class','searchresult__sub searchresult__p-title'})
        Unit = item.find('div', attrs={'class','searchresult__unit'})
        Department = item.find('div', attrs={'class','searchresult__dpt'})
        Phone_Number = item.find('div', attrs={'class','searchresult__phone'})
        Email = item.find('div', attrs={'class','searchresult__email'})

        try:
            name_text = Name.getText()
            name_text = name_text.strip()
        except:
            name_text = None
        try:
            title_text = Title.getText()
            title_text = title_text.strip()
        except:
            title_text = None
        try:
            unit_text = Unit.getText()
            unit_text = unit_text.strip()
        except:
            unit_text = None
        try:
            department_text = Department.getText()
            department_text = department_text.strip()
        except:
            department_text = None
        try:
            phonenumber_text = Phone_Number.getText()
            phonenumber_text = phonenumber_text.strip()
        except:
            phonenumber_text = None
        try:
            email_text = Email.getText()
            email_text = email_text.strip()
            
        except:
            email_text = None

        ## Add Data to Data Frame
        data_frame.loc[i] = [name_text, title_text, email_text, phonenumber_text, unit_text, department_text]
        print(data_frame.loc[i])
        i = i+1
        
print("Scrape Complete")
## Convert Data Frame to CSV
data_frame.to_csv(file_name, index=False)
print("Data Frame Compiled")