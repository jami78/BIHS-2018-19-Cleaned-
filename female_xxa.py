import pandas as pd
xxa=pd.read_stata('094_bihs_r3_female_mod_xxa.dta')

#Null values
xxa['xxa_03'].isnull().value_counts()

#Dropping unneccessary columns and records with null values of male and female education
xxa1=xxa[['a01','xxa_03','xxa_05']].dropna()

#Mapping numbers to categories of educational qualification (female)
mapping_dict = {'Completed class I': 1, 'Completed class II': 2, 'Completed class III': 3,'Completed class IV':4, 'Completed class V':5,'Completed class VI':6,'Completed class VII':7,'Completed class VIII':8,'Completed class IX':9,'SSC/ Dakhil':10,11.0:11,'HSC/Alim':12,'BA/BSC Pass/Fazil':13,'BA/BSC Honours/Fazil':13,'MA/MSC and above Kamil':14,'Mosque based child Class':1,'Never attended school':0}
xxa1['xxa_03'] = xxa1['xxa_03'].map(mapping_dict)

#Mapping numbers to categories of educational qualification (Male)
mapping_dict = {'Completed class I': 1, 'Completed class II': 2, 'Completed class III': 3,'Completed class IV':4, 'Completed class V':5,'Completed class VI':6,'Completed class VII':7,'Completed class VIII':8,'Completed class IX':9,'SSC/ Dakhil':10,11.0:11,'HSC/Alim':12,'BA/BSC Pass/Fazil':13,'BA/BSC Honours/Fazil':13,'MA/MSC and above Kamil':14,'Mosque based child Class':1,'Never attended school':0}
xxa1['xxa_05'] = xxa1['xxa_05'].map(mapping_dict)

# Rename columns:
xxa1.rename(columns={'xxa_03': 'f_ed', 'xxa_05': 'm_ed'}, inplace=True)

# Drop duplicates randomly, keeping the first occurrence:
xxa1 = xxa1.drop_duplicates('a01', keep='first')