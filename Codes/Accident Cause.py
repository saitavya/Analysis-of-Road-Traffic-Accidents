import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
sko =len(vf['Skidding_and_Overturning'])
hoic =len(vf['Hit_Object_in_Carriageway'])
vlc =len(vf['Vehicle_Leaving_Carriageway'])
hooc=len(vf['Hit_Object_off_Carriageway'])
total = sko + hoic + vlc + hooc
sko_pct = sko / total * 100
hoic_pct = hoic / total *100
vlc_pct = vlc / total * 100
hooc_pct=hooc/total *100
print("Percentage of accidents occur in urban areas is {0:.0f}%".format(sko_pct))
print("Percentage of accidents occur in rural areas is {0:.0f}%".format(hoic_pct))
print("Percentage of accidents occur in other areas is {0:.0f}%".format(vlc_pct))
print("Percentage of accidents occur in other areas is {0:.0f}%".format(hooc_pct))
x = ['Skidding', 'Collision', 'Leaving carriageway', 'Overturning']
y = [sko_pct, hoic_pct,vlc_pct,hooc_pct]
x_pos =list(range(len(x)))
plt.bar(x_pos, y)
plt.ylabel('Percentage ofaccidents') 
plt.xticks(x_pos,x)
plt.title("Percentage of accidents occuredby area")
plt.show()