# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:45:28 2023

@author: karthik
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:53:59 2023

@author: Karthik
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:55:38 2023

@author: Karthik
"""
from pydantic import BaseModel
class Water(BaseModel):
    ph:float
    Hardness:float
    Solids:float
    Chloramines:float
    Sulfate:float
    Conductivity:float
    Organic_carbon:float
    Trihalomethanes:float
    Turbidity:float
import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as Pd
import gunicorn
app=FastAPI()
pickle_in=open('clsfr.pkl','rb')
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return{"message":'Hello,stranger'}
@app.get('/{name')
def get_name(name:str):
    return{'message':f'Hello,{name}'}
@app.post('/predict')
def predict_water(data:Water):
    data=data.dict()
    print(data)
    ph=data['ph']
    Hardness=data['Hardness']
    Solids=data['Solids']
    Chloramines=data['Chloramines']
    Sulfate=data['Sulfate']
    Conductivity=data['Sulfate']
    Organic_carbon=data['Organic_carbon']
    Trihalomethanes=data['Trihalomethanes']
    Turbidity=data['Turbidity']
    #   print(classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]]))
    prediction=classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    if(prediction[0]>0.5):
        prediction="Suitable"
    else:
        prediction="Not suitable"
    return{
        'prediction':prediction
    }
    if _name=='__app_':
        uvicorn.run(app,host='129.0.0.1',port=7000)
#uvicorn app:app --reload

