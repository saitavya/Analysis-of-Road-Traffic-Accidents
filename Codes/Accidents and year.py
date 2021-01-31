import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('D:\Accidents0514.csv',low_memory=False)
cf=pd.read_csv('D:\Casualties0514.csv',low_memory=False)
vf=pd.read_csv('D:\Vehicles0514.csv',low_memory=False)
acci['Year'] = acci['Accident_Index'].map(lambda x: str(x)[:4])
acci['Year'] = acci['Year'].apply(pd.to_numeric, errors='coerce')
year = []
num_of_acci_year = []
for i in range(2005, 2015):
 year.append(i)
 num_of_acci_year.append(len(acci[acci['Year'] == i]))
plt.plot(year, num_of_acci_year)
plt.xlabel('Year')
plt.ylabel('Number of accidents')
plt.title('Correlation between number of accidents and year')
plt.grid(True)
plt.show()