
import pandas as pd
import json
import csv


def start():
    bestCombination = {}

    lol_df = pd.read_csv('../datasets/LeagueofLegends.csv', thousands=",")
    dic_bResult = ((lol_df[['bResult']]).to_json())
    dic_blueTopChamp = ((lol_df[['blueTopChamp']]).to_json())
    dic_blueMiddleChamp = ((lol_df[['blueMiddleChamp']]).to_json())
    dic_blueJungleChamp = ((lol_df[['blueJungleChamp']]).to_json())
    dic_blueSupportChamp = ((lol_df[['blueSupportChamp']]).to_json())
    dic_blueADCChamp = ((lol_df[['blueADCChamp']]).to_json())
    dic_year = ((lol_df[['Year']]).to_json())
    dic_season = ((lol_df[['Season']]).to_json())

    dic_rResult = ((lol_df[['rResult']]).to_json())
    dic_redTopChamp = ((lol_df[['redTopChamp']]).to_json())
    dic_redMiddleChamp = ((lol_df[['redMiddleChamp']]).to_json())
    dic_redJungleChamp = ((lol_df[['redJungleChamp']]).to_json())
    dic_redSupportChamp = ((lol_df[['redSupportChamp']]).to_json())
    dic_redADCChamp = ((lol_df[['redADCChamp']]).to_json())
    dic_year = ((lol_df[['Year']]).to_json())
    dic_season = ((lol_df[['Season']]).to_json())

    dicbResult = json.loads(dic_bResult)
    dicblueTopChamp = json.loads(dic_blueTopChamp)
    dicblueMiddleChamp = json.loads(dic_blueMiddleChamp)
    dicblueJungleChamp = json.loads(dic_blueJungleChamp)
    dicblueSupportChamp = json.loads(dic_blueSupportChamp)
    dicblueADCChamp = json.loads(dic_blueADCChamp)
    dicyear = json.loads(dic_year)
    dicseason = json.loads(dic_season)

    dicrResult = json.loads(dic_rResult)
    dicredTopChamp = json.loads(dic_redTopChamp)
    dicredMiddleChamp = json.loads(dic_redMiddleChamp)
    dicredJungleChamp = json.loads(dic_redJungleChamp)
    dicredSupportChamp = json.loads(dic_redSupportChamp)
    dicredADCChamp = json.loads(dic_redADCChamp)
    dicyear = json.loads(dic_year)
    dicseason = json.loads(dic_season)

    def addToDic(combination, champ1, champ2, result, year, season, team, champ1_posi, champ2_posi):
        if result == 1:
            try:
                dictionary = combination[team+"," +
                                         champ1+","+champ2+','+year+','+season]
                # print dictionary['DEFEAT'] + "=== " + dictionary['TOTALPLAYED']
                dictionary['VICTORY'] += 1
                dictionary['TOTALPLAYED'] += 1
                dictionary['PERCENTVICTORY'] = dictionary['VICTORY'] / \
                    dictionary['TOTALPLAYED']
                dictionary['PERCENTDEFEAT'] = dictionary['DEFEAT'] / \
                    dictionary['TOTALPLAYED']

            except:

                combination[team+","+champ1+"," +
                            champ2+','+year+','+season] = {}
                dictionary = combination[team+"," +
                                         champ1+","+champ2+','+year+','+season]
                dictionary['CHAMP1'] = champ1
                dictionary['CHAMP2'] = champ2
                dictionary['CHAMP1_POSITION'] = champ1_posi
                dictionary['CHAMP2_POSITION'] = champ2_posi
                dictionary['VICTORY'] = 1
                dictionary['DEFEAT'] = 0
                dictionary['TOTALPLAYED'] = 1
                dictionary['PERCENTVICTORY'] = 1.0
                dictionary['PERCENTDEFEAT'] = 0.0
                dictionary['YEAR'] = year
                dictionary['SEASON'] = season
                dictionary['TEAM'] = team

            return combination
        else:
            try:
                dictionary = combination[team+"," +
                                         champ1+","+champ2+','+year+','+season]
                dictionary['DEFEAT'] += 1
                dictionary['TOTALPLAYED'] += 1
                dictionary['PERCENTVICTORY'] = dictionary['VICTORY'] / \
                    dictionary['TOTALPLAYED']
                dictionary['PERCENTDEFEAT'] = dictionary['DEFEAT'] / \
                    dictionary['TOTALPLAYED']

            except:

                combination[team+","+champ1+"," +
                            champ2+','+year+','+season] = {}
                dictionary = combination[team+"," +
                                         champ1+","+champ2+','+year+','+season]
                dictionary['CHAMP1'] = champ1
                dictionary['CHAMP2'] = champ2
                dictionary['CHAMP1_POSITION'] = champ1_posi
                dictionary['CHAMP2_POSITION'] = champ2_posi
                dictionary['VICTORY'] = 0
                dictionary['DEFEAT'] = 1
                dictionary['TOTALPLAYED'] = 1
                dictionary['PERCENTVICTORY'] = 0.0
                dictionary['PERCENTDEFEAT'] = 1.0
                dictionary['YEAR'] = year
                dictionary['SEASON'] = season
                dictionary['TEAM'] = team

            return combination

    for x in range(0, len(dicbResult['bResult'])):
        a = addToDic(bestCombination, str(dicblueTopChamp['blueTopChamp'][str(x)]), str(dicblueJungleChamp['blueJungleChamp'][str(
            x)]), dicbResult['bResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Blue', 'TOP_LANER', 'JUNGLER')
        bestCombination["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Blue,"+str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicblueJungleChamp['blueJungleChamp'][str(x)]), str(dicblueMiddleChamp['blueMiddleChamp'][str(
            x)]), dicbResult['bResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Blue', 'JUNGLER', 'MID_LANER')
        bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicblueJungleChamp['blueJungleChamp'][str(x)]), str(dicblueSupportChamp['blueSupportChamp'][str(
            x)]), dicbResult['bResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Blue', 'JUNGLER', 'SUPPORT')
        bestCombination["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Blue,"+str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicblueADCChamp['blueADCChamp'][str(x)]), str(dicblueSupportChamp['blueSupportChamp'][str(
            x)]), dicbResult['bResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Blue', 'AD_CARRY', 'SUPPORT')
        bestCombination["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Blue,"+str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicredTopChamp['redTopChamp'][str(x)]), str(dicredJungleChamp['redJungleChamp'][str(
            x)]), dicrResult['rResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Red', 'TOP_LANER', 'JUNGLER')
        bestCombination["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Red,"+str(dicredTopChamp['redTopChamp'][str(x)])+","+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicredJungleChamp['redJungleChamp'][str(x)]), str(dicredMiddleChamp['redMiddleChamp'][str(
            x)]), dicrResult['rResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Red', 'JUNGLER', 'MID_LANER')
        bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredMiddleChamp['redMiddleChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicredJungleChamp['redJungleChamp'][str(x)]), str(dicredSupportChamp['redSupportChamp'][str(
            x)]), dicrResult['rResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Red', 'JUNGLER', 'SUPPORT')
        bestCombination["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Red,"+str(dicredJungleChamp['redJungleChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

        a = addToDic(bestCombination, str(dicredADCChamp['redADCChamp'][str(x)]), str(dicredSupportChamp['redSupportChamp'][str(
            x)]), dicrResult['rResult'][str(x)], str(dicyear['Year'][str(x)]), str(dicseason['Season'][str(x)]), 'Red', 'AD_CARRY', 'SUPPORT')
        bestCombination["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(
            x)])] = a["Red,"+str(dicredADCChamp['redADCChamp'][str(x)])+","+str(dicredSupportChamp['redSupportChamp'][str(x)])+","+str(dicyear['Year'][str(x)])+","+str(dicseason['Season'][str(x)])]

    arqName = "champ_duos"
    with open("../treasures/"+arqName+'.csv', 'w') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(
            f, bestCombination["Blue,Irelia,RekSai,2015,Spring"].keys())
        w.writeheader()
        for key in bestCombination.keys():
            w.writerow(bestCombination[key])


start()
