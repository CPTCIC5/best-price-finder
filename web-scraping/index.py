from bs4 import BeautifulSoup
import requests

url = ''
result=requests.get(url).text

doc=BeautifulSoup(result,'html.parser')
