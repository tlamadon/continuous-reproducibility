import json
import pandas as pd

df = pd.read_csv('data_clean.csv')
data = {'mean':df.Y.mean(), 'sd': df.Y.std()}

with open('res.txt', 'w') as outfile:
    json.dump(data, outfile)