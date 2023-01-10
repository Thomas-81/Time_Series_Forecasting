import streamlit as st
import pandas as pd 
import numpy as np 
from prophet import Prophet
from prophet import Prophet
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
from prophet.plot import port_cross_validation_metric
import base64

st.title('Automated Time Series Forecasting')

"""This data app uses Facebook's open-source Prophet library to automatic you'll"""
df=st.file_uploader('Import the time series Csv file here. Columns')

if df is not None:
    data=pd.read_csv(df)
    data['ds']=pd.to_datetime(data['ds'],errors='coerce')

    st.write(data)

    max_data=data['ds'].max()



periods_input =st.number_input('How many periods would you like to do'
min_value=1, max_value=365)

if df is not None:
    m=Prophet()
    m.fit(data)
    