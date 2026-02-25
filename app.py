import streamlit as st
import os

st.set_page_config(page_title="My Course Portal")

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Only show login if NOT authenticated
if not st.session_state.authenticated:
    st.title("Course Portal Login")
    password_input = st.text_input("Enter Access Code", type="password")
    login_clicked = st.button("Login")
    
    if login_clicked:
        if password_input == PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Incorrect Access Code")

# Show portal content ONLY if authenticated
if st.session_state.authenticated:
    # HIDE login field completely by using container
    st.empty()  # this removes the login input visually
    st.title("Welcome to My Course Portal")
    st.write("This portal will contain modules, videos, activities and resources.")

    st.header("Announcements")
    st.write("Course will begin next week.")

    st.header("Module Section")
# Path to your PDF files
pdf_files = ["Module1.pdf", "Module2.pdf", "Module3.pdf", "Module4.pdf", "Module5.pdf"]

for pdf in pdf_files:
    if os.path.exists(pdf):
        with open(pdf, "rb") as f:
            st.download_button(
                label=f"Download {pdf}",
                data=f,
                file_name=pdf,
                mime="application/pdf"
            )
    else:
        st.write(f"{pdf} not found.")

    st.header("Video Section")
    st.write("Video links will be added soon.")

    st.header("Activity Section")
    st.write("Activity details will be updated soon.")


