import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv')
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv')
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv')
urban_acci =len(acci[acci['Urban_or_Rural_Area']==1])
rural_acci =len(acci[acci['Urban_or_Rural_Area']==2])
na_acci =len(acci[acci['Urban_or_Rural_Area']==3])
total_acci = urban_acci + rural_acci + na_acci
urban_pct = urban_acci / total_acci * 100
rural_pct = rural_acci / total_acci *100
na_pct = na_acci / total_acci * 100
print("Percentage of accidents occur in urban areas is {0:.0f}%".format(urban_pct))
print("Percentage of accidents occur in rural areas is {0:.0f}%".format(rural_pct))
print("Percentage of accidents occur in other areas is {0:.0f}%".format(na_pct))
x = ['Urban', 'Rural', 'Other']
y = [urban_pct, rural_pct,na_pct]
x_pos =list(range(len(x)))
plt.bar(x_pos, y)
plt.ylabel('Percentage ofaccidents')
plt.xticks(x_pos,x)
plt.title("Percentage of accidents occuredby area")
plt.show()
