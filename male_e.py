import pandas as pd
df1 = pd.read_stata("017_bihs_r3_male_mod_e.dta")
df1
#Checking for duplicate values
duplicate_a01_values = df1[df1.groupby('a01')['e07'].transform('nunique') > 1]['a01'].unique()
duplicate_a01_values
#Mapping Categorical Variables to Numerical Binary Variables
df1['e02'] = df1['e02'].map({'Yes': 1, 'No': 0})
df1['e01'] = df1['e01'].map({'Yes': 1, 'No': 0})

#Count of households which save(d)
df1['e02'].value_counts()
df1['e01'].value_counts()

#Ordinal Encoding of saving frequency
df1['e07'] = df1['e07'].map({'Not regularly': 1, 'Yearly': 2,'Biannually':3,'Quarterly':4,'Monthly':5,'Weekly':6,'Daily':7})

#Filling missing e07 values
df1['e07'].fillna(0,inplace=True)

# Saving diversification- Number of places each household has/had saved in:
a01_counts = df1['a01'].value_counts()
df1['a01_count'] = df1['a01'].map(a01_counts)

#Renaming the column
df1.rename(columns = {'a01_count':'Savings diversification'}, inplace = True) 

#Filling missing e06 values
df1['e06'].fillna(0,inplace=True)

#New column containing the total amount saved currently for each household
e06_sum = df1.groupby('a01')['e06'].sum()
df1['e06_sum'] = df1['a01'].map(e06_sum)

#Creating a new Dataframe with the necessary columns
dff1=df1[['a01','e01','e02','e06_sum','e07','Savings diversification']]

#Dropping duplicate rows
dff1 = dff1.drop_duplicates()

#Keeping rows with the maximum value of saving frequency for each household
dff2 = dff1.loc[dff1.groupby('a01')['e07'].transform(max) == dff1['e07']]

#Z-score standardization

import pandas as pd
from sklearn.preprocessing import StandardScaler
columns_to_standardize = dff2.columns.difference(['a01','e01','e02'])
scaler = StandardScaler()
scaler.fit(dff2[columns_to_standardize])
dff2[columns_to_standardize] = scaler.transform(dff2[columns_to_standardize])