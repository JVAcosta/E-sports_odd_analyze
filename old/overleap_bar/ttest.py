import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import json
from scipy import stats

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


# for r in year_heatmap_2017:
#     print(r.head(10))

jungle_2017_blue = year_heatmap_2017[0].loc[:,  [BLUEJUNGLECHAMP, BRESULT]]
jungle_2017_red = year_heatmap_2017[0].loc[:,  [REDJUNGLECHAMP, RRESULT]]

mid_2017_blue = year_heatmap_2017[1].loc[:,  [BLUEMIDDLECHAMP, BRESULT]]
mid_2017_red = year_heatmap_2017[1].loc[:,  [REDMIDDLECHAMP, RRESULT]]

supp_2017_blue = year_heatmap_2017[2].loc[:,  [BLUESUPPORTCHAMP, BRESULT]]
supp_2017_red = year_heatmap_2017[2].loc[:,  [REDSUPPORTCHAMP, RRESULT]]

adc_2017_blue = year_heatmap_2017[3].loc[:,  [BLUEADCCHAMP, BRESULT]]
adc_2017_red = year_heatmap_2017[3].loc[:,  [REDADCCHAMP, RRESULT]]

top_2017_blue = year_heatmap_2017[4].loc[:,  [BLUETOPCHAMP, BRESULT]]
top_2017_red = year_heatmap_2017[4].loc[:,  [REDTOPCHAMP, RRESULT]]


arq = open("champion.json", "r")
json_s = arq.read()
json_load = json.loads(json_s)
champs = json_load['data'].keys()


def f(x): return '/'.join(json_load['data'][x]['tags'])


tags = list(map(lambda x: f, champs))

# r = json_load['data'][champ]['tags']
jungle_2017_blue[BLUEJUNGLECHAMP] = jungle_2017_blue[BLUEJUNGLECHAMP].apply(f)
jungle_2017_red[REDJUNGLECHAMP] = jungle_2017_red[REDJUNGLECHAMP].apply(f)

tags_red = set(jungle_2017_red[REDJUNGLECHAMP])
tags_blue = set(jungle_2017_blue[BLUEJUNGLECHAMP])
tags_i_jungle = tags_blue.intersection(tags_red)

mid_2017_blue[BLUEMIDDLECHAMP] = mid_2017_blue[BLUEMIDDLECHAMP].apply(f)
mid_2017_red[REDMIDDLECHAMP] = mid_2017_red[REDMIDDLECHAMP].apply(f)

tags_red = set(mid_2017_red[REDMIDDLECHAMP])
tags_blue = set(mid_2017_blue[BLUEMIDDLECHAMP])
tags_i_mid = tags_blue.intersection(tags_red)

supp_2017_blue[BLUESUPPORTCHAMP] = supp_2017_blue[BLUESUPPORTCHAMP].apply(f)
supp_2017_red[REDSUPPORTCHAMP] = supp_2017_red[REDSUPPORTCHAMP].apply(f)

tags_red = set(supp_2017_red[REDSUPPORTCHAMP])
tags_blue = set(supp_2017_blue[BLUESUPPORTCHAMP])
tags_i_supp = tags_blue.intersection(tags_red)

adc_2017_blue[BLUEADCCHAMP] = adc_2017_blue[BLUEADCCHAMP].apply(f)
adc_2017_red[REDADCCHAMP] = adc_2017_red[REDADCCHAMP].apply(f)

tags_red = set(adc_2017_red[REDADCCHAMP])
tags_blue = set(adc_2017_blue[BLUEADCCHAMP])
tags_i_adc = tags_blue.intersection(tags_red)

top_2017_blue[BLUETOPCHAMP] = top_2017_blue[BLUETOPCHAMP].apply(f)
top_2017_red[REDTOPCHAMP] = top_2017_red[REDTOPCHAMP].apply(f)

tags_red = set(top_2017_red[REDTOPCHAMP])
tags_blue = set(top_2017_blue[BLUETOPCHAMP])
tags_i_top = tags_blue.intersection(tags_red)


def test_t(dfB, dfR, tag, BLUECHAMP, REDCHAMP):
    testB = dfB.loc[dfB[BLUECHAMP] == tag]
    testR = dfR.loc[dfR[REDCHAMP] == tag]
    sampleB = testB[BRESULT]
    sampleR = testR[RRESULT]
    r = stats.ttest_ind(sampleB, sampleR)
    return ({'BLUECHAMP': BLUECHAMP, 'REDCHAMP': REDADCCHAMP, "TAG_TO_COMPARE": tag, 'statistic': r[0], 'pvalue': r[1]})


def test_tags(dfB, dfR, tags,  BLUECHAMP, REDCHAMP):
    results = map(lambda t: test_t(dfB, dfR, t, BLUECHAMP, REDCHAMP), tags)
    return list(results)


r_jungle = test_tags(jungle_2017_blue, jungle_2017_red,
                     tags_i_jungle, BLUEJUNGLECHAMP, REDJUNGLECHAMP)
df = pd.DataFrame(r_jungle)
df.to_csv('jungler_ttest_ind.csv', encoding='utf-8', index=False)

r_mid = test_tags(mid_2017_blue, mid_2017_red, tags_i_mid,
                  BLUEMIDDLECHAMP, REDMIDDLECHAMP)
df = pd.DataFrame(r_mid)
df.to_csv('mid_ttest_ind.csv', encoding='utf-8', index=False)

r_supp = test_tags(supp_2017_blue, supp_2017_red, tags_i_supp,
                   BLUESUPPORTCHAMP, REDSUPPORTCHAMP)
df = pd.DataFrame(r_supp)
df.to_csv('support_ttest_ind.csv', encoding='utf-8', index=False)

r_adc = test_tags(adc_2017_blue, adc_2017_red,
                  tags_i_adc, BLUEADCCHAMP, REDADCCHAMP)
df = pd.DataFrame(r_adc)
df.to_csv('adc_ttest_ind.csv', encoding='utf-8', index=False)

r_top = test_tags(top_2017_blue, top_2017_red,
                  tags_i_top, BLUETOPCHAMP, REDTOPCHAMP)
df = pd.DataFrame(r_top)
df.to_csv('top_ttest_ind.csv', encoding='utf-8', index=False)


# print('MID ===>')
# for r in r_mid:

#     print(r)

# print('SUPP ===>')
# for r in r_supp:

#     print(r)

# print('ADC ===>')
# for r in r_adc:

#     print(r)

# print('TOP ===>')
# for r in r_top:

#     print(r)
# df = pd.DataFrame(r_top)
# print(df)
