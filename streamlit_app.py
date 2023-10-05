import streamlit as st
import utils  # Import your utility functions here

st.title("Prediction using Streamlit")

# Create input elements for user input
open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
volume = st.number_input("Volume")

if st.button("Predict"):
    prediction = utils.preprocess(open_price, high_price, low_price, volume)
    st.write(f"Predicted Result: {prediction}")
