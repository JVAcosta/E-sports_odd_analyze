import pandas as pd
from Datasets.Kaggle.datasets import LeagueofLegends_df


def createDataFrames(team,champ1Position,champ2Position):
    
    lol_df = LeagueofLegends_df
    part_df=lol_df.loc[1:30,[team+champ1Position+'Champ',team+champ2Position+'Champ','Year','Season',team[0]+'Result']]
    part_df.insert(1,'CHAMP1_POSITION',champ1Position)
    part_df.insert(1,'CHAMP2_POSITION',champ2Position)
    part_df.insert(1, 'Partidas', 1)
    part_df.insert(1, 'Team', team)
    return1=part_df.rename(index=str,   columns={team+champ1Position+'Champ':'CHAMP1',team+champ2Position+'Champ':"CHAMP2",'CHAMP1_POSITION':'CHAMP1_POS','CHAMP2_POSITION':'CHAMP2_POS'})
    part1_df=return1.groupby(['CHAMP1','CHAMP2','Year','Season','Team','CHAMP1_POS','CHAMP2_POS'],0,None,True,False,False).sum()
    return_df=part1_df.rename(index=str,   columns={team[0]+"Result":"Wins", "Partidas":"Total_Played","Team":"Team"})
    return return_df

def start():
    frames=[]
    duplaBlue1=createDataFrames('blue','Top','Jungle')
    frames.append(duplaBlue1)
    duplaBlue2=createDataFrames('blue','Jungle','Middle')
    frames.append(duplaBlue2)
    duplaBlue3=createDataFrames('blue','Jungle','Support')
    frames.append(duplaBlue3)
    duplaBlue4=createDataFrames('blue','ADC','Support')
    frames.append(duplaBlue4)
    duplaRed1=createDataFrames('red','Top','Jungle')
    frames.append(duplaRed1)
    duplaRed2=createDataFrames('red','Jungle','Middle')
    frames.append(duplaRed2)
    duplaRed3=createDataFrames('red','Jungle','Support')
    frames.append(duplaRed3)
    duplaRed4=createDataFrames('red','ADC','Support')
    frames.append(duplaRed4)


    result=pd.concat(frames)
    result.to_csv('../Datasets/champ_duos/selected_duos.csv', encoding='utf-8')
start()



