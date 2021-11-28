import time
import os
import numpy as np
import datetime as dt
import fitz
import glob
import pandas as pd
import re

# opening the UPS PDF:
filePath = os.getcwd()
os.chdir(str(filePath[:-8]) + "./sample_files")

all_data = pd.DataFrame()

# deleting old merged file:
while True:
    filelist = ['all_data.csv']
    if all([os.path.isfile(f) for f in filelist]):
        os.remove('all_data.csv')
        break
    else:
        print('Past file not found. Proceeding...')
        break

# checking to make sure my hard work (manual inputs) are still there:
while True:
    filelist = ['Major Duties.csv']
    if all([os.path.isfile(f) for f in filelist]):
        major_duties = pd.read_csv('Major Duties.csv', header=0)
        break
    else:
        print('Physical inputs not found. Proceeding...')
        break

# merging all the CSVs:
print('merging the CSVs...\n')
files = []
for f in glob.glob("*.csv"):
    if 'Major' in f:
        continue
    else:
        files.append(f)

allfiles = set(files)

for f in allfiles:
    df = pd.read_csv(f, header=None)
    all_data = all_data.append(df, ignore_index=True)


# adding UPS Headers (updated 2019):
print('adding Headers...\n')
headers = ['Version', 'Recipient Number', 'Account Number', 'Account Country/Territory', 'Invoice Date', 'Invoice Number', 'Invoice Type Code', 'Invoice Type Detail Code', 'Account Tax ID', 'Invoice Currency Code', 'Invoice Amount', 'Transaction Date', 'Pickup Record Number', 'Lead Shipment Number', 'World Ease Number', 'Shipment Reference Number 1', 'Shipment Reference Number 2', 'Bill Option Code', 'Package Quantity', 'Oversize Quantity', 'Tracking Number', 'Package Reference Number 1', 'Package Reference Number 2', 'Package Reference Number 3', 'Package Reference Number 4', 'Package Reference Number 5', 'Entered Weight', 'Entered Weight Unit of Measure', 'Billed Weight', 'Billed Weight Unit of Measure', 'Container Type', 'Billed Weight Type', 'Package Dimensions', 'Zone', 'Charge Category Code', 'Charge Category Detail Code', 'Charge Source', 'Type Code 1', 'Type Detail Code 1', 'Type Detail Value 1', 'Type Code 2', 'Type Detail Code 2', 'Type Detail Value 2', 'Charge Classification Code', 'Charge Description Code', 'Charge Description', 'Charged Unit Quantity', 'Basis Currency Code', 'Basis Value', 'Tax Indicator', 'Transaction Currency Code', 'Incentive Amount', 'Net Amount', 'Miscellaneous Currency Code', 'Miscellaneous Incentive Amount', 'Miscellaneous Net Amount', 'Alternate Invoicing Currency Code', 'Alternate Invoice Amount', 'Invoice Exchange Rate', 'Tax Variance Amount', 'Currency Variance Amount', 'Invoice Level Charge', 'Invoice Due Date', 'Alternate Invoice Number', 'Store Number', 'Customer Reference Number', 'Sender Name', 'Sender Company Name', 'Sender Address Line 1', 'Sender Address Line 2', 'Sender City', 'Sender State', 'Sender Postal', 'Sender Country/Territory', 'Receiver Name', 'Receiver Company Name', 'Receiver Address Line 1', 'Receiver Address Line 2', 'Receiver City', 'Receiver State', 'Receiver Postal', 'Receiver Country/Territory', 'Third Party Name', 'Third Party Company Name', 'Third Party Address Line 1', 'Third Party Address Line 2', 'Third Party City', 'Third Party State', 'Third Party Postal', 'Third party Country/Territory', 'Sold To Name', 'Sold To Company Name', 'Sold To Address Line 1', 'Sold To Address Line 2', 'Sold To City', 'Sold To State', 'Sold To Postal', 'Sold to Country/Territory', 'Miscellaneous Address Qual 1', 'Miscellaneous Address 1 Name', 'Miscellaneous Address 1 Company Name', 'Miscellaneous Address 1 Address Line 1', 'Miscellaneous Address 1 Address Line 2', 'Miscellaneous Address 1 City', 'Miscellaneous Address 1 State', 'Miscellaneous Address 1 Postal', 'Miscellaneous address 1 Country/Territory', 'Miscellaneous Address Qual 2', 'Miscellaneous Address 2 Name', 'Miscellaneous Address 2 Company Name', 'Miscellaneous Address 2 Address Line 1', 'Miscellaneous Address 2 Address Line 2',
           'Miscellaneous Address 2 City', 'Miscellaneous Address 2 State', 'Miscellaneous Address 2 Postal', 'Miscellaneous address 2 Country/Territory', 'Shipment Date', 'Shipment Export Date', 'Shipment Import Date', 'Entry Date', 'Direct Shipment Date', 'Shipment Delivery Date', 'Shipment Release Date', 'Cycle Date', 'EFT Date', 'Validation Date', 'Entry Port', 'Entry Number', 'Export Place', 'Shipment Value Amount', 'Shipment Description', 'Entered Currency Code', 'Customs Number', 'Exchange Rate', 'Master Air Waybill Number', 'EPU', 'Entry Type', 'CPC Code', 'Line Item Number', 'Goods Description', 'Entered Value', 'Duty Amount', 'Weight', 'Unit of Measure', 'Item Quantity', 'Item Quantity Unit of Measure', 'Import Tax ID', 'Declaration Number', 'Carrier Name/Clinical Trial Identification Number/SDS ID ', 'CCCD Number', 'Cycle Number', 'Foreign Trade Reference Number', 'Job Number', 'Transport Mode', 'Tax Type', 'Tariff Code', 'Tariff Rate', 'Tariff Treatment Number', 'Contact Name', 'Class Number', 'Document Type', 'Office Number', 'Document Number', 'Duty Value', 'Total Value for Duty', 'Excise Tax Amount', 'Excise Tax Rate', 'GST Amount', 'GST Rate', 'Order In Council', 'Origin Country/Territory', 'SIMA Access', 'Tax Value', 'Total Customs Amount', 'Miscellaneous Line 1', 'Miscellaneous Line 2', 'Miscellaneous Line 3', 'Miscellaneous Line 4', 'Miscellaneous Line 5', 'Payor Role Code', 'Miscellaneous Line 7', 'Miscellaneous Line 8', 'Miscellaneous Line 9', 'Miscellaneous Line 10', 'Miscellaneous Line 11', 'Duty Rate', 'VAT Basis Amount', 'VAT Amount', 'VAT Rate', 'Other Basis Amount', 'Other Amount', 'Other Rate', 'Other Customs Number Indicator', 'Other Customs Number', 'Customs Office Name', 'Package Dimension Unit Of Measure', 'Original Shipment Package Quantity', 'Corrected Zone', 'Tax Law Article Number', 'Tax Law Article Basis Amount', 'Original tracking number', 'Scale weight quantity', 'Scale Weight Unit of Measure', 'Raw dimension unit of measure', 'Raw dimension length', 'BOL # 1', 'BOL # 2', 'BOL # 3', 'BOL # 4', 'BOL # 5', 'PO # 1', 'PO # 2', 'PO # 3', 'PO # 4', 'PO # 5', 'PO # 6', 'PO # 7', 'PO # 8', 'PO # 9', 'PO # 10', 'NMFC', 'Detail Class', 'Freight Sequence Number', 'Declared Freight Class', 'EORI Number', 'Detail Keyed Dim', 'Detail Keyed Unit of Measure', 'Detail Keyed Billed Dimension', 'Detail Keyed Billed Unit of Measure', 'Original Service Description', 'Promo Discount Applied Indicator', 'Promo Discount Alias', 'SDS Match Level Cd', 'SDS RDR Date', 'SDS Delivery Date', 'SDS Error Code', 'Place Holder 46', 'Place Holder 47', 'Place Holder 48', 'SCC Scale Weight', 'Place Holder 50', 'Place Holder 51', 'Place Holder 52', 'Place Holder 53', 'Place Holder 54', 'Place Holder 55', 'Place Holder 56', 'Place Holder 57', 'Place Holder 58', 'Place Holder 59', 'Place Holder 60']
