import os
import numpy as np
import fitz
import glob
import pandas as pd
import values as values


class UpsReader:
    def __init__(self, pdf, csv):
        self.pdf = pdf
        self.csv = csv

    def address_matcher(self, target, source):
        # i: the address-matcherator: uses minimum edit distance to match strings
            # target = the correct one
            # source = the wrong one

        # build empty matrix
        target = ("#" + str(target)).lower()
        source = ("#" + str(source)).lower()
        target = [k for k in target]
        source = [k for k in source]
        sol = np.zeros((len(source), len(target)))

        # first row and column
        sol[0] = [j for j in range(len(target))]
        sol[:,0] = [j for j in range(len(source))]

        # add anchor value
        if target[1] != source[1]:
            sol[1,1] = 2

        # fill in the rest

        # we need to go through through every entry (column)
        for c in range(1, len(target)):

            # we need to go through every row
            for r in range(1, len(source)):

                # if they are not the same letter
                if target[c] != source[r]:
                    sol[r,c] = min(sol[r-1,c], sol[r,c-1]) + 1

                # if they are the same letter
                else:
                    sol[r,c] = sol[r-1,c-1]
   
        # return
        if len(target) > len(source):
            pctg = abs((len(target) - sol[-1,-1])) / len(target)
        else:
            pctg = abs((len(source) - sol[-1,-1])) / len(source)

        return pctg

    def get_key_info(self):

        upscharges = values.upscharges
        our_addresses = values.addresses
        upsheaders = values.upsheaders
        doc = fitz.open(self.pdf)

        # 1. opening and formatting the UPS CSV:
        df = pd.read_csv(self.csv, header=None)
        df.columns = upsheaders
        df['Receiver Postal'] = df['Receiver Postal'].fillna(0)
        # formatting postal codes properly
        try:
            df['Receiver Postal'] = df['Receiver Postal'].astype(int)
        except ValueError:
            df['Receiver Postal'] = df['Receiver Postal'].astype(str)
        df['Receiver Postal'] = df['Receiver Postal'].astype(str)

        df['Tracking Number'] = df['Tracking Number'].fillna('')

        idsAndPrices = df.groupby(['Tracking Number'], sort=False, as_index=False)[
            'Net Amount'].sum()
        idsAndPrices.columns = ['Tracking Number', 'Net Sum']

        # 2. look for our addresses
        addresses = df.copy(deep=True)
        ye = addresses[['Tracking Number','Receiver Postal']]
        freight = []
        for row in ye.itertuples():
            # look for addresses that are 90% similar to ours:
            for i in our_addresses:
                if self.address_matcher(row[2], i) >= 0.9:
                    freight.append(row[1])

        # removing duplicates from a list
        known_links = set()
        newlist = []
        for t in freight:
            if t in known_links:
                continue
            newlist.append(t)
            known_links.add(t)

        prices = dict()
        for row in idsAndPrices.itertuples():
            for i in newlist:
                if i in row[1]:
                    prices[i] = round(row[2], 2)

        total = 0
        for k, v in prices.items():
            total += v
            for page in doc:
                pg = page.get_text("words")
                if any(k in sublist for sublist in pg):
                    pgnum = page.number + 1
                    break
                else:
                    pgnum = 0
                    continue
            print(str(k) + ': ' + str(v) + ' Page: ' + str(pgnum))
        print('––––––––––––––––––\n' + 'Total: $' + str(round(total, 2)))


        # 3. look for our least common charges
        print('\nLooking at rare charges...\n')
        print(df['Charge Description'].value_counts(ascending=True).head(5))

        # 4. look for expensive charges
        print('\nLooking at expensive charges...\n')
        print(idsAndPrices.sort_values('Net Sum', ascending=False).head(5))

a = os.getcwd()
os.chdir('./sample_files')

i = 0
for p in glob.glob("*.pdf"):
    for c in glob.glob("*.csv"):
        if p[:-4] in c[:-4]:
            read = UpsReader(p, c)
            read.get_key_info()
            print('\n\n\n')
