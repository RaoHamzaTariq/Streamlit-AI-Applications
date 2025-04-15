import hashlib
from cryptography.fernet import Fernet
import streamlit as st

def initialize_session():
    if 'encryption_key' not in st.session_state:
        st.session_state.encryption_key = Fernet.generate_key()
        st.session_state.cipher = Fernet(st.session_state.encryption_key)
    if "encrypted_records" not in st.session_state:
        st.session_state.encrypted_records = {}
    if "login_attempts" not in st.session_state:
        st.session_state.login_attempts = 0
    if "locked_out" not in st.session_state:
        st.session_state.locked_out = False

def get_hashed_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_message(message: str) -> str:
    return st.session_state.cipher.encrypt(message.encode()).decode()

def try_decrypt(encrypted_text: str, passkey: str) -> str | None:
    if st.session_state.locked_out:
        return None

    hashed_key = get_hashed_passkey(passkey)
    saved_data = st.session_state.encrypted_records

    if encrypted_text in saved_data and saved_data[encrypted_text]["passkey"] == hashed_key:
        st.session_state.login_attempts = 0
        try:
            return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()
        except:
            return None

    st.session_state.login_attempts += 1
    if st.session_state.login_attempts >= 3:
        st.session_state.locked_out = True
    return None

def reset_login():
    st.session_state.login_attempts = 0
    st.session_state.locked_out = False
