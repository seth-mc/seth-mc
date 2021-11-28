import os
import pandas as pd
import numpy as np
import fitz
import glob
import re

# 1. the address-matcherator:

groupedlists = []


def autocorrector(target, source):
    target = "#" + str(target)
    source = "#" + str(source)
    target = [k for k in target]
    source = [k for k in source]
    sol = np.zeros((len(source), len(target)))

    sol[0] = [j for j in range(len(target))]
    sol[:, 0] = [j for j in range(len(source))]

    if target[1] != source[1]:
        sol[1, 1] = 2

    for c in range(1, len(target)):
        for r in range(1, len(source)):
            if target[c] != source[r]:
                sol[r, c] = min(sol[r - 1, c], sol[r, c - 1]) + 1
            else:
                sol[r, c] = sol[r - 1, c - 1]

    if len(target) > len(source):
        pctg = abs((len(target) - sol[-1, -1])) / len(target)
    else:
        pctg = abs((len(source) - sol[-1, -1])) / len(source)

    return(pctg)

filepath = os.getcwd()
os.chdir('./sample_files')

for f in glob.glob("*.pdf"):

    doc = fitz.open(f)
    for page in doc:
        x = str(page.get_text()).split('\n')

        redundant_stuff = ['21 Line', 'Ligne', '22 Description - Désignation', '23 Weight/KGM', 'Poids/KGM', '24 Previous Transaction Number', 'Transaction Antérieure Numéro', '25 Line', 'Ligne', '26 Special Authority - Autorisation Spéciale', '27 Classification No.', 'No de classement', '28 Tariff Code 29 Quantity - Quantité', '30 U - M', '31 VFDC', 'Code VD', '32 SIMAC', 'CLMSI', '33 Rate of Cust Duty', 'Taux de droit de douane', '34 E.T. Rate', 'Taux T.A.', '35 GST Rate', 'Taux de TPS', '36 Value for Currency Conversion', 'Conversion valeur pour change', 'Tarifaire', '37 Value for Duty - Valeur en Douane', '38 Customs Duties', 'Droits de Douane', '39 SIMA Assessment', 'Cotisation de LMSI', "40 Excise Tax - Taxe d'Accise", '41 Value for Tax - Valeur pour Taxe', '42 GST - TPS', '21 Line', 'Ligne', '22 Description - Désignation', '23 Weight/KGM', 'Poids/KGM', '24 Previous Transaction Number', 'Transaction Antérieure Numéro', '25 Line', 'Ligne', '26 Special Authority - Autorisation Spéciale', '27 Classification No.', 'No de classement', '28 Tariff Code 29 Quantity - Quantité', '30 U - M', '31 VFDC', 'Code VD', '32 SIMAC', 'CLMSI', '33 Rate of Cust Duty', 'Taux de droit de douane', '34 E.T. Rate', 'Taux T.A.', '35 GST Rate', 'Taux de TPS', '36 Value for Currency Conversion', 'Conversion valeur pour change', 'Tarifaire', '37 Value for Duty - Valeur en Douane', '38 Customs Duties', 'Droits de Douane', '39 SIMA Assessment', 'Cotisation de LMSI', "40 Excise Tax - Taxe d'Accise", '41 Value for Tax - Valeur pour Taxe', '42 GST - TPS', '21 Line', 'Ligne', '22 Description - Désignation', '23 Weight/KGM', 'Poids/KGM', '24 Previous Transaction Number', 'Transaction Antérieure Numéro', '25 Line', 'Ligne', '26 Special Authority - Autorisation Spéciale', '27 Classification No.', 'No de classement', '28 Tariff Code 29 Quantity - Quantité', '30 U - M', '31 VFDC', 'Code VD', '32 SIMAC', 'CLMSI', '33 Rate of Cust Duty', 'Taux de droit de douane', '34 E.T. Rate', 'Taux T.A.', '35 GST Rate', 'Taux de TPS', '36 Value for Currency Conversion', 'Conversion valeur pour change', 'Tarifaire', '37 Value for Duty - Valeur en Douane', '38 Customs Duties', 'Droits de Douane', '39 SIMA Assessment', 'Cotisation de LMSI', "40 Excise Tax - Taxe d'Accise", '41 Value for Tax - Valeur pour Taxe', '42 GST - TPS', '21 Line', 'Ligne', '22 Description - Désignation', '23 Weight/KGM', 'Poids/KGM', '24 Previous Transaction Number', 'Transaction Antérieure Numéro', '25 Line', 'Ligne', '26 Special Authority - Autorisation Spéciale', '27 Classification No.', 'No de classement', '28 Tariff Code 29 Quantity - Quantité', '30 U - M', '31 VFDC', 'Code VD', '32 SIMAC', 'CLMSI', '33 Rate of Cust Duty', 'Taux de droit de douane', '34 E.T. Rate', 'Taux T.A.', '35 GST Rate', 'Taux de TPS', '36 Value for Currency Conversion', 'Conversion valeur pour change',
                           'Tarifaire', '37 Value for Duty - Valeur en Douane', '38 Customs Duties', 'Droits de Douane', '39 SIMA Assessment', 'Cotisation de LMSI', "40 Excise Tax - Taxe d'Accise", '41 Value for Tax - Valeur pour Taxe', '42 GST - TPS', '21 Line', 'Ligne', '22 Description - Désignation', '23 Weight/KGM', 'Poids/KGM', '24 Previous Transaction Number', 'Transaction Antérieure Numéro', '25 Line', 'Ligne', '26 Special Authority - Autorisation Spéciale', '27 Classification No.', 'No de classement', '28 Tariff Code 29 Quantity - Quantité', '30 U - M', '31 VFDC', 'Code VD', '32 SIMAC', 'CLMSI', '33 Rate of Cust Duty', 'Taux de droit de douane', '34 E.T. Rate', 'Taux T.A.', '35 GST Rate', 'Taux de TPS', '36 Value for Currency Conversion', 'Conversion valeur pour change', 'Tarifaire', '37 Value for Duty - Valeur en Douane', '38 Customs Duties', 'Droits de Douane', '39 SIMA Assessment', 'Cotisation de LMSI', "40 Excise Tax - Taxe d'Accise", '41 Value for Tax - Valeur pour Taxe', '42 GST - TPS', 'CANADA CUSTOMS CODING FORM', 'DOUANES CANADA - FORMULE DE CODAGE', 'Protected (When Completed)', 'Protégé (Une Fois Rempli)', '1 Importer name and address', "Nom et adresse de l'importateur", 'No.', '2 Transaction No. - No de transaction', '10 Sub ', 'Hdr', 'No.', 'No de', 'sous-', 'en-tête', '11 Vendor name - Nom du Vendeur', 'No.', '3 Type 4 Office No.', 'No de bureau', '5 GST Registration No.', 'No de TPS', '6 Payment', 'code', 'Code de', 'paiement', '7 Mode', 'of-de', 'Trans', '8 Port of', 'unlading', 'Port de', 'débarq.', '9 Total VFD - Total de la VD', '12 Country of Origin', "Pays d'origine", '13 Place of Export', "Lieu d'exportation", '14 Tariff Treatment', 'Traitement tarifaire', '15 U.S. Port of Exit', 'Bureau de sortie', 'des É.-U.', '16 Direct Shipment Date', "Date d'expédition directe", '17 CRCY', 'Code', 'Devise', '18 Time Limit - Délai 19 Freight - Fret', '20 Release Date - Date de la mainlevée', 'Reserved for CCRA Use', "Réservé à l'usage de l'agence", 'Location of Goods - Emplacement des marchandises', "Shipped Per - Mode d'expédition", 'Cust. Order No. - Comm du client', 'B/L No. - No de connaissement', "Exchange Rate - Taux d'échange", 'Declaration - Déclaration', 'I', 'Je', 'Please Print Name - Lettres moulées S.V.P.', 'OF', 'DE', 'Importer/Agent - Importateur/Agent', 'Declare the particulars of this document to be true, accurate and complete.', 'Déclare que les renseignements ci-dessus sont vrais et complets.', 'Date', 'Signature', '43 Deposit - Dépôt', "44 Warehouse No. - No d'entrepôt", '45 Cargo Control No. - No de contrôle du fret', "46 Carrier Code at Importation - Code de transporteur à l'importation", '47 Customs', 'Duties', 'Droits de', 'Douane', '48 SIMA', 'Assessment', 'Cotisation', 'de lmsi', '49 Excise Tax', "Taxe d'accise", '50 GST', 'TPS', '51', 'TOTAL', 'B3-3 (04)', 'Canada']

        new = [i for i in x if i not in redundant_stuff]
        new2 = [word for line in new for word in re.split('\s\s+', line)]
        groupedlists.append(new2)


all_data = pd.DataFrame(groupedlists)


all_data.to_csv('all_data.csv', index=None, header=True,
                encoding='utf-8', na_rep='')
