import streamlit as st
from utils import encrypt_message, get_hashed_passkey, try_decrypt, reset_login

def home_page():
    st.subheader("Welcome to Your Private Vault")
    st.write("""
        This simple app lets you **encrypt and store sensitive information**, then retrieve it securely later using a passkey.
        
        - Uses Fernet encryption for security
        - Passkeys are hashed and never stored in plain form
        - 3 failed attempts will lock access until re-logged in
    """)
    
    if st.session_state.encrypted_records:
        st.info(f"You have {len(st.session_state.encrypted_records)} encrypted records stored.")
    else:
        st.info("No data stored yet. Use the 'Store Data' page to add your first encrypted message.")

def store_data_page():
    st.subheader("Encrypt & Store Your Secret")
    
    secret_data = st.text_area("Enter your confidential message:", height=150)
    passkey = st.text_input("Set a unique passkey to unlock this message later:", type="password")
    confirm_passkey = st.text_input("Confirm your passkey:", type="password")

    if st.button("Encrypt & Save"):
        if not secret_data:
            st.error("Please enter a message to encrypt.")
        elif not passkey:
            st.error("Please set a passkey.")
        elif passkey != confirm_passkey:
            st.error("Passkeys do not match!")
        else:
            encrypted_token = encrypt_message(secret_data)
            st.session_state.encrypted_records[encrypted_token] = {
                "passkey": get_hashed_passkey(passkey),
                "message": secret_data
            }
            st.success("Your data has been encrypted and saved!")
            st.markdown("**Here is your encrypted token. Copy and keep it safe:**")
            st.code(encrypted_token, language="text")

            st.warning("""
            **Important Notes:**
            1. This token is required to retrieve your message later
            2. The app doesn't store this token for you - save it somewhere secure
            3. If you lose this token or your passkey, your message cannot be recovered
            """)

def retrieve_data_page():
    st.subheader("Decrypt Stored Data")

    if st.session_state.locked_out:
        st.error("Account locked due to too many failed attempts. Please log in to continue.")
        st.stop()

    encrypted_input = st.text_area("Paste the encrypted token here:", height=100)
    passkey_input = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if not encrypted_input:
            st.error("Please enter an encrypted token.")
        elif not passkey_input:
            st.error("Please enter your passkey.")
        else:
            result = try_decrypt(encrypted_input, passkey_input)
            if result:
                st.success("Success! Here's your decrypted message:")
                st.text_area("Decrypted Message", value=result, height=150, key="decrypted_output")
            else:
                remaining = max(0, 3 - st.session_state.login_attempts)
                if remaining > 0:
                    st.error(f"Incorrect passkey. Attempts left: {remaining}")
                else:
                    st.session_state.locked_out = True
                    st.error("Too many failed attempts. Account locked.")
                    st.rerun()

def login_page():
    st.subheader("Re-Login to Unlock the App")

    if not st.session_state.locked_out and st.session_state.login_attempts < 3:
        st.info("ℹ You're not currently locked out. You can proceed to other pages.")

    entered_password = st.text_input("Enter Master Password:", type="password", key="master_pass_input")

    if st.button("Login"):
        if entered_password == "9211":  
            reset_login()
            st.success("Access restored. Redirecting to home page...")
            st.rerun()
        else:
            st.error("Incorrect master password.")
