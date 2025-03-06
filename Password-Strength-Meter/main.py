import streamlit as st
from manual_analyzer import check_password_strength
from ai_analyzer import AIPasswordAdvisor
from password_generator import generate_strong_password

# Set up the Streamlit app title and description
st.title("🔐 Password Strength Meter 🔐")
st.write("This app evaluates the strength of your password and provides feedback. You can also generate a strong password!")

# Sidebar for mode selection
st.sidebar.title("Options")
mode = st.sidebar.radio("Choose Analysis Mode:", ("Manual Analysis", "AI-Powered Analysis"))

# Input field for the user's password
password = st.text_input("Enter your password:", type="password")

# Analyze password strength
if st.button("Check Password Strength"):
    if password:
        if mode == "Manual Analysis":
            st.write("### Manual Analysis Results:")
            strength_score, feedback = check_password_strength(password)
            for message in feedback:
                st.write(message)
        else:
            st.write("### AI-Powered Analysis Results:")
            strength_score, _ = check_password_strength(password)
            ai_advisor = AIPasswordAdvisor()
            ai_feedback = ai_advisor.get_feedback(password, strength_score)
            st.write(ai_feedback)
    else:
        st.error("Please enter a password to analyze.")

# Generate a strong password
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.write("### Generated Strong Password:")
    st.code(strong_password)