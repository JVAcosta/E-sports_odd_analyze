import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))


# matchinfo_df = pd.read_csv('matchinfo_bans.csv')

# Name = "{} = '{}'"
# for c in matchinfo_df.columns:
#     print(Name.format(c.upper(), c))

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
    sub_df_columns = list(sub_df_columns)
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
    return list(result)


columns_red = red_columns
sub_red = select_sub_frame(matchinfo_df, columns_red)

columns_blue = blue_columns
sub_blue = select_sub_frame(matchinfo_df, columns_blue)


def l(x): return [x]


result_single_red = map_tuples_frames(sub_red, list(map(l, red_columns)))
result_single_blue = map_tuples_frames(sub_blue, list(map(l, blue_columns)))

result_tuples_red = map_tuples_frames(sub_red, red_tuples)
result_tuples_blue = map_tuples_frames(sub_blue, blue_tuples)


# for df in result_single_red:
#     print(df.head())
# for df in result_single_blue:
#     print(df.head())
# for df in result_tuples_red:
#     print(df.head())
# for df in result_tuple_blue:
#     print(df.head())

# test = result_tuples_red[1].groupby(
#     [REDJUNGLECHAMP, REDMIDDLECHAMP, YEAR]).sum()
# print(set(result_tuples_red[1].columns))
sum_columns = [BRESULT, RRESULT]

sum_single_red = group_by_and_sum(result_single_red, sum_columns)
sum_single_blue = group_by_and_sum(result_single_blue, sum_columns)

sum_tuples_red = group_by_and_sum(result_tuples_red, sum_columns)
sum_tuples_blue = group_by_and_sum(result_tuples_blue, sum_columns)

# for df in sum_single_red:
#     print(df.head(30))
# for df in sum_single_blue:
#     print(df.head())
# for df in sum_tuples_red:
#     print(df.head())
#print(sum_tuples_red)
# for df in sum_tuples_blue:
#     print(df.head())
# sum_all_single_red = sum_single_red
sum_all_single_red = delete_dfs_column(sum_single_red, YEAR)
sum_all_single_blue = delete_dfs_column(sum_single_blue, YEAR)

sum_all_tuples_red = delete_dfs_column(sum_tuples_red, YEAR)
sum_all_tuples_blue = delete_dfs_column(sum_tuples_blue, YEAR)

# for df in sum_all_single_red:
#     print(df.head(30))
# for df in sum_all_single_blue:
#     print(df.head())
# for df in sum_all_tuples_red:
#     print(df.head())
# for df in sum_all_tuples_blue:
#     print(df.head())

sum_all_single_red = group_by_and_sum(sum_all_single_red, sum_columns)
sum_all_single_blue = group_by_and_sum(sum_all_single_blue, sum_columns)

sum_all_tuples_red = group_by_and_sum(sum_all_tuples_red, sum_columns)
sum_all_tuples_blue = group_by_and_sum(sum_all_tuples_blue, sum_columns)


# sum_all_single_red = select_rows_by_column_value(
#     sum_all_single_red, YEAR, '2016')
# for df in sum_all_single_red:
#     print(df.head(30))
# for df in sum_all_single_blue:
#     print(df.head())
# for df in sum_all_tuples_red:
#     print(df.head())
# for df in sum_all_tuples_blue:
#     print(df.head())
# df.plot.bar(stacked=True)

sns.set()
# df.set_index(REDTOPCHAMP).plot(kind='bar', stacked=True)
# plt.show()
VICTORY = 'Victories'
DEFEAT = 'Defeats'
# df.rename(columns={BRESULT: DEFEAT,
#                    RRESULT: VICTORY}, inplace=True)

RED = 'red'
BLUE = 'blue'


def build_graph(df, side, supp_columns):
    set(df.columns) - set(sum_columns)
    colors = ['#a30016',  '#11a81d'] if side == RED else [
        '#11a81d',  '#a30016']
    graph_columns = {BRESULT: DEFEAT,
                     RRESULT: VICTORY} if side == RED else \
        {BRESULT: VICTORY, RRESULT: DEFEAT}

    new_names = df.rename(columns=graph_columns)
    new_names.set_index([REDTOPCHAMP, REDJUNGLECHAMP])\
        .plot(kind='bar', stacked=True,
              colormap=ListedColormap(sns.color_palette(colors)),
              figsize=(24, 12))

    plt.show()


# print
# upper = outliers_iqr(list(df[RRESULT]))
# upper = upper[0]
# print(upper)
# df = sum_all_tuples_blue[0]
df = sum_all_tuples_red[0]
#print(df.head())
df1 = df.loc[df[RRESULT] > 50]
#build_graph(df1, RED, sum_columns)

# df2 = df.loc[df[RRESULT] < 50]
# build_graph(df, RED, sum_columns)
# colors = ['#a30016',  '#11a81d']
# new_names = df.rename(columns={BRESULT: DEFEAT,
#                                RRESULT: VICTORY})
# new_names.set_index(REDTOPCHAMP)\
#     .plot(kind='bar', stacked=True,
#           colormap=ListedColormap(sns.color_palette(colors)),
#           figsize=(24, 12))
# plt.show()
