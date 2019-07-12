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

#new columns

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
    list_wins=sorted(list(df[column_name]))#----->>>basta mudar a lista que recebe aqui e a coluna que quer saber os outliers
    rang=len(list_wins)                                         ###
    quartil_1=list_wins[(rang+3)//4]                            ###
    quartil_3=list_wins[(3*rang+1)//4]                          ###
                                                                ###
    if quartil_1>quartil_3:                                     ###
        faixa_inter_quartil=quartil_1-quartil_3                 ###
    else:                                                       ###
        faixa_inter_quartil=quartil_3-quartil_1                 ###
                                                                ###
    outliers=quartil_3+(1.5*faixa_inter_quartil)                ###
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
    result = map(lambda df: df.loc[df[column_name] >= function(df, column_name)], df_list)
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


# for r in year_heatmap_2016:
#     print(r.head(10))


# outliers = 15

year_heatmap_2015_blue_victory = delete_dfs_column(year_heatmap_2015, RRESULT)
year_heatmap_2016_blue_victory = delete_dfs_column(year_heatmap_2016, RRESULT)
year_heatmap_2017_blue_victory = delete_dfs_column(year_heatmap_2017, RRESULT)

year_heatmap_2015_blue_victory = select_rows_by_great_value(
    year_heatmap_2015_blue_victory, BRESULT, outliers)
year_heatmap_2016_blue_victory = select_rows_by_great_value(
    year_heatmap_2016_blue_victory, BRESULT, outliers)
year_heatmap_2017_blue_victory = select_rows_by_great_value(
    year_heatmap_2017_blue_victory, BRESULT, outliers)

year_heatmap_2015_red_victory = delete_dfs_column(year_heatmap_2015, BRESULT)
year_heatmap_2016_red_victory = delete_dfs_column(year_heatmap_2016, BRESULT)
year_heatmap_2017_red_victory = delete_dfs_column(year_heatmap_2017, BRESULT)

year_heatmap_2015_red_victory = select_rows_by_great_value(
    year_heatmap_2015_red_victory, RRESULT, outliers)
year_heatmap_2016_red_victory = select_rows_by_great_value(
    year_heatmap_2016_red_victory, RRESULT, outliers)
year_heatmap_2017_red_victory = select_rows_by_great_value(
    year_heatmap_2017_red_victory, RRESULT, outliers)

# for r in year_heatmap_2015_blue_victory:
#     print(r.head(10))

jungle_2015_blue_victory = year_heatmap_2015_blue_victory[0].pivot(
    BLUEJUNGLECHAMP, REDJUNGLECHAMP, BRESULT)
jungle_2016_blue_victory = year_heatmap_2016_blue_victory[0].pivot(
    BLUEJUNGLECHAMP, REDJUNGLECHAMP, BRESULT)
jungle_2017_blue_victory = year_heatmap_2017_blue_victory[0].pivot(
    BLUEJUNGLECHAMP, REDJUNGLECHAMP, BRESULT)

middle_2015_blue_victory = year_heatmap_2015_blue_victory[1].pivot(
    BLUEMIDDLECHAMP, REDMIDDLECHAMP, BRESULT)
middle_2016_blue_victory = year_heatmap_2016_blue_victory[1].pivot(
    BLUEMIDDLECHAMP, REDMIDDLECHAMP, BRESULT)
middle_2017_blue_victory = year_heatmap_2017_blue_victory[1].pivot(
    BLUEMIDDLECHAMP, REDMIDDLECHAMP, BRESULT)

support_2015_blue_victory = year_heatmap_2015_blue_victory[2].pivot(
    BLUESUPPORTCHAMP, REDSUPPORTCHAMP, BRESULT)
support_2016_blue_victory = year_heatmap_2015_blue_victory[2].pivot(
    BLUESUPPORTCHAMP, REDSUPPORTCHAMP, BRESULT)
support_2017_blue_victory = year_heatmap_2015_blue_victory[2].pivot(
    BLUESUPPORTCHAMP, REDSUPPORTCHAMP, BRESULT)

adc_2015_blue_victory = year_heatmap_2015_blue_victory[3].pivot(
    BLUEADCCHAMP, REDADCCHAMP, BRESULT)
adc_2016_blue_victory = year_heatmap_2016_blue_victory[3].pivot(
    BLUEADCCHAMP, REDADCCHAMP, BRESULT)
adc_2017_blue_victory = year_heatmap_2017_blue_victory[3].pivot(
    BLUEADCCHAMP, REDADCCHAMP, BRESULT)

top_2015_blue_victory = year_heatmap_2015_blue_victory[4].pivot(
    BLUETOPCHAMP, REDTOPCHAMP, BRESULT)
top_2016_blue_victory = year_heatmap_2016_blue_victory[4].pivot(
    BLUETOPCHAMP, REDTOPCHAMP, BRESULT)
top_2017_blue_victory = year_heatmap_2017_blue_victory[4].pivot(
    BLUETOPCHAMP, REDTOPCHAMP, BRESULT)


jungle_2015_red_victory = year_heatmap_2015_red_victory[0].pivot(
    REDJUNGLECHAMP, BLUEJUNGLECHAMP, RRESULT)
jungle_2016_red_victory = year_heatmap_2016_red_victory[0].pivot(
    REDJUNGLECHAMP, BLUEJUNGLECHAMP, RRESULT)
jungle_2017_red_victory = year_heatmap_2017_red_victory[0].pivot(
    REDJUNGLECHAMP, BLUEJUNGLECHAMP, RRESULT)

middle_2015_red_victory = year_heatmap_2015_red_victory[1].pivot(
    REDMIDDLECHAMP, BLUEMIDDLECHAMP, RRESULT)
middle_2016_red_victory = year_heatmap_2016_red_victory[1].pivot(
    REDMIDDLECHAMP, BLUEMIDDLECHAMP, RRESULT)
middle_2017_red_victory = year_heatmap_2017_red_victory[1].pivot(
    REDMIDDLECHAMP, BLUEMIDDLECHAMP, RRESULT)

support_2015_red_victory = year_heatmap_2015_red_victory[2].pivot(
    REDSUPPORTCHAMP, BLUESUPPORTCHAMP, RRESULT)
support_2016_red_victory = year_heatmap_2015_red_victory[2].pivot(
    REDSUPPORTCHAMP, BLUESUPPORTCHAMP, RRESULT)
support_2017_red_victory = year_heatmap_2015_red_victory[2].pivot(
    REDSUPPORTCHAMP, BLUESUPPORTCHAMP, RRESULT)

adc_2015_red_victory = year_heatmap_2015_red_victory[3].pivot(
    REDADCCHAMP, BLUEADCCHAMP, RRESULT)
adc_2016_red_victory = year_heatmap_2016_red_victory[3].pivot(
    REDADCCHAMP, BLUEADCCHAMP, RRESULT)
adc_2017_red_victory = year_heatmap_2017_red_victory[3].pivot(
    REDADCCHAMP, BLUEADCCHAMP, RRESULT)

top_2015_red_victory = year_heatmap_2015_red_victory[4].pivot(
    REDTOPCHAMP, BLUETOPCHAMP, RRESULT)
top_2016_red_victory = year_heatmap_2016_red_victory[4].pivot(
    REDTOPCHAMP, BLUETOPCHAMP, RRESULT)
top_2017_red_victory = year_heatmap_2017_red_victory[4].pivot(
    REDTOPCHAMP, BLUETOPCHAMP, RRESULT)





# df = df.pivot(BLUEJUNGLECHAMP, REDJUNGLECHAMP, RRESULT)

# grid_kws = {"height_ratios": (.9, .05), "hspace": 0.8}
# f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
# sns.heatmap(df, ax=ax)

# Draw a heatmap with the numeric values in each cell


def plot_heatmap(df, title, color):
    sns.set()

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.canvas.set_window_title(title)
    ax.title.set_text(title)
    color = "Reds" if color == "red" else "Blues"
    cmap = sns.color_palette(color)
    g = sns.heatmap(df, annot=True, fmt="0.1f",
                    linewidths=0.2, ax=ax, cmap=cmap)
    g.set_facecolor('#cbd0d6')

    # plt.figure(figsize=(20, 15))

    # sns.heatmap(df, ax=ax)
    plt.show()


red, blue = 'red', 'blue'
y_2015 = 2015
y_2016 = 2016
y_2017 = 2017
middle = 'mid laner'
top = 'top laner'
jungle = 'jungler'
# title = 'Individual {} matchup at {} side in {}'
title = 'Individual victories of {} at {} side in {}'
plot_heatmap(top_2015_red_victory, title.format(top, red, y_2015), red)
plot_heatmap(top_2016_red_victory, title.format(top, red, y_2016), red)
plot_heatmap(top_2017_red_victory, title.format(top, red, y_2017), red)

plot_heatmap(jungle_2015_red_victory, title.format(jungle, red, y_2015), red)
plot_heatmap(jungle_2016_red_victory, title.format(jungle, red, y_2016), red)
plot_heatmap(jungle_2017_red_victory, title.format(jungle, red, y_2017), red)

plot_heatmap(middle_2015_red_victory, title.format(middle, red, y_2015), red)
plot_heatmap(middle_2016_red_victory, title.format(middle, red, y_2016), red)
plot_heatmap(middle_2017_red_victory, title.format(middle, red, y_2017), red)

plot_heatmap(top_2015_blue_victory, title.format(top, blue, y_2015), blue)
plot_heatmap(top_2016_blue_victory, title.format(top, blue, y_2016), blue)
plot_heatmap(top_2017_blue_victory, title.format(top, blue, y_2017), blue)

plot_heatmap(jungle_2015_blue_victory,
             title.format(jungle, blue, y_2015), blue)
plot_heatmap(jungle_2016_blue_victory,
             title.format(jungle, blue, y_2016), blue)
plot_heatmap(jungle_2017_blue_victory,
             title.format(jungle, blue, y_2017), blue)

plot_heatmap(middle_2015_blue_victory,
             title.format(middle, blue, y_2015), blue)
plot_heatmap(middle_2016_blue_victory,
             title.format(middle, blue, y_2016), blue)
plot_heatmap(middle_2017_blue_victory,
             title.format(middle, blue, y_2017), blue)
