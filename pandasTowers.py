import pandas as pd
# import seaborn as sns
import json
from mathPlot import mathBoxPlot
arqSaida = open('saida.txt', "w")
tempo_torre = 9999999999999.9
listablue = []
tempo_torrered = 9999999999999.9
listared = []
lol_df = pd.read_csv('leagueoflegends/LeagueofLegends.csv', thousands=",")


dic_torresblue = ((lol_df[['bTowers']]).to_json())
dictjblue = json.loads(dic_torresblue)
for x in dictjblue["bTowers"].values():
    x = x.replace('[', '').replace(']', '').replace(' ', '')
    x = x.split(',')
    # print(x)
    for i in x:
        try:
            if float(i) < tempo_torre:
                tempo_torre = float(i)
        except:
            pass
    if tempo_torre != 9999999999999.9:
        listablue.append(tempo_torre)

    tempo_torre = 9999999999999.9

dic_torresred = ((lol_df[['rTowers']]).to_json())
dictjred = json.loads(dic_torresred)
for x in dictjred["rTowers"].values():
    x = x.replace('[', '').replace(']', '').replace(' ', '')
    x = x.split(',')
    for i in x:
        try:
            if float(i) < tempo_torrered:
                tempo_torrered = float(i)
        except:
            pass
    if tempo_torrered != 9999999999999.9:
        listared.append(tempo_torrered)

    tempo_torrered = 9999999999999.9

print(listablue)
print(listared)


mathBoxPlot((listared))
