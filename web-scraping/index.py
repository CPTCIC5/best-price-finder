from bs4 import BeautifulSoup
import requests

url = 'https://timesofindia.indiatimes.com/'
result=requests.get(url).text
print(result)
doc=BeautifulSoup(result,'html.parser')

