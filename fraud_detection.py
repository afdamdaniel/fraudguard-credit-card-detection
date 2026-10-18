# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:57:13 2026

@author: afdamdaniel
"""
import pickle
from pathlib import Path
import streamlit as st

MODEL_PATH = Path(__file__).parent / "fraud_detection_model.sav"

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

fraud_detection_model = load_model()

#
st.title('Credit Card Fraud Detection Using Machine Learning')

# fraud - Is the transaction fraudulent

distance_from_home = st.number_input(
    "Distance from home", min_value=0.0
)

distance_from_last_transaction = st.number_input(
    "Distance from last transaction", min_value=0.0
)

ratio_to_median_purchase_price = st.number_input(
    "Ratio to median purchase price", min_value=0.0
)

repeat_retailer = st.selectbox(
    "Repeat retailer?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

used_chip = st.selectbox(
    "Used chip?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

used_pin_number = st.selectbox(
    "Used PIN?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

online_order = st.selectbox(
    "Online order?",
    [1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

#prediction
fraud_detec = '' #empty string

#Button

if st.button('Result'):
    fraud_detect = fraud_detection_model.predict([[
        distance_from_home,
        distance_from_last_transaction,
        ratio_to_median_purchase_price,
        repeat_retailer,
        used_chip,
        used_pin_number,
        online_order
    ]])

    if fraud_detect[0] == 1:
        fraud_detec = 'The card transaction is fraudulent'
        st.error(fraud_detec)
    else:
        fraud_detec = 'The card transaction is normal'
        st.success(fraud_detec)
