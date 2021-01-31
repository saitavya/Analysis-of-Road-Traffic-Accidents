import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
accidents=acci['Accident_Index'][1:25]
LightConditions=acci['Light_Conditions'][1:25]

fig = plt.figure(figsize=(10,8))
plt.plot(LightConditions,accidents)
plt.xlabel('Light_Conditions')
plt.ylabel('Accidents')
plt.title('no of accidents occurred as per light conditions')
plt.grid(True)
plt.show()