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


#1 Read the Suite details from column 4 in Suits.xls.
Suite_Names_list= read_xl("Suits.xls","Sheet2",1)
Suite_Id=read_xl("Suits.xls","Sheet2",0)

URL_WO_ID="http://autolab.corp.intuit.net/autolab/task/DeploymentPlanView.php?id="
URL_List=[]

for ID in Suite_Id:
    ID=str(ID)
    ID=ID.split(".")[0]
    URL=URL_WO_ID+"{}".format(ID)
    URL_List.append(URL)

driver=webdriver.Firefox()
driver.get(URL_List[0])
driver.implicitly_wait(30)
sleep(120)
text=driver.page_source
suitename_machineID={}
machineID = re.findall('\d{5,7}', text)
#machineIDStr = [str(x).replace('::', "") for x in machineID]
suitename_machineID[Suite_Names_list[0]] = machineID
# with open("mapped.txt", 'w')as mapping:
#     mapping.write(Suite_Names_list[0]+"\n")
#     str1 = ','.join(machineIDStr)
#     mapping.write(str1+"\n")
#     mapping.write("************************"+"\n")
print(Suite_Names_list[0], "\n")
print(Suite_Names_list[0],len(machineID))
print(machineID)
print("#########################################################################","\n")

for i in range(1,len(URL_List)):
    driver.get(URL_List[i])
    sleep(5)
    text=driver.page_source
    machineID=re.findall('\d{5,7}', text)
    #machineIDStr = [str(x).replace('::', "") for x in machineID]
    suitename_machineID[Suite_Names_list[i]] = machineID
    print(Suite_Names_list[i], "\n")
    print(Suite_Names_list[i], len(machineID))
    print(machineID)
    print("#########################################################################", "\n")


    # with open("mapped.txt", 'w')as mapping:
    #     mapping.write(Suite_Names_list[i]+"\n")
    #     str1 = ','.join(machineIDStr)
    #     mapping.write(str1+"\n")
    #     print(Suite_Names_list[i],"\n")
    #     print(str1, "\n")
    #     print("#########################################################################","\n")
print(suitename_machineID)





















