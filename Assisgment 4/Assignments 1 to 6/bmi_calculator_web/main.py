import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)")
height = st.number_input("Enter your height (m)")

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 30:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")