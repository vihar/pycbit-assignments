import pandas as pd
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

pointsOfEmbarkment = ["Cherbourg","Queenstown", "Southampton"]
groups = (df.groupby("Embarked"))
total = (dict(groups["Survived"].agg(np.size)))
#print(d)
the_grid = GridSpec(1, 3)
plt.subplot(the_grid[0, 0], aspect=1)
plt.pie(d.values(), labels = pointsOfEmbarkment, autopct='%1.1f%%')


survivors = df[df["Survived"] == 1].groupby("Embarked")

d1 = (dict(survivors["Name"].agg(np.size)))
#print(d1)
plt.subplot(the_grid[0,2], aspect = 1)
plt.pie(d1.values(), labels = pointsOfEmbarkment, autopct='%1.1f%%')
plt.title("Division of passengers based on the point of embarkment\nTotal and Survivors")
plt.show()
