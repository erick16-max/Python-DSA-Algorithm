import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://www.w3schools.com/python/pandas/dirtydata.csv.txt')
data['Calories'].fillna(data['Calories'].mean(), inplace= True)
data['Date'] = pd.to_datetime(data['Date'])
 
for x in data.index:
    if  data.loc[x, 'Duration'] < 120:
         data.loc[x, 'Duration'] = 120
        
data.drop_duplicates(inplace=True)
data["Duration"].plot(kind = 'hist')
plt.show()
