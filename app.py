import streamlit as st

# ---- PASSWORD PROTECTION ----
PASSWORD = "MBA2026"  # You can change this to any code you want

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Course Portal Access")
    password = st.text_input("Enter Access Code", type="password")
    
    if st.button("Login"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.success("Access Granted")
        else:
            st.error("Incorrect Access Code")
    st.stop()
# ---- END PASSWORD PROTECTION ----
