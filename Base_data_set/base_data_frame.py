import pandas as pd

#from Datasets.Kaggle.datasets import LeagueofLegends_df
# from functions import splitDfBySeasonAndYear

bans_df = pd.read_csv(
    '/home/victor_costa/Python/E-sports_odd_analyze/Datasets/Kaggle/bans.csv')
matchinfo_df = pd.read_csv(
    '/home/victor_costa/Python/E-sports_odd_analyze/Datasets/Kaggle/matchinfo.csv')
champ_class = pd.read_csv(
    '/home/victor_costa/Python/E-sports_odd_analyze/Datasets/league of legends/champions_tags.csv')


def format_tag(tag):
    string = tag.replace("['", '')
    string = string.replace("', '", '/')
    string = string.replace("']", '')
    return string


BLUETOP = 'blueTop'
BLUETOPCHAMP = 'blueTopChamp'
BLUEJUNGLE = 'blueJungle'
BLUEJUNGLECHAMP = 'blueJungleChamp'
BLUEMIDDLE = 'blueMiddle'
BLUEMIDDLECHAMP = 'blueMiddleChamp'
BLUEADC = 'blueADC'
BLUEADCCHAMP = 'blueADCChamp'
BLUESUPPORT = 'blueSupport'
BLUESUPPORTCHAMP = 'blueSupportChamp'
REDTOP = 'redTop'
REDTOPCHAMP = 'redTopChamp'
REDJUNGLE = 'redJungle'
REDJUNGLECHAMP = 'redJungleChamp'
REDMIDDLE = 'redMiddle'
REDMIDDLECHAMP = 'redMiddleChamp'
REDADC = 'redADC'
REDADCCHAMP = 'redADCChamp'
REDSUPPORT = 'redSupport'
REDSUPPORTCHAMP = 'redSupportChamp'

red_columns = [REDTOPCHAMP,
               REDJUNGLECHAMP,
               REDMIDDLECHAMP,
               REDADCCHAMP,
               REDSUPPORTCHAMP]

blue_columns = [BLUETOPCHAMP,  # blueTopChampx
                BLUEJUNGLECHAMP,
                BLUEMIDDLECHAMP,
                BLUEADCCHAMP,
                BLUESUPPORTCHAMP]

champ_columns = red_columns + blue_columns

df_result = pd.merge(matchinfo_df, bans_df, on='Address', how='inner')
df_result = pd.DataFrame(df_result).reset_index().set_index('index')
champ_class['tag'] = champ_class['tag'].apply(format_tag)
champ_class = champ_class.reset_index().set_index('index')
champ_class = champ_class.drop('Unnamed: 0', axis=1)

# print(champ_class.head())
# print(df_result.columns)
# df_result.to_csv('matchinfo_bans.csv', encoding='utf-8')
