import pandas as pd
import json
from mathPlot import mathBoxPlot
pathName = "leagueoflegends/"  # path para arquivos csv
# pd.to_csv(name_of_the_file_to_save.csv')

df = pd.read_csv(pathName + "bans.csv")
df = df[['ban_1']]
print(df)
dfBan1 = df.groupby('ban_1').sum()
print(dfBan1)
