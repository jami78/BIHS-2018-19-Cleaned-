e= pd.read_csv('e.csv')
g=pd.read_csv('g.csv')
xxa=pd.read_csv('xxa.csv')
we2= pd.read_csv('we2.csv')
we5a= pd.read_csv('we5a.csv')

#Inner join all dataframes
df = (e.merge(g, on='a01', how='inner')
             .merge(xxa, on='a01', how='inner')
             .merge(we2, on='a01', how='inner')
             .merge(we5a, on='a01', how='inner'))

#Dropping rows with duplicate a01
duplicate_rows = df[df['a01'].duplicated()]
print(duplicate_rows)

#Standardizing Columns
from sklearn.preprocessing import StandardScaler
columns_to_standardize = ['g02', 'g02_1', 'Land Acquired', 'g10', 'f_ed', 'm_ed', 'combined_ed', 'Input in economic activity', 'Input on use of generated income', 'Autonomy in personal decisions in household']
scaler = StandardScaler()
scaler.fit(df[columns_to_standardize])
df[columns_to_standardize] = scaler.transform(df[columns_to_standardize])

