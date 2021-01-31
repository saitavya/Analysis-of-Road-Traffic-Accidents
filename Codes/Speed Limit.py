import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
speed_limit = []
num_casualty = []
num_acci = []
ratio = []

for i in sorted(list(set(acci['Speed_limit']))):
    speed_limit.append(i)
    casualty = acci.loc[acci['Speed_limit'] == i, 'Number_of_Casualties'].sum()
    num_casualty.append(casualty)
    accident = len(acci[(acci['Speed_limit'] == i)])
    num_acci.append(accident)
    r = casualty / accident
    ratio.append(r)

plt.plot(speed_limit, ratio)
plt.xlabel('Speed limit')
plt.ylabel('Casualty per accident, average')
plt.title('Correlation between casualty per accident and speed limit')
plt.grid(True)
plt.show()