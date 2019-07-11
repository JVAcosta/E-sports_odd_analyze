import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import transformation as tf

# graficos de caixa para os valores absolutos da vitorias das duplas
# separados por lado vermelho e azul

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

all_duos_list_df=[]
matchinfo_df = pd.read_csv('matchinfo_bans.csv')


columns_red = red_columns
sub_red = tf.select_sub_frame(matchinfo_df, columns_red)

columns_blue = blue_columns
sub_blue = tf.select_sub_frame(matchinfo_df, columns_blue)



result_tuples_red = tf.map_tuples_frames(sub_red, red_tuples)
result_tuples_blue = tf.map_tuples_frames(sub_blue, blue_tuples)

sum_columns = [BRESULT, RRESULT]

sum_tuples_red = tf.group_by_and_sum(result_tuples_red, sum_columns)
sum_tuples_blue = tf.group_by_and_sum(result_tuples_blue, sum_columns)
'''
sum_tuples_red[0].to_csv('sum_tuples_red.csv', encoding='utf-8')
sum_tuples_blue[0].to_csv('sum_tuples_blue.csv', encoding='utf-8')
'''
def add_col_tagname(df):
    if df.keys().sort_values()[2][0:4]=='blue':
        df.insert(1,'CHAMP_DUOS',df.keys().sort_values()[2][4:]+'-'+df.keys().sort_values()[3][4:])
        df['Year']=df['Year'].astype(str)
        df = df.reindex(columns=sorted(df.columns))
        df['CHAMP_DUOS_PER_YEAR']=df.iloc[1:-1,0]+'-'+df.iloc[1:-1,1]
        df.insert(1,'Team','blue')
        new_df=df.rename(index=str,   columns={df.keys().sort_values()[5]: 'CHAMP1',df.keys().sort_values()[6]:'CHAMP2','bResult':'Wins','rResult':'Defeats'})
       
    else:
        df.insert(1,'CHAMP_DUOS',df.keys().sort_values()[3][3:]+'-'+df.keys().sort_values()[4][3:])
        df['Year']=df['Year'].astype(str)
        df = df.reindex(columns=sorted(df.columns))
        df['CHAMP_DUOS_PER_YEAR']=df.iloc[1:-1,0]+'-'+df.iloc[1:-1,1]
        df.insert(1,'Team','red')
        new_df=df.rename(index=str,   columns={df.keys().sort_values()[5]: 'CHAMP1',df.keys().sort_values()[6]:'CHAMP2','rResult':'Wins','bResult':'Defeats'})
    return new_df



select_duos_df_blue=list(map(add_col_tagname,sum_tuples_blue))
select_duos_df_red=list(map(add_col_tagname,sum_tuples_red))
#extrair para um metodo!!!!!
all_duos_list_df.append(select_duos_df_blue[0])
all_duos_list_df.append(select_duos_df_blue[1])
all_duos_list_df.append(select_duos_df_blue[2])
all_duos_list_df.append(select_duos_df_blue[3])
all_duos_list_df.append(select_duos_df_red[0])
all_duos_list_df.append(select_duos_df_red[1])
all_duos_list_df.append(select_duos_df_red[2])
all_duos_list_df.append(select_duos_df_red[3])
all_duos_df = pd.concat(all_duos_list_df,sort=False)
#---------------------------
#print(select_duos_df_blue[0]['Wins'])
###############--calculo de outliers--#########################
#top_jun-15                                                 ###
#jun-mid-17                                                 ###
#jung-sup-17                                                ###
#adc-sup-22                                                 ###
list_wins=sorted(list(select_duos_df_blue[1]['Wins']))      ###
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
print(outliers)                                             ###
###############################################################

all_duos_per_year_df=all_duos_df.loc[all_duos_df['Year'].isin(['2015','2016','2017'])]

def plot_box (x_my,y_my,hue_my,df_my,title_my,colors):
    plot=sns.boxplot(x=x_my,y=y_my,hue=hue_my,data=df_my,palette=colors,width=0.3,saturation=1)
    plot.set_title(title_my)
    plt.legend()
    #plt.show()
 
plot_box('CHAMP_DUOS','Wins','Team',all_duos_df,'All_lanes_per_team',['b','r'])

plot_box('CHAMP_DUOS','Wins','Year',all_duos_per_year_df,'All_lanes_per_year',['pink','gray','green'])

top_jung_per_year_df=all_duos_per_year_df.loc[all_duos_per_year_df['CHAMP_DUOS']=='JungleChamp-TopChamp']
plot_box('CHAMP_DUOS_PER_YEAR','Wins','Team',top_jung_per_year_df,'All_years_JUNG_TOP',['b','r'])

jung_mid_per_year_df=all_duos_per_year_df.loc[all_duos_per_year_df['CHAMP_DUOS']=='JungleChamp-MiddleChamp']
plot_box('CHAMP_DUOS_PER_YEAR','Wins','Team',jung_mid_per_year_df,'All_years_JUNG_MID',['b','r'])

jung_sup_per_year_df=all_duos_per_year_df.loc[all_duos_per_year_df['CHAMP_DUOS']=='JungleChamp-SupportChamp']
plot_box('CHAMP_DUOS_PER_YEAR','Wins','Team',jung_sup_per_year_df,'All_years_JUNG_SUP',['b','r'])

adc_sup_per_year_df=all_duos_per_year_df.loc[all_duos_per_year_df['CHAMP_DUOS']=='ADCChamp-SupportChamp']
plot_box('CHAMP_DUOS_PER_YEAR','Wins','Team',adc_sup_per_year_df,'All_years_ADC_SUP',['b','r'])


