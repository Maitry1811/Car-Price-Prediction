import streamlit as st
import numpy as np
import pickle
from datetime import datetime

# Load model
model = pickle.dump(model,open("car_model.pkl", "wb"))

st.title("Car Price Prediction App")

# Inputs
year = st.number_input("Year of Purchase", 2000, datetime.now().year)
present_price = st.number_input("Present Price (in lakhs)")
kms_driven = st.number_input("Kms Driven")

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", [0,1,2,3])

# Convert categorical
fuel_map = {"Petrol":0, "Diesel":1, "CNG":2}
seller_map = {"Dealer":0, "Individual":1}
trans_map = {"Manual":0, "Automatic":1}

if st.button("Predict Price"):
    input_data = np.array([[
        year,
        present_price,
        kms_driven,
        fuel_map[fuel],
        seller_map[seller],
        trans_map[transmission],
        owner
    ]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {round(prediction[0], 2)} lakhs")
