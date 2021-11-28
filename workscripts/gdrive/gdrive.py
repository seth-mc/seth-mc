import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd
import numpy as np
import time
from values import *

d = os.getcwd()
os.chdir(d)
products = pd.read_excel('allproducts.xlsx')
nas = values.na_values1
for na in nas:
    products[na] = products[na].fillna("")

nas = values.na_values2
hts = pd.read_csv('htsdata.csv', header=0)
hts = hts[nas]
for na in nas:
    hts[na] = hts[na].fillna("")
    
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('DataBot').sheet1

headers = values.excel_headers

completed = ['Internal Reference']


while True:
    # adding from allproducts.xlsx
    added = sheet.col_values(3)
    new = np.array([el for el in added if el not in completed])
    if len(new) == 0:
        while True:
            time.sleep(5)
            added = sheet.col_values(3)
            new = np.array([el for el in added if el not in completed])
            if len(new) != 0:
                break
            
    for iteration, item in enumerate(new):
        # keep a list of completed stuff
        completed.append(item)
        # find what was inputted in excel
        info = products.loc[products['Internal Reference'] == item]
        # remove duplicate finds
        if len(info.index) > 1:
            print('multiple matches for {}, selecting first'.format(info['Internal Reference']))
            info = info.iloc[:,0]
        info = info.to_dict('record')
        rowid = sheet.find(item).row
        diction = info[0]
        # add info to each value
        for key in diction.keys():
            val = headers[key] + str(iteration + 2)
            sheet.update(val, diction[key])


    # getting htsdata from file
    completedhs = ['HS Code (Short)']
    addedhs = sheet.col_values(4)
    newhs = np.array([el for el in addedhs if el not in completedhs])

    for iteration, item in enumerate(newhs):
        # keep a list of completed stuff
        completedhs.append(item)
        # keep shortening and searching HS Code until it finds a match
        while True:
            info = hts.loc[hts['HTS Number'] == item]
            match = len(info)
            if match < 1:
                item = item[:-1]
                continue
            elif match == 1:
                break
            elif match > 1:
                info = info.iloc[:,0]
        
        info = info.to_dict('record')
        diction = info[0]
        # add info to each value
        for key in diction.keys():
            val = headers[key] + str(iteration + 2)
            sheet.update(val, diction[key])
    
    
    time.sleep(5)
        


# adding item ID's to completed list and taking those out of the equation does not work,
# item ID's will appear multiple times.

# maybe adding val to a list and ensuring that you don't go over each unique cell ID (A1, B2)
# would work more seamlessly. 
    

 
