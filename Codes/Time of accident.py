import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

acci=pd.read_csv('D:\Accidents0514.csv')
cf=pd.read_csv('D:\Casualties0514.csv')
vf=pd.read_csv('D:\Vehicles0514.csv')
first_df=pd.merge(cf,acci,on='Accident_Index')
df=pd.merge(first_df,vf,on='Accident_Index')
df.head()
df.drop('LSOA_of_Accident_Location',axis=1,inplace=True)
df.dropna(subset=['Location_Easting_OSGR','Location_Northing_OSGR', 'Longitude', 'Latitude'],axis=0,inplace=True)
df.dropna(subset=['Time'],axis=0,inplace=True)
q3_df=pd.DataFrame(data=df,columns=['Accident_Severity','Light_Conditions','Weather_Conditions','Hour'])
def time_of_day(n):
    if n in range(4,8):
        return 'Early Morning'
    elif n in range(8,12):
        return 'Morning'
    elif n in range(12,17):
        return 'Afternoon'
    elif n in range(17,20):
        return 'Evening'
    elif n in range(20,25) or n==0:
        return 'Night'
    elif n in range(1,4):
        return 'Late Night'
q3_df['Time_of_Day']=q3_df['Hour'].apply(lambda x: time_of_day(x))
q3_df=q3_df[q3_df.Weather_Conditions!=-1]
sns.heatmap(q3_df.corr())