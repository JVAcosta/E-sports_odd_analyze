import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np


def champToChamp():
    df = pd.read_csv('../Results/TagsHugo.csv')
    # number of variable
    print(df)
    df["categorie"] = df["CHAMP1_y"].map(str) + df["CHAMP2_y"]
    df = df.loc[(df['CHAMP1_x'] == 'Lucian') &
                (df['CHAMP2_x'] == 'Braum')]
    categories = np.array(list(df.categorie))
    N = len(categories)
    print(N)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    angles = np.array(angles)

    values = []
    for x in categories:
        values.append(df.loc[df['categorie'] == x].bResult /
                      df.loc[df['categorie'] == x].Partidas_x)
    values = np.array(values)
    print(len(values))
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    ax.plot(angles[:-1], values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    ax.show()


champToChamp()
