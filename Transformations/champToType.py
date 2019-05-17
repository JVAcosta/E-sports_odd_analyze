import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
import json
class ChampTags:
    def __init__(self):
        self.lol_df = pd.read_csv('..\Results\selected_duos.csv')
        self.lolChamps = json.loads(open('..\Datasets\league of legends\champion.json' , encoding="utf8").read())

    def createDataFrames(self):
        part_df=self.lol_df.loc[:,['CHAMP1','CHAMP2','Total_Played','Wins']]
        return1=part_df.rename(index=str,   columns={'CHAMP1':'TAG1',"CHAMP2":'TAG2'})
        self.lol_df=return1.groupby(['TAG1','TAG2'],0,None,True,False,False).sum()
        for i in range(len(self.lol_df)):
            print(self.lol_df)
            dat=self.lol_df.iloc[0,'TAG1']
            data = self.lolChamps['data'][dat]
            self.lol_df[i,'TAG1'] = self.lolChamps['data'][self.lol_df.iat[i,0]]
            
        return self.lol_df



    
ct=ChampTags()
ct.createDataFrames().to_csv('..\Results\TAGS.csv', encoding='utf-8')


