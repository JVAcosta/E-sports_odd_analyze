import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# graficos de caixa para os valores absolutos da vitorias das duplas
# separados por lado vermelho e azul

df = pd.read_csv("selected_duos_teste.csv")


new_df=df
new_df.insert(1, 'CHAMP_DUOS', df.iloc[1:-1,6]+'-'+df.iloc[1:-1,7])

sns.set(style="ticks", palette="pastel")



ax=sns.boxplot(x='CHAMP_DUOS',y='Wins',hue="Team",data=new_df,palette=['b','r'],width=0.3,saturation=1)

plt.legend()
plt.show(ax)

