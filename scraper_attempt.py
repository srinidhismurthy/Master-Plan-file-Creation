from utilities.read_xls import read_xl
from bs4 import BeautifulSoup
import requests
import lxml
from base.meothods import MyDriver as MD


from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
from page.AlLogin import ALoginPage as AL

Regresssion_test={'Regression: Reports_RegressionTest1_Filters_SCTM (34 Machines)': ['103241', '103245', '103255', '103257', '103259', '103261', '103263', '103264', '103266', '103268', '103270', '103272', '103247', '103275', '103277', '103279', '103281', '103283', '103284', '103286', '103250', '103252', '103287', '103242', '103294', '103243', '103309', '103310', '103311', '103312', '103313', '103314', '103315', '103316']}
LoginURL = "http://silkcentral.intuit.com/login"
IDURL="http://silkcentral.intuit.com/silk/DEF/TM/Execution?nEx={}&execView=execDetails&view=details&pId=540&nTP=1521775&etab=1"

driver=webdriver.Firefox()
driver.get(LoginURL)
driver.maximize_window()
driver.implicitly_wait(30)
for suite,id in Regresssion_test.items():
    for Mid in id:
        if Mid=="103241":
            source=requests.get(IDURL.format(Mid)).text
            print(source)


# soup=BeautifulSoup.find_all(source,'lxml')
# text=soup.text
# print(text)

