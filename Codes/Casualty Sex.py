import pandas as pd
import matplotlib.pyplot as plt
acci=pd.read_csv('E:/dftRoadSafetyData_Accidents_2018.csv',low_memory=False)
cf=pd.read_csv('E:/dftRoadSafetyData_Casualties_2018.csv',low_memory=False)
vf=pd.read_csv('E:/dftRoadSafetyData_Vehicles_2018.csv',low_memory=False)
men =len(cf[cf['Sex_of_Casualty']==1])
women =len(cf[cf['Sex_of_Casualty']==2])
x = ['Men', 'Women']
y = [men,women]
x_pos =list(range(len(x)))
plt.bar(x_pos, y,color ='maroon')
plt.ylabel('Casulaities')
plt.xticks(x_pos,x)
plt.title("Casualitiesoccured by gender")
plt.show()