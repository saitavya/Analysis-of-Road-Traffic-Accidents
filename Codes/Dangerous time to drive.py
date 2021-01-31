import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv')
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv')
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv')
acci['Hour'] = acci['Time'].map(lambda x: str(x).split(':')[0])
# print(acci['Hour'].describe())

acci['Hour'] = acci['Hour'].apply(pd.to_numeric, errors='coerce')
hour = []
num_of_fatal_acci = []
num_of_acci = []
for i in range(24):
    hour.append(i)
    num_of_fatal_acci_hour = len(acci[(acci['Accident_Severity'] == 1) & (acci['Hour'] == i)])
    num_of_acci_hour = len(acci[acci['Hour'] == i])
    num_of_fatal_acci.append(num_of_fatal_acci_hour)
    num_of_acci.append(num_of_acci_hour)
print(hour)
print(num_of_fatal_acci)
print(num_of_acci)

normalized_num_of_fatal_acci = list(np.array(num_of_fatal_acci) / np.array(num_of_acci) * 100)
# print(max(normalized_num_of_fatal_acci))

fig = plt.figure(figsize=(14,8))

ax1 = fig.add_subplot(221)
ax1.plot(hour, num_of_fatal_acci)
ax1.set_ylabel('Number of fatal accidents')
ax1.set_xlabel('Hour')
ax1.grid(True)

ax2 = fig.add_subplot(222)
ax2.plot(hour, num_of_acci)
ax2.set_ylabel('Number of all accidents')
ax2.set_xlabel('Hour')
ax2.grid(True)

ax3 = fig.add_subplot(223)
ax3.plot(hour, normalized_num_of_fatal_acci)
ax3.set_ylabel('Percentage of fatal accidents in all accidents')
ax3.set_xlabel('Hour')
ax3.grid(True)

plt.show()

print("The most dangerous hour to drive, when most fatal accidents happend in all accidents, is {} PM".format(normalized_num_of_fatal_acci.index(max(normalized_num_of_fatal_acci))))