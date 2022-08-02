import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

## Create Data Frame
column_name = ['Name', 'Title', 'Phone Number', 'Department', 'Email']
data_frame = pd.DataFrame(columns=column_name)
file_name = 'Buffalo_Faculty_guide.csv'

url = 'https://www.buffalo.edu/search/search.html?query=%2BpeopleAffiliation%3AFaculty+%2BpeopleAffiliation%3Aor+%2BpeopleAffiliation%3AStaff&f.Tabs%7Cdb-people=People&searchUrl=https%3A%2F%2Fwww.buffalo.edu%2Fsearch%2Fsearch.html&collection=meta-search&sort=metapeopleLastFirstName&start_rank=1'

start_rank = 1
