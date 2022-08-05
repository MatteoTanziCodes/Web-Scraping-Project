from turtle import title
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import re

## Create Data Frame
column_name = ['Name', 'Title', 'department', 'Education']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Rice_Faculty_guide.csv'

url = 'https://ga.rice.edu/administration-faculty/faculty/'


# Scraper Algorithm
page_content = requests.get(url)
page_soup = BeautifulSoup(page_content.content, 'html5lib')

container = page_soup.find('div', attrs={'id':'textcontainer', 'class':'page_content'})
text_containers = container.find_all('p')

for text in text_containers:

    print("***********************************************")
    new_text = text.getText()
    if new_text != 'A B C D E  F G H I J K L M N O P Q R S T U V W X Y Z':
        # get name:
        if('\n' in new_text):
            first_line = new_text.split('\n')[0]
            second_line = new_text.split('\n')[1]
            last_name = first_line.split(',')[0]
            first_name = first_line.split(',')[1]
            name = first_name + " " + last_name

            # get title:
            title_line = re.split(r'/^\d{4}$/\.' , new_text) # split by 4 digit num
            t_array = title_line[0].split('\n')
            line = t_array[0]
            temp = re.split(r'\b(\d\d\d\d)\b', line)
            Title = temp[2].split(',')[0]
            
            # get education:
            education = t_array[1]
            
            # get department:
            if len(temp[2].split(',')) > 1:
                department = temp[2].split(',')[1]
        
        else:
            last_name = new_text.split(',')[0]
            first_name = new_text.split(',')[1]
            name = first_name + " " + last_name
        
        dataframe_entry_point = len(data_frame) + 1
        data_frame.loc[dataframe_entry_point] = [name, Title, department, education]

data_frame.to_csv(file_name, index=False)
print("Data Frame Compiled")

