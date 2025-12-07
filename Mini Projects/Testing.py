import pandas as pd

df = pd.read_csv('testing.csv') # Load dataset
df.set_index('CustomerID', inplace=True) # Set index to CustomerID

print(df.loc['C345'])
print(df.loc[['C345', 'C789']])
print(df.loc['C123' : 'C456'])
print(df.loc[df['Region']== 'Asia'])
print(df.loc[:, 'Name'])
print(df.loc[:, ['Name', 'Age']])