all_data.columns = headers

# remove double headers
all_data = all_data[all_data.Version != 'Version']


# merging address info into 'origin' and 'destination':
print('merging addresses...\n')
addresstings = ['Sender Address Line 1', 'Sender Address Line 2', 'Sender City', 'Sender State', 'Sender Postal', 'Sender Country/Territory', 'Receiver Company Name', 'Receiver Address Line 1', 'Receiver Address Line 2',
                'Receiver City', 'Receiver State', 'Receiver Postal', 'Receiver Country/Territory']

all_data['Origin'] = all_data['Sender Address Line 1'].astype(str) + ' ' + all_data['Sender Address Line 2'].astype(str) + ' ' + all_data['Sender City'].astype(
    str) + ' ' + all_data['Sender State'].astype(str) + ' ' + all_data['Sender Postal'].astype(str) + ' ' + all_data['Sender Country/Territory'].astype(str)

all_data['Destination'] = all_data['Receiver Address Line 1'].astype(str) + ' ' + all_data['Receiver Address Line 2'].astype(str) + ' ' + all_data['Receiver City'].astype(
    str) + ' ' + all_data['Receiver State'].astype(str) + ' ' + all_data['Receiver Postal'].astype(str) + ' ' + all_data['Receiver Country/Territory'].astype(str)

all_data = all_data.drop(axis=1, columns=[i for i in addresstings])


all_data['Invoice Number'] = all_data['Invoice Number'].astype(str)
all_data['Net Amount'] = all_data['Net Amount'].astype(str)


# add new items to major duties

# find new invoices that are in the file
print('adding to Major Duties.csv...\n')
finalones = major_duties['Invoice Number'].tolist()
conglomerates = all_data['Invoice Number'].tolist()
newinvoices = np.setdiff1d(conglomerates, finalones)

autoinputs = ['Invoice Number', 'Invoice Date', 'Charge Description',
              'Goods Description', 'Net Amount', 'Origin', 'Destination']
keydata = all_data[autoinputs]
keydata = keydata.loc[(all_data['Charge Description'].str.contains(r'DUTY TO CUSTOMS'))]


# add new rows to thing
for i in newinvoices:
    for row in keydata.itertuples():
        if i in row[1]:
            new = pd.DataFrame(row[1:]).transpose()
            new.columns = autoinputs
            major_duties = pd.concat([major_duties, new], sort=True, ignore_index=True)
                



# organize by date:
print('Organizing by Date...\n')


major_duties['Invoice Date'] = pd.to_datetime(
    major_duties['Invoice Date'], format='%d-%b-%y')
major_duties = major_duties.sort_values(by='Invoice Date')


columnorder = ['Invoice Number','Invoice Date','Charge Description','Goods Description','Net Amount','Origin','Destination','HTSUS Description 1','HTSUS Code 1','HTSUS (Tariff) Rate 1','HTSUS1 Dollar Amount','HTSUS Description 2','HTSUS Code 2','HTSUS (Tariff) Rate 2','HTSUS2 Dollar Amount','MPF Rate','MPF Dollar Amount','HMF Rate','HMF Dollar Amount','Total Entered Value','Customs Date']


major_duties[columnorder].to_csv('Major Duties.csv', index=None, header=True,
                encoding='utf-8', na_rep='')
