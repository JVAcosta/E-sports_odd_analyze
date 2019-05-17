import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
import json
class ChampTags:
    def __init__(self):
        self.lol_df = pd.read_csv('..\Results\selected_duos.csv')
    
    def changeValues(self,index):
        print('oi')
        champ1 = df.get_value(index,'TAG1')
        champ2 = df.get_value(index,'TAG2')
        self.lol_df.set_value(index, 'TAG1', lolChamps[champ1]['tags'])
        self.lol_df.set_value(index, 'TAG2', lolChamps[champ2]['tags'])

    def createDataFrames(self,):
        lolChamps = json.loads(open('..\Datasets\league of legends\champion.json' , encoding="utf8").read())
        part_df=self.lol_df.loc[:,['CHAMP1','CHAMP2','Total_Played','Wins']]
        return1=part_df.rename(index=str,   columns={'CHAMP1':'TAG1',"CHAMP2":'TAG2'})
        self.lol_df=return1.groupby(['TAG1','TAG2'],0,None,True,False,False).sum()
        lista = list(range(len(self.lol_df)))
        print(lista)
        map(self.changeValues,lista)
        return self.lol_df



    
ct=ChampTags()
ct.createDataFrames().to_csv('..\Results\TAGS.csv', encoding='utf-8')


