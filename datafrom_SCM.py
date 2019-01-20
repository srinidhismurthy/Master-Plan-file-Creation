from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import re
from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
from base.meothods import MyDriver
from selenium.webdriver.common.by import By

#suitename_machineID_old = {'CBT ConsolidatedSCTM(31machines)': ['70386', '70387', '70388', '70389', '70390', '70391', '70471', '70472', '70473', '70474', '70475', '70476', '70477', '70478', '70479', '70480', '70481', '70482', '70483', '70484', '70485', '70486', '70487', '70488', '70489', '70490', '70491', '70492', '93525', '70495', '70494'], 'CBT Consolidated2SCTM(24machines)': ['70496', '70497', '70498', '70502', '70503', '70504', '70505', '70506', '70508', '70510', '70511', '70512', '70516', '70517', '70518', '70519', '70520', '70521', '70522', '70523', '70524', '70525', '70526', '70527'], 'QBE2ERegressionTests_SetUpConfigUtilities': ['68929', '68930', '68931', '68932', '68933', '68934', '68935', '68936', '68937', '68938', '68939', '68940', '68941', '68942', '68943', '68944', '68945', '68946', '68947', '68948', '68949', '68950', '68951', '68916', '68917', '68919', '68920', '68921'], 'QBE2ERegressionTests_BankingFinancialsServices (Ruby Onwards)': ['68893', '68894', '68896', '68897', '68901', '68903', '68904', '68905', '68906'], 'QBE2ERegressionTests_MoneyIn_MoneyOut_AssetMgmt(Ruby onwards)': ['69255', '69324', '69325', '69326', '69327', '69328', '69329', '69330', '69333', '69334', '69338', '69339', '69340', '69341', '69335', '69336', '69337'], 'QBE2ERegressionTests_DelightersSaveTransaction': ['68908', '68909', '68910', '68911', '68912'], 'QBBranchTests_BankingAccouting - Ruby onwards (14Machines)': ['69265', '69259', '69260', '69261', '69262', '69263', '69264', '69266', '69267', '69268', '69269', '69270', '69271', '69272'], 'QBBranchTests_MoneyInMoneyOutReportsAddons (7 Machines)': ['69352', '69353', '69354', '69355', '69356', '69357', '69360', '69362', '69364'], 'SCTM_INTL_QBBranchTests_FileOpsSetupConfigUtilities': ['70314', '70316', '70325', '70326', '70327', '70328', '70329'], 'FileOps-DataDriven(7 Machines)': ['88233', '88234', '88235', '88231', '88232', '88230', '93365', '93366', '93367', '111845'], 'Regression: Reports_RegressionTest1_Filters (48 Machines)': [], 'QB Mainstreet: Links_AP_1 (41 Machines)': ['70225', '70227', '70228', '70229', '70230', '70231', '70210', '70212', '70213', '70214', '70215', '70222', '70223', '70224', '70216', '70217', '70218', '70219', '70220', '70221', '70797', '70798', '70799', '70800', '70801', '70802', '70803', '70804', '70805', '70806', '70807', '70808', '70809', '73503', '70811', '70812', '70813', '70814', '70815', '70816', '73126'], 'QB Mainstreet: Links_AP_2 (17 Machines)': ['73127', '73144', '73149', '73151', '73153', '73152', '73229', '73230', '73231', '73232', '73233', '73234', '73526', '73527', '73528', '73529', '73530'], 'QB Mainstreet: Links_AR_1 (45 Machines)': ['73561', '73569', '73570', '73571', '73572', '73573', '73664', '73665', '73666', '73667', '73668', '73669', '73670', '73671', '73672', '76954', '76948', '76815', '76816', '76817', '73576', '73578', '76799', '76800', '76801', '76804', '73673', '73674', '73675', '73676', '73677', '73678', '73679', '73680', '73681', '73682', '73683', '73684', '76824', '76825', '76826', '76827', '76828'], 'QB Mainstreet: Links_AR_2 (46 Machines)': ['76829', '76830', '76831', '76832', '76833', '76834', '76835', '76836', '76837', '76903', '76904', '76905', '76919', '76921', '76926', '76928', '76805', '76806', '76811', '76812', '76813', '76814', '76818', '76819', '74684', '76759', '76761', '76762', '76764', '76788', '76789', '76790', '76791', '76792', '76793', '76794', '76795', '76796', '76797', '76798', '76931', '76934', '76820', '76821', '76822', '76823'], 'QB Accountant: CDR_ACforVenti (1 Machine)': ['69847'], 'QB Accountant: CDR Unlinked Transactions': ['75376'], 'QB Accountant: CDR Unlinked Transactions MC': ['69935', '74370'], 'Optimized_QB Accountant: Legacy_consolidated_(27 Machines)': ['103640', '103643', '103644', '103645', '103642', '103652', '103647', '103648', '103733', '103734', '103646', '103650', '103651', '103735', '103744', '103745', '103736', '103737', '103738', '103739', '103740', '103741', '103742', '103743', '103649', '103654', '103655'], 'Optimized_QB Accountant: BatchEnter Transactions(23 Machines)': ['101654', '101663', '101657', '101658', '101659', '101660', '101661', '101662', '101748', '101749', '101750', '101751', '101752', '101738', '101739', '101740', '101741', '101742', '101743', '101744', '101745', '101746', '101747'], 'Optimized_QB Accountant: BatchEnter Transactions1(12 Machines)': ['108105', '108106', '108091', '108104', '110064', '110065', '110066', '112142', '112141', '112049', '112144', '114179', '114180', '114181'], 'QB Accountant: Starter File (1 Machine)': ['69929'], 'Optimized_QB Accountant: DataExchange_consolidated (41 Machines)': ['104272', '104247', '104285', '104261', '104262', '104263', '104264', '104273', '104274', '104275', '104276', '104251', '104252', '104253', '104254', '104269', '104277', '104278', '104255', '104256', '104257', '104258', '104259', '104260', '104279', '104280', '104281', '104282', '104248', '104378', '104380', '104249', '104250', '104284', '104283', '104270', '104271', '104265', '104266', '104267', '104268'], 'QB Accountant: Accountant Center (1 Machine)': ['70114'], 'Transaction_copyline_pasteline(5 machines)': ['90021', '90022', '90023', '90024', '90025'], 'MemorisedTransaction': ['98685', '98686'], 'QBFeatures_Core_Batch_Invoice': ['100164', '100167', '100952', '101385'], 'QBFeatures_QAD_Global(3 Machines)': ['109444', '109445', '109544'], 'EmailRevamp(4 Machine)': ['90029', '90030', '90031', '90032'], 'LuceneSearch(3Machines)': ['90007', '90008', '90009'], 'BatchTimeSheet(1 Machine)': ['93669'], 'BillPaymentStubFeature': ['93036', '93037', '93038', '93039', '93040', '93041', '93078'], 'Fit_to_Height': ['90067', '90069'], 'QBFeatures_TransactionLinkingTypes(12 Machines)': ['110665', '110666', '110667', '110668', '110669', '110670', '110671', '110672', '110673', '110674', '110675', '110676', '110867', '110865', '110864'], 'QBFeatures_BuildAssembly(2 machines)': ['111784', '111786'], 'QBFeatures_ReportsSanity(2 Machines)': ['114184', '114185'], 'QBFeatures_QBSearch(1 Machine)': ['112047'], 'QB ES : EnterprisePermissions1 RubyOnwards(4 Machines)': ['126752', '126753', '126754', '126755'], 'QB : Core Permissions (16 Machines)': ['126875', '126876', '126877', '126878', '126879', '126880', '126881', '126882', '126883', '126884', '126885', '126886', '126887', '126888', '126889', '126890'], 'All Inventory Smoke Tests (1 Machine)': ['69370', '69371', '69372', '69373', '69374'], 'WriteOffInvoice(4 Machines)': ['97971', '97972', '97973', '97974'], 'QB Multicurrency_Sales_Regression (4 Machine)': ['125857', '125858', '125859', '125860', '125861', '125862', '125863', '125864'], 'QB Multicurrency_Setup_Regression': ['126751'], 'QB Multicurrency_Lists_Regression (3 Machine)': ['126757', '126758', '126759'], 'QB ES LotNumber (MLI 1 Machine)': ['126750'], 'QB ES FIFO Cost Lot History Report (MLI 1 Machine)': ['80322'], 'QB ES PriceMarkup (1 Machine)': ['126749'], 'QB ES PurchasingImprovements (MLI 1Machine)': ['48382'], 'QB ES RowShelfBin (MLI 1 Machine)': ['64742'], 'QB ES Security Enhancement (1 Machine)': ['69385'], 'QB ES SerialNumber (MLI 1 Machine)': ['126747', '126748'], 'QB ES Barcode Scanning (MLI 1 machine)': ['64744', '126404'], 'QB ES FIFO (MLI 1 machine)': ['126746'], 'QB ES Hide Zero QOH (MLI 1 Machine)': ['38553'], 'QB ES List Limit Increases (1 machine)': ['48046'], 'QB ES InventoryCenter (1 machine)': ['126742'], 'QB ES MLI_BlazeAndLater (MLI 3 machines)': ['126743', '126744', '126745'], 'QB ES JobCosting(4 Machines)': ['82764', '82765', '82766', '82767'], 'QB ES Reorder Qty (1 Machine)': ['81208'], 'QB ES BuildAssemblyImprovements (1 Machine)': ['71544'], 'QBFeatures_CBT_MoneyInOut_Txns(5 machines)': ['122025', '122026', '122027', '122191', '122192'], 'CBT_Features_ SimpleFindAndAdvanceFind (1 Machine)': ['121952'], 'QBFeatures_BatchTimesheet_ BatchTimeExpense(4 Machines)': ['122194', '122195', '122197', '122196'], 'CBT_Feature_MLI ( 1 Machine )': ['122083'], 'CBT_Feature_SplitEIR (1 Machine)': ['122236'], 'CBT_Feature_PriceMarkup (1 Machine)': ['122085'], 'CBT_Feature_FiFo (5 Machine)': ['122435', '122881', '122882', '122883', '122884'], 'CBT_Feature_SalesTaxTesting (3 Machines)': ['122029', '122077', '122078'], 'CBTFeatures_SampleFile ( 1 Machine)': ['122262'], 'CBT_Feature_Sendforms_RegressionTC(4 Machines)': ['122429', '122430', '122431', '122432'], 'QBFeatures_QB_Todo': ['119815', '122513', '122512'], 'QBFeature_CompanyFileCreation (1Machine)': ['121822'], 'CBT_Feature_ToggleAndSwitch (6 Machine)': ['122244', '122888', '122889', '122890', '122891', '122892'], 'CBT Features_EmployeeCenter ( 1 Machine )': ['122493'], 'CBT Features_VendorCenter (2 Machines)': ['121774', '121775'], 'CBTFeatures_CustomerCenter (2 machines)': ['121948', '121949'], 'CBT_Features_InventoryCenter ( 1 Machine)': ['122317'], 'QBFeatures_QBAllMenuInvoke(3 Machines)': ['119615', '119618', '119617'], 'QBFeatures_QBInventoryAllMenuInvoke(1 Machine)': ['119616'], 'CBT_Features_IconBar': ['119558'], 'CBT_Feature_ShippingManager (4 Machine)': ['122682', '122887', '122886', '122885'], 'CBT_Feature_StarterFile (1 Machine)': ['122437'], 'CBTFeatures_RapidData(2 Machines)': ['123091', '123092']}
#suitename_machineID
dummy = {'CBT_Feature_Sendforms_RegressionTC(4 Machines)': ['122430','70386']}

