import requests


payload = {'m': '', 'M': '', 'n': '', 'q': '', 'Tqu&lang=': 'ru'}
url_template = ('https://wttr.in/{}')
cities = 'london', 'cherepovec', 'sheremetievo'

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
