import requests

url_template = 'https://wttr.in/{}?m?M?n?qTqu&lang=ru'
url = url_template.format('london')
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = url_template.format('cherepovec')
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = url_template.format('sheremetievo')
response = requests.get(url)
response.raise_for_status()
print(response.text)
