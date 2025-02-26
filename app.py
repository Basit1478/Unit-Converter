import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100.0,
        "Millimeter": 1000.0,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    return value * (length_units[to_unit] / length_units[from_unit]) if from_unit in length_units and to_unit in length_units else None


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Gram": 1.0,
        "Kilogram": 0.001,
        "Milligram": 1000.0,
        "Pound": 0.00220462,
        "Ounce": 0.035274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit]) if from_unit in weight_units and to_unit in weight_units else None


def temperature_converter(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: None)(value)

st.title("Unit Converter")
option = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot", "Yard", "Mile"],
    "Weight": ["Gram", "Kilogram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

value = st.number_input("Enter value", min_value=0.0, step=0.01)
from_unit = st.selectbox("From unit", units[option])
to_unit = st.selectbox("To unit", units[option])

if st.button("Convert"):
    result = None
    if option == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif option == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif option == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    if result is not None:
        st.success(f"Converted value: {result}")
    else:
        st.error("Invalid unit or conversion")
