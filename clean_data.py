import pandas as pd

df = pd.read_csv('data.csv')
df.Y = df.Y - df.Y.mean()
df.to_csv('data_clean.csv',index = False)

