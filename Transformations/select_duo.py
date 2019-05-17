import pandas as pd
# from Datasets.Kaggle.datasets import LeagueofLegends_df
from functions import splitDfBySeasonAndYear


def createDataFrames(team, champ1Position, champ2Position, df):

    # lol_df = pd.read_csv('..\Datasets\Kaggle\LeagueofLegends.csv')
    part_df = df.loc[:, [team+champ1Position+'Champ', team +
                         champ2Position+'Champ', 'Year', 'Season', team[0]+'Result']]
    part_df.insert(1, 'CHAMP1_POSITION', champ1Position)
    part_df.insert(1, 'CHAMP2_POSITION', champ2Position)
    part_df.insert(1, 'Partidas', 1)
    part_df.insert(1, 'Team', team)
    return1 = part_df.rename(index=str,   columns={team+champ1Position+'Champ': 'CHAMP1', team +
                                                   champ2Position+'Champ': "CHAMP2", 'CHAMP1_POSITION': 'CHAMP1_POS', 'CHAMP2_POSITION': 'CHAMP2_POS'})
    part1_df = return1.groupby(['CHAMP1', 'CHAMP2', 'Year', 'Season', 'Team',
                                'CHAMP1_POS', 'CHAMP2_POS'], 0, None, True, False, False).sum()
    part1_df = pd.DataFrame(part1_df).reset_index()
    return_df = part1_df.rename(index=str,   columns={
                                team[0]+"Result": "Wins", "Partidas": "Total_Played", "Team": "Team"})
    return return_df


def start(df):
    frames = []
    duplaBlue1 = createDataFrames('blue', 'Top', 'Jungle', df)
    frames.append(duplaBlue1)
    duplaBlue2 = createDataFrames('blue', 'Jungle', 'Middle', df)
    frames.append(duplaBlue2)
    duplaBlue3 = createDataFrames('blue', 'Jungle', 'Support', df)
    frames.append(duplaBlue3)
    duplaBlue4 = createDataFrames('blue', 'ADC', 'Support', df)
    frames.append(duplaBlue4)
    duplaRed1 = createDataFrames('red', 'Top', 'Jungle', df)
    frames.append(duplaRed1)
    duplaRed2 = createDataFrames('red', 'Jungle', 'Middle', df)
    frames.append(duplaRed2)
    duplaRed3 = createDataFrames('red', 'Jungle', 'Support', df)
    frames.append(duplaRed3)
    duplaRed4 = createDataFrames('red', 'ADC', 'Support', df)
    frames.append(duplaRed4)

    result = pd.concat(frames)
    print(result.head())
    season = str(result['Season'].tolist()[0])
    year = str(result['Year'].tolist()[0])
    result.to_csv('../Results/selected_duos_'+year +
                  '_'+season+'.csv', encoding='utf-8')


lol_df = pd.read_csv('../Datasets/Kaggle/LeagueofLegends.csv')
splitedDfs = splitDfBySeasonAndYear(lol_df)
# result = map(start, splitedDfs)
result = [start(x) for x in splitedDfs if not(x.empty)]
# print(len(splitedDfs))
# for i in range(len(splitedDfs)):
#     dfi = splitedDfs[i]
#     if not(dfi.empty):
#         start(dfi)
