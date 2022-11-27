import requests
import pandas as pd

endpoint = 'https://www.archdaily.com/search/api/v1/us/projects?page='
page = '1'
pages = 833

def main_request(endpoint, page):
    r = requests.get(endpoint + f'{page}')
    return r.json()

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

mainlist = []
data = main_request(endpoint, page)
for page in range(1, pages+1):
    print(page)
    mainlist.extend(parse_json(main_request(endpoint, page)))

df = pd.DataFrame(mainlist)
df.to_csv('projects_raw.csv', index=False)

# print(len(mainlist))
# print(df.head())