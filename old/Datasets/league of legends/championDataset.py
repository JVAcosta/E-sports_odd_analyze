import pandas as pd
import json
arq = open('champion.json', 'r')
j = json.load(arq)
print(j['data']['Rakan'].keys())
l = [(x, y['tags']) for x, y in j['data'].items()]
df = pd.DataFrame(l)
df = df.rename(index=str, columns={0: "champion", 1: "tag"})
name = 'champions_tags.csv'
df.to_csv(name, encoding='utf-8')
print(df.head())
