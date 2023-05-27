import json
import csv
import numpy as np

header = {'S&P':'S&P500','LowCode':'Low-code','Income':'Net Income','OpIncome':'Operating Income','R&D':'Research & Development','Rev':'Revenue','CapEx':'Capital Expenditures','Goodwill':'Goodwill, Net','Intangibles':'Intangibles, Net'}
features = ['S&P500','Low-code','APPN - Research & Development','APPN - Revenue','APPN - Capital Expenditures','APPN - Intangibles','MSFT - Research & Development','MSFT - Revenue','MSFT - Capital Expenditures','MSFT - Intangibles','NICE - Research & Development','NICE - Revenue','NICE - Capital Expenditures','NICE - Intangibles','PATH - Research & Development','PATH - Revenue','PATH - Capital Expenditures','PATH - Intangibles','SSNC - Research & Development','SSNC - Revenue','SSNC - Capital Expenditures','SSNC - Intangibles','RPA market size']
avgFeatures = ['S&P500','Low-code',header['Intangibles'],header['R&D'],header['CapEx'],header['Rev'],'RPA market size']
featureNumber = len(features)
features = [features,np.zeros(featureNumber),np.zeros(featureNumber),np.zeros(featureNumber)]
avgFeatures = [[header['S&P'],header['LowCode'],'Intangibles',header['R&D'],header['Rev'],header['CapEx'],'RPA market size'],[3756,14311,0,0,0,0,2389],[4766,14311,0,0,0,0,2854],[3839,22869,0,0,0,0,3352]]

featureDictionary = {
    'R&D':0,
    'Revenue':1,
    'CapEx': 2,
    'Intangibles': 3,
}

companyDictionary = {
    'APPN': 2,
    'MSFT': 6,
    'NICE': 10,
    'PATH': 14,
    'SSNC': 18
}

companies = ['PATH','MSFT','SSNC','NICE','APPN']

features[1][0] = 3756 #S&P
features[2][0] = 4766
features[3][0] = 3839
features[1][1] = 14311 #Low-code
features[2][1] = 18497
features[3][1] = 22869





for company in companies:

    with open('./data-mining-trend/raw-data/'+company+'.json', 'r') as f:
        data = json.load(f)

    startingPoint = companyDictionary[company]

    for balanceItem in data[1]:
        if(balanceItem[0]==header['Intangibles']):
            features[1][companyDictionary[company]+featureDictionary['Intangibles']]= balanceItem[3] 
            features[2][companyDictionary[company]+featureDictionary['Intangibles']]= balanceItem[2] 
            features[3][companyDictionary[company]+featureDictionary['Intangibles']]= balanceItem[1]  
    for incomeItem in data[2]:
        if(incomeItem[0]==header['R&D']):
            features[1][companyDictionary[company]+featureDictionary['R&D']]= incomeItem[3] #2020
            features[2][companyDictionary[company]+featureDictionary['R&D']]= incomeItem[2] #2021
            features[3][companyDictionary[company]+featureDictionary['R&D']]= incomeItem[1] #2022
        elif(incomeItem[0]==header['Rev']):
            features[1][companyDictionary[company]+featureDictionary['Revenue']]= incomeItem[3] 
            features[2][companyDictionary[company]+featureDictionary['Revenue']]= incomeItem[2] 
            features[3][companyDictionary[company]+featureDictionary['Revenue']]= incomeItem[1] 
    for cashflowItem in data[3]:    
        if(cashflowItem[0]==header['CapEx']):
            features[1][companyDictionary[company]+featureDictionary['CapEx']]= -1*cashflowItem[3] 
            features[2][companyDictionary[company]+featureDictionary['CapEx']]= -1*cashflowItem[2] 
            features[3][companyDictionary[company]+featureDictionary['CapEx']]= -1*cashflowItem[1] 

features[1][featureNumber-1] = 2389 #Target
features[2][featureNumber-1] = 2854
features[3][featureNumber-1] = 3352

for i in range(1,len(features)):
    actSumIntangibles = 0
    actSumRnD = 0
    actSumRev = 0
    actSumCapEx = 0
    
    for j in range(len(features[i])):
        if features[0][j][7:] == 'Intangibles':
            actSumIntangibles += features[i][j]
        if features[0][j][7:] == header['R&D']:
            actSumRnD += features[i][j]
        if features[0][j][7:] == header['Rev']:
            actSumRev += features[i][j]
        if features[0][j][7:] == header['CapEx']:
            actSumCapEx += features[i][j]
    
    avgFeatures[i][2]=actSumIntangibles / 5
    avgFeatures[i][3]=actSumRnD / 5
    avgFeatures[i][4]=actSumRev / 5
    avgFeatures[i][5]=actSumCapEx / 5


with open('./data-mining-trend/features.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for row in features:
        writer.writerow(row)

with open('./data-mining-trend/avgFeatures.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for row in avgFeatures:
        writer.writerow(row)