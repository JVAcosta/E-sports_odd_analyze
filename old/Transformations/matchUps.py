import pandas as pd
# from Datasets.Kaggle.datasets import LeagueofLegends_df
import json


def createDataFrameChampions():
    lol_df = pd.read_csv('../Results/mathUps_teste.csv')
    lol_df = pd.DataFrame(lol_df.groupby(['CHAMP1_x', 'Team_x', 'CHAMP2_x', 'Year_x',
                                          'CHAMP1_y', 'CHAMP2_y'], 0, None, True, False, False)['Partidas_x', 'bResult'].sum()).reset_index()

    return lol_df


def createDataFrameTags():
    lol_df = pd.read_csv('../Results/mathUps_teste.csv')
    tagsDF = pd.read_csv('../Datasets/league of legends/champions_tags.csv')
    lolChamps = json.loads(
        open('../Datasets/league of legends/champion.json', encoding="utf8").read())
    for i, v in lol_df.iterrows():
        tags1 = ''
        for x in lolChamps['data'][v.CHAMP1_y]['tags']:
            tags1 += x+'/'
        lol_df.at[i, 'CHAMP1_y'] = tags1
        tags2 = ''
        for x in lolChamps['data'][v.CHAMP2_y]['tags']:
            tags2 += x+'/'
        lol_df.at[i, 'CHAMP2_y'] = tags2
    lol_df = pd.DataFrame(lol_df.groupby(['CHAMP1_x', 'Team_x', 'CHAMP2_x', 'Year_x',
                                          'CHAMP1_y', 'CHAMP2_y'], 0, None, True, False, False)['Partidas_x', 'bResult'].agg('sum')).reset_index()

    return lol_df


def createDataFrameTags2():
    lol_df = pd.read_csv('../Results/mathUps_teste.csv')
    tagsDF = pd.read_csv('../Datasets/league of legends/champions_tags.csv')
    lolChamps = json.loads(
        open('../Datasets/league of legends/champion.json', encoding="utf8").read())
    for i, v in lol_df.iterrows():
        tags1 = ''
        for x in lolChamps['data'][v.CHAMP1_y]['tags']:
            tags1 += x+'/'
        lol_df.at[i, 'CHAMP1_y'] = tags1
        tags2 = ''
        for x in lolChamps['data'][v.CHAMP2_y]['tags']:
            tags2 += x+'/'
        lol_df.at[i, 'CHAMP2_y'] = tags2
        tags1 = ''
        for x in lolChamps['data'][v.CHAMP1_x]['tags']:
            tags1 += x+'/'
        lol_df.at[i, 'CHAMP1_x'] = tags1
        tags2 = ''
        for x in lolChamps['data'][v.CHAMP2_x]['tags']:
            tags2 += x+'/'
        lol_df.at[i, 'CHAMP2_x'] = tags2
    lol_df = pd.DataFrame(lol_df.groupby(['CHAMP1_x', 'Team_x', 'CHAMP2_x', 'Year_x',
                                          'CHAMP1_y', 'CHAMP2_y'], 0, None, True, False, False)['Partidas_x', 'bResult'].agg('sum')).reset_index()

    return lol_df


createDataFrameChampions().to_csv('../Results/ChampsHugo.csv', encoding='utf-8')
createDataFrameTags().to_csv('../Results/TagsHugo.csv', encoding='utf-8')
createDataFrameTags2().to_csv('../Results/TagsHugo2.csv', encoding='utf-8')
