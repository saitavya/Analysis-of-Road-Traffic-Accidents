import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
age_acci = vf[['Accident_Index', 'Age_of_Driver', 'Vehicle_Type']]
# print(age_acci.head())
# print(max(age_acci['Age_of_Driver']))
age = []
num_of_acci = []
for i in range(17, max(age_acci['Age_of_Driver'])+1):
    age.append(i)
    num_of_acci.append(len(age_acci[(age_acci['Age_of_Driver'] == i) & (age_acci['Vehicle_Type'] == 9)]))
# print(age)
# print(num_of_acci)

plt.plot(age, num_of_acci, label = 'Data', marker = 'o')
plt.xlabel('Age')
plt.ylabel('Number of car accidents')
plt.title('Correlation between driver age and number of car accidents')
plt.grid(True)
plt.show()