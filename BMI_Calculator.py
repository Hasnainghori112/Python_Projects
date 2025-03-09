import streamlit as st

st.title("BMI calculator")
st.subheader("This is a simple BMI calculator")
height = st.slider("Enter your height in (cm)" ,70,200)
weight = st.slider("Enter your weight in (kg)",10,100)
bmi = weight/((height/100)**2)
st.write("Your BMI is: ", bmi)
st.subheader("BMI catagory")
st.write("underweight: When BMI is less then 18.5")
st.write("NormalWeight : when BMI between the 18.5 and 24.4")
st.write("obesity : when BMI is 28.4 or greater")