import pandas as pd

df = pd.read_csv('projects_raw.csv')

# Dropping null values
df = df.dropna(subset=df.columns.values)

# Dropping invalid years and changing data type
df['year'] = df['year'].astype('int')
df = df.loc[(df.year >1900) & (df.year < 2030)]

# Dropping non-projects
df = df.loc[~df['title'].str.contains('Classic')]

# Spliting column
df[['project_name', 'architect']] = df['title'].str.split(' / ', 1, expand=True)

# Filtering pojects without the city and dropping those without location
only_country = df.loc[~df['location'].str.contains(', ')]
only_country = only_country.loc[~only_country['location'].str.contains('0')]
only_country['country'] = only_country['location']

# Spliting column and joining datasets back together
df = df.loc[df['location'].str.contains(', ')]
df[['city', 'country']] = df['location'].str.split(', ', 1, expand=True)
df = pd.concat([df, only_country])

# Cleaning publication date format (removing hours)
df['publication_date'] = df['publication_date'].str.split('T').str[0]

# Ordering columns
df = df[['project_name', 'architect', 'year', 'country', 'city', 'publication_date', 'project_id']]
df = df.sort_values(by='publication_date', ascending=False)

# Saving clean data to csv
df.to_csv('projects.csv', index=False)

print(df)