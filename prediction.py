import pandas as pd 
import pickle
import json

def predict (data, model_path='model'): 
    '''
    data: data to get prediction on (JSON) 
    model_path: path to the model (string) 
    ''' 
    columns=['Auxiliary Boilers Feed Water Header Pressure',
       'Heat Recovery System Header Mass Flow',
       'Heat Recovery System Header Mass Flow.1',
       'Heat Recovery System Header Pressure', 'Lube Oil Tank Temperature',
       'Motor Current Phase A', 'Motor Input Power', 'Motor Power Factor',
       'Motor Voltage', 'Pump Discharge Pressure',
       'Pump Discharge Volumetric Flow', 'Pump Journal 2 Bearing Temperature',
       'Pump Shaft Speed', 'Pump Suction Pressure 1',
       'Pump Suction Strainer Differential Pressure',
       'Pump Suction Temperature', 'Pump Thrust Bearing Temperature 1']


    
    
    data = pd.read_json(data) 
    
    test=pd.DataFrame()
    for column in columns:
        test[column]=data[column]
    test=test.fillna(0)

    with open(model_path,'rb') as file:
        model=pickle.load(file)

    

    prediction = model.predict(test)  
    return prediction
