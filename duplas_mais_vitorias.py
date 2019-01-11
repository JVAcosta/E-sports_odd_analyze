import pandas as pd
import json
arqSaida = open('saida.txt', "w")
bestCombination={}
bestCombination['Top/Jung']={}
bestCombination['Jung/Mid']={}
bestCombination['Jung/Sup']={}
bestCombination['ADC/Sup']={}

lol_df = pd.read_csv('LeagueofLegends.csv', thousands=",")
dic_bResult          = ((lol_df[['bResult']]).to_json())
dic_blueTopChamp     = ((lol_df[['blueTopChamp']]).to_json())
dic_blueMiddleChamp  = ((lol_df[['blueMiddleChamp']]).to_json())
dic_blueJungleChamp  = ((lol_df[['blueJungleChamp']]).to_json())
dic_blueSupportChamp = ((lol_df[['blueSupportChamp']]).to_json())
dic_blueADCChamp     = ((lol_df[['blueADCChamp']]).to_json())

dicbResult          = json.loads(dic_bResult)
dicblueTopChamp     = json.loads(dic_blueTopChamp)
dicblueMiddleChamp  = json.loads(dic_blueMiddleChamp)
dicblueJungleChamp  = json.loads(dic_blueJungleChamp)
dicblueSupportChamp = json.loads(dic_blueSupportChamp)
dicblueADCChamp     = json.loads(dic_blueADCChamp)



for x in range(0,len(dicbResult['bResult'])):
    if dicbResult['bResult'][str(x)]==1:
        try:
            bestCombination['Top/Jung'][str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])]=bestCombination['Top/Jung'][str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])]+1
        except:
            bestCombination['Top/Jung'][str(dicblueTopChamp['blueTopChamp'][str(x)])+","+str(dicblueJungleChamp['blueJungleChamp'][str(x)])]=1
        try:
            bestCombination['Jung/Mid'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])]=bestCombination['Jung/Mid'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])]+1
        except:
            bestCombination['Jung/Mid'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueMiddleChamp['blueMiddleChamp'][str(x)])]=1
        try:
            bestCombination['Jung/Sup'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]=bestCombination['Jung/Sup'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]+1
        except:
            bestCombination['Jung/Sup'][str(dicblueJungleChamp['blueJungleChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]=1
        try:
            bestCombination['ADC/Sup'][str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]=bestCombination['ADC/Sup'][str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]+1
        except:
            bestCombination['ADC/Sup'][str(dicblueADCChamp['blueADCChamp'][str(x)])+","+str(dicblueSupportChamp['blueSupportChamp'][str(x)])]=1
        
arqSaida.write(str(bestCombination))
'''
for item in sorted(bestCombination['Top/Jung'], key = bestCombination['Top/Jung'].get,reverse= True):
    listakrai.append(bestCombination['Top/Jung'][item])
'''
        
        




