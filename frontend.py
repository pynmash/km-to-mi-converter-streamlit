import streamlit as st
import backend

st.title("Kilometers                                        Miles Converter")

conversion = st.radio("Choose the conversion direction",
                      ["Kilometers to miles", "Miles to kilometers"],
                      index=None, key="convert_choice")

distance = float(st.number_input("Enter the distance"))

if st.button(":rainbow[Convert]"):
    if conversion == "Kilometers to miles":
        converted = backend.km_to_miles(distance)
    else:
        converted = backend.miles_to_km(distance)
    st.subheader(f"{distance} {conversion} = {converted}")
