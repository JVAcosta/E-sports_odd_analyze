import pandas as pd
from itertools import product


def locBySeasonAndYear(x):
    year = x[0]
    season = x[1]
    df = x[2]
    season_column = "Season"
    years_column = "Year"
    locked = df.loc[(df[season_column].isin([season]))
                    & (df[years_column].isin([year]))]
    return locked


def splitBySeasonAndYear(df, years, seasons):
    inputs = list(product(years, seasons, [df]))
    splited = map(locBySeasonAndYear, inputs)
    return list(splited)


def splitDfBySeasonAndYear(df):
    years = [2014, 2015, 2016, 2017, 2018]
    seasons = ['Spring', 'Summer']
    return splitBySeasonAndYear(df, years, seasons)


# df = pd.read_csv("../Datasets/Kaggle/LeagueofLegends.csv")
# print(splitDfBySeasonAndYear(df))
