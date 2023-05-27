from selenium import webdriver
from selenium.webdriver.common.by import By
import json


driver = webdriver.Chrome('C:/Users/rtribrunner/Downloads/chromedriver_win32/chromedriver.exe')

companies = ['PATH.N','MSFT.O','SSNC.OQ','NICE.OQ','APPN.A']

reports = ['balance-sheet-annual','income-annual','cash-flow-annual']
tableIdentifiers = ['Balance Sheet, annual','Income Statement, annual','Cash Flow, annual']


for company in companies:

    balance_sheet = []
    income = []
    cashFlow = []

    for i in range(3):

        driver.get('https://www.reuters.com/markets/companies/'+company+'/financials/'+reports[i])

        table = driver.find_element(By.XPATH,'//table[@aria-label="'+tableIdentifiers[i]+'"]')

        rows = table.find_elements(By.XPATH,'.//tr')

        keys = table.find_elements(By.XPATH,'.//th')

        actualReport = []

        for j in range(len(rows)-1):
            actualCell = ['NaN','NaN','NaN']
            cells = rows[j+1].find_elements(By.XPATH,".//td")
            if len(cells)==0:
                actualReport.append([keys[j+5].text,0, 0, 0])
            elif len(cells)==1:
                actualCell[0] = cells[0].text
                actualCell[0] = actualCell[0].replace("--","0")
                actualCell[0] = actualCell[0].replace("(","-")
                actualCell[0] = actualCell[0].replace(")","")
                actualCell[0] = actualCell[0].replace(",","")
                actualReport.append([keys[j+5].text,float(actualCell[0]), 0, 0])
            elif len(cells)==2:
                for k in range(2):
                    actualCell[k] = cells[k].text
                    actualCell[k] = actualCell[k].replace("--","0")
                    actualCell[k] = actualCell[k].replace("(","-")
                    actualCell[k] = actualCell[k].replace(")","")
                    actualCell[k] = actualCell[k].replace(",","")
                actualReport.append([keys[j+5].text,float(actualCell[0]), float(actualCell[1]), 0])
            else:
                for k in range(3):
                    actualCell[k] = cells[k].text
                    actualCell[k] = actualCell[k].replace("--","0")
                    actualCell[k] = actualCell[k].replace("(","-")
                    actualCell[k] = actualCell[k].replace(")","")
                    actualCell[k] = actualCell[k].replace(",","")                
                actualReport.append([keys[j+5].text,float(actualCell[0]), float(actualCell[1]), float(actualCell[2])])
        
        if i == 0:
            balance_sheet = actualReport
        elif i == 1:
            income = actualReport
        elif i == 2:
            cashFlow = actualReport
        

    financials = [company[0:4],balance_sheet,income,cashFlow]
    
    with open(company[0:4]+'.json', 'w') as outfile:
        outfile.write(json.dumps(financials))


driver.quit()