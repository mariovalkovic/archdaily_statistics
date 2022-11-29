import requests
import pandas as pd

# Defining API endpoint and known parameters
endpoint = 'https://www.archdaily.com/search/api/v1/us/projects?page='
page = '1'
pages = 833

# API request
def main_request(endpoint, page):
    r = requests.get(endpoint + f'{page}')
    return r.json()

# Saving selected parameters from json into a list of dictionaries
def parse_json(response):
    dictionary = []
    for item in response['results']:
        dict_entry = {
        'title': item['title'],
        'year': item['year'],
        'location': item['location'],
        'project_id': item['document_id'],
        'publication_date': item['publication_date'],
        }
        dictionary.append(dict_entry)
    return dictionary

# Scraping
mainlist = []
data = main_request(endpoint, page)
for page in range(1, pages+1):
    print(page)
    mainlist.extend(parse_json(main_request(endpoint, page)))

# Pandas data frame and saving csv
df = pd.DataFrame(mainlist)
df.to_csv('projects_raw.csv', index=False)