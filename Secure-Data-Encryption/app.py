import streamlit as st
from pages import home_page, store_data_page, retrieve_data_page, login_page
from utils import initialize_session

# Set up Streamlit page
st.set_page_config(page_title="🔐 Secure Data Vault", page_icon="🛡️")
st.title("🛡️ Secure Data Encryption System")

# Initialize session state
initialize_session()

# Navigation
menu_options = ["Home", "Store Data", "Retrieve Data", "Login"]
current_page = st.sidebar.selectbox("Navigate", menu_options)

# Render selected page
if current_page == "Home":
    home_page()
elif current_page == "Store Data":
    store_data_page()
elif current_page == "Retrieve Data":
    retrieve_data_page()
elif current_page == "Login":
    login_page()
