import streamlit as st

st.set_page_config(page_title="My Course Portal")

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"  # change as you like

# Initialize session variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# LOGIN PAGE
if st.session_state.page == "login":
    st.title("Course Portal Login")
    password = st.text_input("Enter Access Code", type="password")
    if st.button("Login"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.session_state.page = "portal"  # go to portal page
        else:
            st.error("Incorrect Access Code")

# PORTAL PAGE
if st.session_state.page == "portal" and st.session_state.authenticated:
    st.title("Welcome to My Course Portal")
    st.write("This portal will contain modules, videos, activities and resources.")

    st.header("Announcements")
    st.write("Course will begin next week.")

    st.header("Module Section")
    st.write("Module materials will be uploaded soon.")

    st.header("Video Section")
    st.write("Video links will be added soon.")

    st.header("Activity Section")
    st.write("Activity details will be updated soon.")