LoginURL = "http://silkcentral.intuit.com/login"

################################# Locators##############################
search = '//input[@id="search"]'

searched_id_link = "//div[contains(text(),'{}')]//parent::td//following-sibling::td[1]//a" # format with Machine ID

Assigned_Test_Tab = "//span[contains(text(),'Assigned Tests')]"

Assigned_tests = "//a[starts-with(@title,'Go to Test')]" # Find elemnts

Execution_plan = "//a[starts-with(@title,'Go to Execution Plan')]"

###############################Locators##########################


driver=webdriver.Firefox()
driver.get(LoginURL)
driver.implicitly_wait(30)
driver.maximize_window()
MD = MyDriver(driver)
sleep(30)
maindict = {}
idToPath = {}
pathlist = []

#####################SCTM search action #######################################
#for sName,Mids in suitename_machineID.items():
for sName, Mids in dummy.items():
    for id in Mids:

        print(sName)
        print(id)
        #Get the URL for eachID
        IDURL="http://silkcentral.intuit.com/silk/DEF/TM/Execution?nEx={}&execView=execDetails&view=details&pId=540&nTP=1521775&etab=1"
        iDURLF=IDURL.format(id)
        driver.get(iDURLF)
        sleep(8)
        assigned_tests = driver.find_elements_by_xpath(Assigned_tests)

        if len(assigned_tests) == 1:
            newURL = driver.find_element_by_xpath(Assigned_tests).get_attribute('href')
            driver.get(newURL)
            sleep(8)
            try:
                pathlist.clear()
                element = driver.find_element_by_xpath(
                    '//td[contains(@class,"defaulttablecell")and contains(text(),":")]')
                text = element.text

                print(text)
                pathlist.append(text)
                print(pathlist)

                idToPath[id] = pathlist
                print(idToPath)
                maindict[sName] = idToPath
                print(maindict)
                print("************" * 5)


            except:
                print("Could not find the path for the id {}".format(id))

            #idToPath[id] = pathlist
        elif len(assigned_tests)>1:
            pathlist.clear()
            for i in range(0,len(assigned_tests)):
                assigned_tests_new=driver.find_elements_by_xpath(Assigned_tests)
                newURL=assigned_tests_new[i].get_attribute('href')
                driver.get(newURL)
                sleep(8)
                try:
                    #element = driver.find_element_by_xpath(
                    #  '//td[contains(@class,"defaulttablecell")and contains(text(),":")]')
                    element = MD.explicitWait(By.XPATH,'//td[contains(@class,"defaulttablecell")and contains(text(),":")]')
                    text = element.text
                    print(text)
                    pathlist.append(text)
                    driver.get(iDURLF)
                    sleep(8)
                except:
                    print("Cound not find the path for the id {}".format(id))

            print(pathlist)
            idToPath[id] = pathlist
            print(idToPath)
            print("********"*20)
        maindict[sName] = idToPath
print(maindict)
driver.close()



# # text=driver.page_source
# # match=re.findall(r">C:\\QAP\\silkscripts\\.(<)$" , text)
# # print(match)
# try:
#     element = driver.find_element_by_xpath('//td[contains(@class,"defaulttablecell")and contains(text(),"C:")]')
#     text = element.text
#     print(text)
# except:
#     element = driver.find_element_by_xpath('//td[contains(@class,"defaulttablecell")and contains(text(),"c:")]')
#     text = element.text
#     print(text)
#
#
# # for key,values in suitename_machineID.items():
# #     for i in values:
# #         driver.get("http://silkcentral.intuit.com/silk/DEF/TM/Test+Plan?nEx={}&execView=execDetails&view=details&pId=540&nTP=1135811&etab=1".format(i))
# #         text=driver.page_source
# #         path=re.findall("^C:\\\\QAP.(t|pln)$",text)


















