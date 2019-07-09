import pandas as pd


df_champ_duos = pd.read_csv("../treasures/champ_duos.csv")
df_champ_full = pd.read_csv("../treasures/skill_treasure.csv")

df_tags_duos = df_champ_duos.merge(
    df_champ_full, left_on='CHAMP2', right_on='champion', how="inner").drop(['champion'], axis=1)

df_tags_duos.rename(
    columns={'type': 'CHAMP1_SKILL_TYPE'}, inplace=True)

df_tags_duos = df_tags_duos.merge(
    df_champ_full, left_on='CHAMP1', right_on='champion', how="inner").drop(['champion'], axis=1)

df_tags_duos.rename(
    columns={'type': 'CHAMP2_SKILL_TYPE'}, inplace=True)

df_tags_duos.drop(['CHAMP1', 'CHAMP2'], axis=1, inplace=True)
# df_tags_duos = df_tags_duos.loc[(df_tags_duos['YEAR'].isin([2016, 2017]))]
df_tags_duos = df_tags_duos.groupby(['CHAMP1_POSITION', 'CHAMP2_POSITION', 'YEAR', 'SEASON', 'TEAM', 'CHAMP1_SKILL_TYPE', 'CHAMP2_SKILL_TYPE'],
                                    as_index=False)['VICTORY', 'DEFEAT', 'TOTALPLAYED'].sum()
df_tags_duos['PERCENTVICTORY'] = df_tags_duos.VICTORY/df_tags_duos.TOTALPLAYED

df_tags_duos['PERCENTDEFEAT'] = df_tags_duos.DEFEAT/df_tags_duos.TOTALPLAYED

# print(df_tags_duos.head())
df_tags_duos.to_csv('../treasures/skill_duos.csv', encoding='utf-8', index=False)
