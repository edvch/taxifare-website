import streamlit as st
import pandas as pd
import requests
import datetime

'''
# NYC taxi fare
'''

d = st.date_input("Insert taxi pickup date and time", datetime.date(2014, 7, 6))
if d != "":
    st.write("The pickup date is", d)

t = st.time_input("Set an alarm for", value='19:00')
if t != "":
    st.write("The pickup time is", t)

passenger_count = st.slider("How many passenger?", 1, 8, 1)
if passenger_count != "":
    st.write("The number of passenger is", passenger_count)
    passenger_count = int(passenger_count)

col1, col2 = st.columns(2)

pickup_long = col1.number_input('Insert taxi pickup longitude', -73.950655, key='plong')
if pickup_long != "":
    pickup_long = float(pickup_long)

pickup_lat = col2.number_input('Insert taxi pickup latitude', 40.783282, key='plat')
if pickup_lat != "":
    pickup_lat = float(pickup_lat)

col3, col4 = st.columns(2)
dropoff_long = col3.number_input('Insert taxi dropoff longitude', -73.984365, key='dlong')
if dropoff_long != "":
    dropoff_long = float(dropoff_long)

dropoff_lat = col4.number_input('Insert taxi dropoff latitude', 40.769802, key='dlat')
if dropoff_lat != "":
    dropoff_lat = float(dropoff_lat)

map = pd.DataFrame([[pickup_lat, pickup_long], [dropoff_lat, dropoff_long]], columns=['lat', 'lon'])
st.map(map, zoom=12)

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
'''
## Ride price
'''

pickup_datetime = str(d) + ' ' + str(t)

params = {'pickup_datetime':pickup_datetime,
          'pickup_longitude':pickup_long,
          'pickup_latitude':pickup_lat,
          'dropoff_longitude':dropoff_long,
          'dropoff_latitude':dropoff_lat,
          'passenger_count':passenger_count
}

if st.button("How much it will cost?"):
    response = requests.get(url, params=params)
    predicted_price = round(float(response.json()['fare']), 2)
    st.badge(f'{predicted_price} $', color="green")
    st.markdown("[![Click me](./app/static/terry_crews_taxi.gif)](https://streamlit.io)")
    st.audio("Tokyo_Drift.mp3", format="audio/mpeg", loop=True, autoplay=True)
