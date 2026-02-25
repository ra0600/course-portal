import streamlit as st

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"  # Change as you like

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Input password
if not st.session_state.authenticated:
    password = st.text_input("Enter Access Code", type="password")
    login = st.button("Login")
    
    if login:
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.success("Access Granted ✅")
        else:
            st.error("Incorrect Access Code")

# Only show portal content if authenticated
if st.session_state.authenticated:
    # ----- BEGIN YOUR PORTAL CONTENT -----
    st.set_page_config(page_title="My Course Portal")

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
    # ----- END YOUR PORTAL CONTENT -----

