import seaborn as sns
import numpy as np
from math import pi
import pandas as pd
import matplotlib.pyplot as plt
import math


def f2(seq):
    # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked


def champToChamp():
    df = pd.read_csv('../Results/TAGS.csv')

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
    categories = list(df)[1:]
    N = len(categories)
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    # close the plot
    angles = np.concatenate((angles, [angles[0]]))
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)
    plt.yticks([30, 50, 70], ["30", "50", "70"], color="grey", size=7)
    plt.ylim(0, 100)
    values = df.iloc[0].values.tolist()
    values = [0 if math.isnan(x) else x for x in values]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
    ax.fill(angles, values, 'b', alpha=0.1)
    values = df.iloc[3].values.tolist()
    values = [0 if math.isnan(x) else x for x in values]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
    ax.fill(angles, values, 'r', alpha=0.1)
    values = df.iloc[5].values.tolist()
    values = [0 if math.isnan(x) else x for x in values]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="group C")
    ax.fill(angles, values, 'g', alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()


champToChamp()
