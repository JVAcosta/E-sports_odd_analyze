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


heatmap_tuples = [[BLUEJUNGLECHAMP, REDJUNGLECHAMP],
                  [BLUEMIDDLECHAMP, REDMIDDLECHAMP],
                  [BLUESUPPORTCHAMP, REDSUPPORTCHAMP],
                  [BLUEADCCHAMP, REDSUPPORTCHAMP],
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
years = [2014, 2015, 2016, 2017, 2018]
year_heatmap = select_rows_by_column_value(
    sum_tuples_heatmap, YEAR, years[2])

# for r in year_heatmap:
#     print(r.head(10))

sum_all_tuples_heatmap = delete_dfs_column(year_heatmap, YEAR)
# for r in sum_all_tuples_heatmap:
#     print(r.head(10))

sum_all_tuples_heatmap = group_by_and_sum(sum_all_tuples_heatmap, sum_columns)
# for r in sum_all_tuples_heatmap:
#     print(r.head(4000))


sns.set()

# Load the example flights dataset and conver to long-form


# print(df.head())
df = delete_dfs_column(sum_all_tuples_heatmap, BRESULT)
df = df[0]
df = df.loc[df[RRESULT] > 5]


df = df.pivot(BLUEJUNGLECHAMP, REDJUNGLECHAMP, RRESULT)

# grid_kws = {"height_ratios": (.9, .05), "hspace": 0.8}
# f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
# sns.heatmap(df, ax=ax)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(12, 8))
cmap = sns.dark_palette("purple")
g = sns.heatmap(df, annot=True, fmt="0.1f",
                linewidths=0.2, ax=ax, cmap=cmap)
g.set_facecolor('xkcd:gray')

# plt.figure(figsize=(20, 15))

# sns.heatmap(df, ax=ax)
plt.show()
