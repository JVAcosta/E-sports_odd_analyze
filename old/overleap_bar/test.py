# t = [1, 2, 3]
# l = [3, 2, 1]

# r = set(t) - set(l)

# print(r)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load the example flights dataset and conver to long-form
flights_long = sns.load_dataset("flights")
print(flights_long.head())
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
obj = sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()
