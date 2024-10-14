import requests

url_template = 'https://wttr.in/{}?m?M?n?qTqu&lang=ru'
citys = 'london', 'cherepovec', 'sheremetievo'

for city in citys:
    url = url_template.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
