# library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns

# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
data = pd.read_csv(url)

# Transform it to a long format
df = data.unstack().reset_index()
print(df.head())
df.columns = ["X", "Y", "Z"]
print(df.head())
# And transform the old column name in something numeric
df['X'] = pd.Categorical(df['X'])
print(df.head())
df['X'] = df['X'].cat.codes
print(df['X'])
print(df['Y'])
print(df['Z'])
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
ax.set_xlabel('time (s)')
ax.set_ylabel('time (y)')
ax.set_zlabel('time (z)')
ax.set_title('title')
# plt.show()

# to Add a color bar which maps values to colors.
surf = ax.plot_trisurf(df['Y'], df['X'], df['Z'],
                       cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# Rotate it
ax.view_init(30, 45)
plt.show()

# Other palette
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.jet, linewidth=0.01)
# plt.show()
