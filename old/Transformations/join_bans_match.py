import pandas as pd
#from Datasets.Kaggle.datasets import LeagueofLegends_df
# from functions import splitDfBySeasonAndYear

bans_df = pd.read_csv(
    '/home/victor_costa/Python/E-sports_odd_analyze/Datasets/Kaggle/bans.csv')
matchinfo_df = pd.read_csv(
    '/home/victor_costa/Python/E-sports_odd_analyze/Datasets/Kaggle/matchinfo.csv')
df_result = pd.merge(matchinfo_df, bans_df, on='Address', how='inner')
df_result = pd.DataFrame(df_result).reset_index().set_index('index')
print(pd.DataFrame(df_result).reset_index().set_index('index'))
df_result.to_csv('matchinfo_bans.csv', encoding='utf-8')
