import seaborn as sns
import numpy as np
from math import pi
import pandas as pd
import matplotlib.pyplot as plt


def f2(seq):
    # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked


def champToChamp():
    df = pd.read_csv('../Results/TAGS.csv')

    df['CHAMP_DUOS_BLUE']=df.iloc[0:-1,1]+'-'+df.iloc[0:-1,2]
    df['CHAMP_DUOS_RED']=df.iloc[0:-1,3]+'-'+df.iloc[0:-1,4]
    del df['TAG_Champ_1_Blue']
    del df['TAG_Champ_2_blue']
    del df['TAG_Champ_1_Red']
    del df['TAG_Champ_2_red']
    df=pd.pivot_table(df,index='CHAMP_DUOS_BLUE',columns='CHAMP_DUOS_RED')
    print(df.keys())
    df.to_csv('teste_felipe.csv', encoding='utf-8')
    
    

    
champToChamp()
'''
    df['CHAMP_DUOS']=df.iloc[1:-1,0]+'-'+df.iloc[1:-1,1]
    
    print(df)
    # number of variable
    categories = []
    for i, v in df.iterrows():
        categories.append(v.TAG_Champ_1_Red+"/" + v.TAG_Champ_2_red)
    # categories = np.array(categories)
    print(categories)
    N = len(categories)

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    # close the plot
    angles = np.concatenate((angles, [angles[0]]))

    values = []
    categories = f2(categories)
    print(categories)
    new_df = df
    new_df.insert(
        1, 'Tags_red', (new_df.iloc[1:-1, 3]+'/'+new_df.iloc[1:-1, 4]))
    for x in categories:
        dfloc = new_df.loc[(new_df['Tags_red'] == x)]
        values.append(dfloc.values)
    print(values)
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, categories)
    ax.grid(True)
    fig.show()


champToChamp()
'''
