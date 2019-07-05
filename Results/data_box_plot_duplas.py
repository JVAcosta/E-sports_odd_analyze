import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# graficos de caixa para os valores absolutos da vitorias das duplas
# separados por lado vermelho e azul

    
    
df = pd.read_csv("selected_duos_teste.csv")


new_df=df
new_df.insert(1, 'CHAMP_DUOS', df.iloc[1:-1,6]+'-'+df.iloc[1:-1,7])
new_df2=new_df
new_df2.insert(1, 'Relative_Wins(%)', (new_df2.iloc[1:-1,10]/new_df2.iloc[1:-1,9])*100  )
new_df3=new_df2.loc[(df['Total_Played'] >= 10) ]


top_jungle=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Top-Jungle']))]
jungle_middle=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Jungle-Middle']))]
jungle_support=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Jungle-Support']))]
adc_support=new_df.loc[(new_df['CHAMP_DUOS'].isin(['ADC-Support']))]

top_jungle_relative=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Top-Jungle']))&(df['Total_Played'] >= 10)]
jungle_middle_relative=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Jungle-Middle']))&(df['Total_Played'] >= 10)]
jungle_support_relative=new_df.loc[(new_df['CHAMP_DUOS'].isin(['Jungle-Support']))&(df['Total_Played'] >= 10)]
adc_support_relative=new_df.loc[(new_df['CHAMP_DUOS'].isin(['ADC-Support']))&(df['Total_Played'] >= 10)]


ax1=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=new_df,palette=['b','r'],width=0.3,saturation=1)
ax1.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

ax2=sns.boxplot(x='Team',y='Wins',hue="CHAMP_DUOS",data=new_df,palette=['g','pink','orange','gray'],width=0.3,saturation=1)
ax2.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

ax3=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=top_jungle,palette=['b','r'],width=0.3,saturation=1)
ax3.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

ax4=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=jungle_middle,palette=['b','r'],width=0.3,saturation=1)
ax4.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

ax5=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=jungle_support,palette=['b','r'],width=0.3,saturation=1)
ax5.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

ax6=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=adc_support,palette=['b','r'],width=0.3,saturation=1)
ax6.set_title("Vitórias Absolutas")

plt.legend()
plt.show()

#----------------------------------relative plots---------------

ax1=sns.boxplot(x='CHAMP_DUOS',y='Relative_Wins(%)',hue="Team",data=new_df3,palette=['b','r'],width=0.3,saturation=1)
ax1.set_title("Vitórias relativas")

plt.legend()
plt.show()

ax2=sns.boxplot(x='Team',y='Relative_Wins(%)',hue="CHAMP_DUOS",data=new_df3,palette=['g','pink','orange','gray'],width=0.3,saturation=1)
ax2.set_title("Vitórias relativas")

plt.legend()
plt.show()

ax3=sns.boxplot(x='CHAMP_DUOS',y='Relative_Wins(%)',hue="Team",data=top_jungle_relative,palette=['b','r'],width=0.3,saturation=1)
ax3.set_title("Vitórias relativas")

plt.legend()
plt.show()

ax4=sns.boxplot(x='CHAMP_DUOS',y='Relative_Wins(%)',hue="Team",data=jungle_middle_relative,palette=['b','r'],width=0.3,saturation=1)
ax4.set_title("Vitórias relativas")

plt.legend()
plt.show()

ax5=sns.boxplot(x='CHAMP_DUOS',y='Relative_Wins(%)',hue="Team",data=jungle_support_relative,palette=['b','r'],width=0.3,saturation=1)
ax5.set_title("Vitórias relativas")

plt.legend()
plt.show()

ax6=sns.boxplot(x='CHAMP_DUOS',y='Relative_Wins(%)',hue="Team",data=adc_support_relative,palette=['b','r'],width=0.3,saturation=1)
ax6.set_title("Vitórias relativas")

plt.legend()
plt.show()
