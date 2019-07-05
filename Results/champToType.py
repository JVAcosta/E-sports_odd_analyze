import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
import json


class ChampTags:
    def __init__(self):
        self.lol_df = pd.read_csv("mathUps_teste.csv")
        self.lolChamps = json.loads(
            open('../Datasets/league of legends/champion.json', encoding="utf8").read())

    def createDataFrames(self):
        part_df = self.lol_df.loc[:, [
            'CHAMP1_x', 'CHAMP2_x', 'CHAMP1_y', 'CHAMP2_y', 'bResult', 'rResult', 'Partidas_x']]
        return1 = part_df.rename(index=str,   columns={
                                 'CHAMP1_x': 'TAG_Champ_1_Blue', "CHAMP2_x": 'TAG_Champ_2_blue', 'CHAMP1_y': 'TAG_Champ_1_Red', "CHAMP2_y": 'TAG_Champ_2_red'})
        self.lol_df = pd.DataFrame(return1.groupby(['TAG_Champ_1_Blue', 'TAG_Champ_2_blue', 'TAG_Champ_1_Red', 'TAG_Champ_2_red'], 0, None, True, False, False).sum(
        )).reset_index().sort_values('Partidas_x', ascending=False)
        for i, v in self.lol_df.iterrows():
            tags = str(self.lolChamps['data'][v.TAG_Champ_1_Blue]['tags'])[
                2:-2].replace("'", '')
            self.lol_df.at[i, 'TAG_Champ_1_Blue'] = tags
            tags = str(self.lolChamps['data'][v.TAG_Champ_2_blue]['tags'])[
                2:-2].replace("'", '')
            self.lol_df.at[i, 'TAG_Champ_2_blue'] = tags
            tags = str(self.lolChamps['data'][v.TAG_Champ_1_Red]['tags'])[
                2:-2].replace("'", '')
            self.lol_df.at[i, 'TAG_Champ_1_Red'] = tags
            tags = str(self.lolChamps['data'][v.TAG_Champ_2_red]['tags'])[
                2:-2].replace("'", '')
            self.lol_df.at[i, 'TAG_Champ_2_red'] = tags

        self.lol_df = self.lol_df.groupby(
            ['TAG_Champ_1_Blue', 'TAG_Champ_2_blue', 'TAG_Champ_1_Red', 'TAG_Champ_2_red'], 0, None, True, False, False)

        self.lol_df = self.lol_df.sum()
        self.lol_df = pd.DataFrame(self.lol_df)
        self.lol_df = self.lol_df.reset_index().sort_values(
            'Partidas_x', ascending=False)
        print(self.lol_df)
        return self.lol_df


ct = ChampTags()
ct.createDataFrames().to_csv('TAGS.csv', encoding='utf-8')
