import streamlit as st
import pandas as pd
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

pickup_datetime = st.text_input('Insert taxi pickup date and time', '2014-07-06 19:18:00')
if pickup_datetime != "":
    st.write("The pickup date is", pickup_datetime)
    #pickup_datetime = pd.Timestamp(pickup_datetime, tz='US/Eastern')

pickup_long = st.text_input('Insert taxi pickup longitude', '-73.950655')
if pickup_long != "":
    st.write("The pickup longitude is", pickup_long)
    pickup_long = float(pickup_long)

pickup_lat = st.text_input('Insert taxi pickup latitude', '40.783282')
if pickup_lat != "":
    st.write("The pickup latitude is", pickup_lat)
    pickup_lat = float(pickup_lat)

dropoff_long = st.text_input('Insert taxi dropoff longitude', '-73.984365')
if dropoff_long != "":
    st.write("The dropoff longitude is", dropoff_long)
    dropoff_long = float(dropoff_long)

dropoff_lat = st.text_input('Insert taxi dropoff latitude', '40.769802')
if dropoff_lat != "":
    st.write("The dropoff latitude is", dropoff_lat)
    dropoff_lat = float(dropoff_lat)

passenger_count = st.text_input('Insert the number of passenger', '2')
if passenger_count != "":
    st.write("The number of passenger is", passenger_count)
    passenger_count = int(passenger_count)

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
'''
## User prediction
'''

params = {'pickup_datetime':pickup_datetime,
          'pickup_longitude':pickup_long,
          'pickup_latitude':pickup_lat,
          'dropoff_longitude':dropoff_long,
          'dropoff_latitude':dropoff_lat,
          'passenger_count':passenger_count
}

if st.button("Predict", type="primary"):
    response = requests.get(url, params=params)
    st.write('**Prediction result:**', response.json()['fare'])
