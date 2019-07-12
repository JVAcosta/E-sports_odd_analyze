import seaborn as sns
import numpy as np
from math import pi
import pandas as pd
import matplotlib.pyplot as plt
import math


def champToChamp():
    df = pd.read_csv('../Results/TAGS.csv')
    df = df.loc[(df['TAG_Champ_1_Blue'] +
                 df['TAG_Champ_2_blue'] == 'MarksmanSupport, Tank') | (df['TAG_Champ_1_Blue'] +
                                                                       df['TAG_Champ_2_blue'] == 'MarksmanSupport, Mage')]
    df['CHAMP_DUOS_BLUE'] = df.iloc[0:-1, 1]+'-'+df.iloc[0:-1, 2]
    df['CHAMP_DUOS_RED'] = df.iloc[0:-1, 3]+'-'+df.iloc[0:-1, 4]
    df['RESULT(%)'] = df.iloc[0:-1, 5]/df.iloc[0:-1, 7]*100
    del df['TAG_Champ_1_Blue']
    del df['TAG_Champ_2_blue']
    del df['TAG_Champ_1_Red']
    del df['TAG_Champ_2_red']
    del df['bResult']
    del df['rResult']
    del df['Partidas_x']
    df = pd.pivot_table(df, index='CHAMP_DUOS_BLUE',
                        columns='CHAMP_DUOS_RED', values='RESULT(%)')

    df.to_csv('teste_felipe.csv', encoding='utf-8')

    # number of variable
    print(df)
    categories = range(1, len(df.columns))
    print(categories)
    N = len(categories)
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    # close the plot
    angles = np.concatenate((angles, [angles[0]]))
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ["10", "20", "30", "40", "50", '60',
                                                           "70", "80", "90", '100'], color="grey", size=7)
    plt.ylim(0, 100)
    values = df.loc["Marksman-Support, Tank", :].values.tolist()
    values = [0 if math.isnan(x) else x for x in values]
    ax.plot(angles, values, linewidth=1,
            linestyle='solid', label="group A")
    ax.fill(angles, values, 'b', alpha=0.1)

    values = df.loc["Marksman-Support, Mage", :].values.tolist()
    values = [0 if math.isnan(x) else x for x in values]
    ax.plot(angles, values, linewidth=1,
            linestyle='solid', label="group b")
    ax.fill(angles, values, 'r', alpha=0.1)

    ax.legend((1, 2, 3), ('a', 'b', 'c'))
    plt.show()


champToChamp()
