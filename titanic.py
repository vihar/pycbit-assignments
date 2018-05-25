#importing modules

import pandas as pd
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt

#read .csv file into a dataframe
data=pd.read_csv('titanic.csv')

#description of dataframe
data.info()

#first 5 rows display
display(data.head())

#count number of survivers in a specified age range
survivers_count=[0,0,0,0,0,0,0,0]
for i in range(0,8):
	survivers_count[i] = int((data[data.Age>=((i+1)*10)][data.Age<(i+2)*10][data.Survived==1].PassengerId.count()/data[data.Age>=((i+1)*10)][data.Age<((i+2)*10)].PassengerId.count())*100)

#craete a dictionary so that it can be converted to dataframe
dict1={'AgeRange':[1,2,3,4,5,6,7,8],'PercentageofSurvival': survivers_count}
data_res=pd.DataFrame(data=dict1)
print("\n\n\n")

#display sample rows of new dataframe
display(data_res.head())

#scatter plot created
data_res.plot(kind='scatter', x='AgeRange', y='PercentageofSurvival',alpha = 0.5,color = 'red')
plt.xlabel('AgeRange(scale= 1:10-20)')  
plt.ylabel('Survivers_Percentage')
plt.title('Age Survival Scatter Plot')
plt.show()

plt.bar(dict1['AgeRange'],dict1['PercentageofSurvival'])
plt.show()