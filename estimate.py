import json
import pandas as pd

df = pd.read_csv('data_clean.csv')
m = df.Y.mean()
data = {'mean':m}

with open('res.txt', 'w') as outfile:
    json.dump(data, outfile)
