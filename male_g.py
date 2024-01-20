import pandas as pd
dg=pd.read_csv('male_g.csv')
dg
#Land Acquired= Current Land- Land in 2015
dg['Land Acquired']=dg['g02']-dg['g02_1'] 

#Shortened Dataset(Columns that are required)
dg=dg[['a01','g02','g02_1','g09c','Land Acquired','g10']]

#Filling the missing g10 values:
# Calculate the sum of g10 and sum of g02:
sum_g10 = dg['g10'].sum()
sum_g02 = dg['g02'].sum()

# Calculate the ratio and create the mv variable:
mv = (sum_g10 / sum_g02) * dg['g02']

#Filling the values:
dg['g10'].fillna(mv, inplace=True)

#Adding the land amount and land value for each household
male_g = male_g.groupby('a01')[['g02_1', 'g02', 'Current Land', 'g10']].sum()