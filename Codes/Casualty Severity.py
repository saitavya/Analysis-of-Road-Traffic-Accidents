import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
Severity1 =len(cf[cf['Casualty_Severity']==1])
Severity2 =len(cf[cf['Casualty_Severity']==2])
Severity3 =len(cf[cf['Casualty_Severity']==3])
tot=Severity1+Severity2+Severity3;
s1=(Severity1/tot)*100;
s2=(Severity2/tot)*100;
s3=(Severity3/tot)*100;
print("Percentage of Deaths is {0:.0f}%".format(s1))
print("Percentage of Major Injuries is {0:.0f}%".format(s2))
print("Percentage of Minor Injuires is {0:.0f}%".format(s3))
labels = 'Deaths','MajorInjuries','Minor Injuries'
sizes = [s1, s2, s3]
colors = ['lightskyblue', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
shadow=True, startangle=140)
plt.axis('equal')
plt.show()