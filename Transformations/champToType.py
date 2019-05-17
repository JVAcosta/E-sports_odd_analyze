import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
import json

def changeValues(index,data):
    print(index)
    df.set_value(index, 'CHAMP1', lolChamps[champ1]['tags'])
    df.set_value(index, 'CHAMP2', lolChamps[champ2]['tags'])

def createDataFrames():
    
    lol_df = pd.read_csv('..\Results\selected_duos.csv')
    lolChamps = json.loads(open('..\Datasets\league of legends\champion.json' , encoding="utf8").read())
    part_df=lol_df.loc[:,['CHAMP1','CHAMP2','Total_Played','Wins']]
    return1=part_df.rename(index=str,   columns={'CHAMP1':'TAG1',"CHAMP2":'TAG2'})
    part1_df=return1.groupby(['TAG1','TAG2'],0,None,True,False,False).sum()
    print(part1_df.iterrows().data)
    map(changeValues,part1_df.iterrows())
    return part1_df



    

createDataFrames().to_csv('..\Results\TAGS.csv', encoding='utf-8')


