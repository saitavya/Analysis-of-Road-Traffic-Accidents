import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

acci=pd.read_csv('D:\Accidents0514.csv')
cf=pd.read_csv('D:\Casualties0514.csv')
vf=pd.read_csv('D:\Vehicles0514.csv')
first_df=pd.merge(cf,acci,on='Accident_Index')
df=pd.merge(first_df,vf,on='Accident_Index')
df.drop('LSOA_of_Accident_Location',axis=1,inplace=True)
df.dropna(subset=['Location_Easting_OSGR','Location_Northing_OSGR', 'Longitude', 'Latitude'],axis=0,inplace=True)
df.dropna(subset=['Time'],axis=0,inplace=True)
def month(string):
    return int(string[3:5])
df['Month']=df['Date'].apply(lambda x: month(x))
def hour(string):
    s=string[0:2]
    return int(s)
df['Hour']=df['Time'].apply(lambda x: hour(x))
q1_df=pd.DataFrame(data=df,columns=['Hour','Day_of_Week','Month','Accident_Severity'])
sns.heatmap(q1_df.corr())