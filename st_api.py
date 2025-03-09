import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/calculator/"

num1 = st.number_input("Enter first number", key="num1")
num2 = st.number_input("Enter second number", key="num2")
operation = st.selectbox("Choose operation", ["addition", "subtraction", "multiplication", "division" , "modulus", "power"])
try : 
    if st.button("Calculate"):
        data = {"num1": num1, 
                "num2": num2, "operation": operation}
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            st.success(f"Result: {response.json()}")
        else:
            st.error(f"API Error: {response.text}")
except Exception as exp:
    print(f"an error occured {exp}")
    




