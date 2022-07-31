import pandas as pd
import pickle
import json
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


df= pd.read_csv('final_raw_data.csv',index_col=0)
df=df.dropna(subset=['Auxiliary Boilers A/B Feed Water Header Pressure 2'])
df=df.dropna(subset=['Pump Radial Bearing Vibration'])
df=df.drop(columns=['Auxiliary Boilers A/B Feed Water Header Pressure 2','Heat Recovery System Header Pressure.1','Lube Oil Cooler Outlet Temperature','Motor Current Phase B','Motor Current Phase C', 'Pump Journal 1 Bearing Temperature','Pump Suction Pressure 2','Pump Thrust Bearing Temperature 2'])
df['Motor Voltage'].fillna(method='bfill', inplace=True)
df=df.fillna(0)

y=df.pop('Pump Radial Bearing Vibration')

X_train,X_test,y_train,y_test= train_test_split(df,y, test_size=0.2, random_state=56)
rfr = RandomForestRegressor(max_depth=25)
rfr.fit(X_train, y_train)
print(rfr.score(X_test,y_test))

with open('model','wb') as file:
    pickle.dump(rfr,file)

