import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

INDEX = 'index'
LEAGUE = 'League'
YEAR = 'Year'
SEASON = 'Season'
TYPE = 'Type'
BLUETEAMTAG = 'blueTeamTag'
BRESULT = 'bResult'
RRESULT = 'rResult'
REDTEAMTAG = 'redTeamTag'
GAMELENGTH = 'gamelength'
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
ADDRESS = 'Address'
TEAM = 'Team'
BAN_1 = 'ban_1'
BAN_2 = 'ban_2'
BAN_3 = 'ban_3'
BAN_4 = 'ban_4'
BAN_5 = 'ban_5'


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

# new columns

TOTAL_PLAYED = 'totalPlayed'

red_columns = [REDTOPCHAMP,
               REDJUNGLECHAMP,
               REDMIDDLECHAMP,
               REDADCCHAMP,
               REDSUPPORTCHAMP]

red_tuples = [[REDJUNGLECHAMP, REDTOPCHAMP],
              [REDJUNGLECHAMP, REDMIDDLECHAMP],
              [REDJUNGLECHAMP, REDSUPPORTCHAMP],
              [REDADCCHAMP, REDSUPPORTCHAMP]]

blue_columns = [BLUETOPCHAMP,
                BLUEJUNGLECHAMP,
                BLUEMIDDLECHAMP,
                BLUEADCCHAMP,
                BLUESUPPORTCHAMP]

blue_tuples = [[BLUEJUNGLECHAMP, BLUETOPCHAMP],
               [BLUEJUNGLECHAMP, BLUEMIDDLECHAMP],
               [BLUEJUNGLECHAMP, BLUESUPPORTCHAMP],
               [BLUEADCCHAMP, BLUESUPPORTCHAMP]]

support_columns = [BRESULT,
                   RRESULT,
                   YEAR]


matchinfo_df = pd.read_csv('matchinfo_bans.csv')


def outliers(df, column_name):
    # ----->>>basta mudar a lista que recebe aqui e a coluna que quer saber os outliers
    list_wins = sorted(list(df[column_name]))
    rang = len(list_wins)
    quartil_1 = list_wins[(rang+3)//4]
    quartil_3 = list_wins[(3*rang+1)//4]
    ###
    if quartil_1 > quartil_3:
        faixa_inter_quartil = quartil_1-quartil_3
    else:
        faixa_inter_quartil = quartil_3-quartil_1
        ###
    outliers = quartil_3+(1.5*faixa_inter_quartil)
    return outliers


def select_sub_frame(df, sub_df_columns, supp_col=support_columns):
    # sub_df_columns = list(sub_df_columns)
    sub_frame = df.loc[:, sub_df_columns + supp_col]
    return sub_frame


def map_tuples_frames(df, champ_tuples):
    result = map(lambda champ_tuple: select_sub_frame(
        df, champ_tuple), champ_tuples)
    return list(result)


def group_by_and_sum(df_list, sum_columns):

    result = map(lambda df: df.groupby(
        list(set(df.columns) - set(sum_columns))).sum(), df_list)

    result = map(lambda df: df.reset_index(), result)

    return list(result)


def delete_dfs_column(df_list, column_name):
    result = map(lambda df: df.drop(column_name, axis=1), df_list)
    return list(result)


def select_rows_by_column_value(df_list, column_name, column_value):
    result = map(lambda df: df.loc[df[column_name] == column_value], df_list)
    return result


def select_rows_by_great_value(df_list, column_name, function):
    result = map(lambda df: df.loc[df[column_name]
                                   >= function(df, column_name)], df_list)
    return list(result)


heatmap_tuples = [[BLUEJUNGLECHAMP, REDJUNGLECHAMP],
                  [BLUEMIDDLECHAMP, REDMIDDLECHAMP],
                  [BLUESUPPORTCHAMP, REDSUPPORTCHAMP],
                  [BLUEADCCHAMP, REDADCCHAMP],
                  [BLUETOPCHAMP, REDTOPCHAMP]]


columns_heatmap = red_columns + blue_columns
sub_heatmap = select_sub_frame(matchinfo_df, columns_heatmap)
# print(sub_heatmap.head())

result_tuples_heatmap = map_tuples_frames(sub_heatmap, heatmap_tuples)
# for r in result_tuples_heatmap:
#     print(r.head(10))
sum_columns = [BRESULT, RRESULT]

sum_tuples_heatmap = group_by_and_sum(result_tuples_heatmap, sum_columns)

# for r in sum_tuples_heatmap:
#     print(r.head(10))

# years = [2014, 2015, 2016, 2017, 2018]

year_heatmap_2015 = select_rows_by_column_value(sum_tuples_heatmap, YEAR, 2015)
year_heatmap_2016 = select_rows_by_column_value(sum_tuples_heatmap, YEAR, 2016)
year_heatmap_2017 = select_rows_by_column_value(sum_tuples_heatmap, YEAR, 2017)

# for r in year_heatmap_2016:
#     print(r.head(10))

year_heatmap_2015 = delete_dfs_column(year_heatmap_2015, YEAR)
year_heatmap_2016 = delete_dfs_column(year_heatmap_2016, YEAR)
year_heatmap_2017 = delete_dfs_column(year_heatmap_2017, YEAR)


year_heatmap_2017[0]

jungle_2017_blue = year_heatmap_2017[0].loc[:,  [BLUEJUNGLECHAMP, BRESULT]]
print(jungle_2017_blue)
