from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html


source=requests.get("http://silkcentral.intuit.com/silk/DEF/TM/Test+Plan?nEx=110665&execView=execDetails&view=details&pId=540&nTP=1400050&etab=1").text

soup=BeautifulSoup.find_all(source,'lxml')
text=soup.text
print(text)

