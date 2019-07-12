import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
import json


class ChampTags:
    def __init__(self):
        self.lol_df = pd.read_csv('../Results/selected_duos_teste.csv')
        self.lolChamps = json.loads(
            open('../Datasets/league of legends/champion.json', encoding="utf8").read())

    def createDataFrames(self):
        part_df = self.lol_df.loc[:, [
            'CHAMP1', 'CHAMP2', 'Total_Played', 'Wins']]
        return1 = part_df.rename(index=str,   columns={
                                 'CHAMP1': 'TAG1', "CHAMP2": 'TAG2'})
        self.lol_df = pd.DataFrame(return1.groupby(['TAG1', 'TAG2'], 0, None, True, False, False).sum(
        )).reset_index().sort_values('Wins', ascending=False)
        for i, v in self.lol_df.iterrows():
            tags1 = ''
            for x in self.lolChamps['data'][v.TAG1]['tags']:
                print(self.lolChamps['data'][v.TAG1]['tags'])
                tags1 += x+'/'
            self.lol_df.at[i, 'TAG1'] = tags1
            tags2 = ''
            for x in self.lolChamps['data'][v.TAG2]['tags']:
                tags2 += x+'/'
                self.lol_df.at[i, 'TAG2'] = tags2
                self.lol_df = pd.DataFrame(self.lol_df.groupby(
                    ['TAG1', 'TAG2'], 0, None, True, False, False).sum()).reset_index().sort_values('Wins', ascending=False)

        return self.lol_df


ct = ChampTags()
ct.createDataFrames().to_csv('../Results/TAGS.csv', encoding='utf-8')
