import pandas as pd
import json
from mathPlot import mathBoxPlot
pathName = "leagueoflegends/"  # path para arquivos csv
# pd.to_csv(name_of_the_file_to_save.csv')

df = pd.read_csv(pathName + "LeagueofLegends.csv")


string_json = df[['golddiff']].to_json()
json_dic = json.loads(string_json)
arq = open("teste.txt", "w")
arq.write(string_json)
arq.close()

listLastValues = []
for x in json_dic['golddiff'].values():
    x = x.replace('[', '').replace(']', '').replace(' ', '')
    x = x.split(',')
    x = int(x[-1])
    listLastValues.append(x)

mathBoxPlot((listLastValues))
