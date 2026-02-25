import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Investment Banking Course Portal",
    page_icon="📘",
    layout="wide"
)

# ---- BACKGROUND IMAGE (light finance/stock theme) ----
background_url = "https://images.pexels.com/photos/590020/pexels-photo-590020.jpeg"
st.markdown(
    f"""
    <style>
    /* Background image and overlay */
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: relative;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255,255,255,0.4);  /* semi-transparent overlay */
        z-index: 0;
    }}
    /* Buttons styling */
    .stButton>button {{
        color: white;
        background-color: #003366;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("IBFS Course Portal Login")
    password_input = st.text_input("Enter Access Code", type="password")
    if st.button("Login"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Incorrect Access Code")

# ---- PORTAL CONTENT ----
if st.session_state.authenticated:
    # Header
    st.title("Semester-IV IBFS Course Portal")
    
    # Announcement Panel
    st.subheader("📢 Announcements")
    st.info("""
    - Course will begin next week.  
    - Modules and resources will be updated regularly.  
    - Check back here for latest news and updates.  
    """)

    # Tabs for 4 courses
    tab1, tab2, tab3, tab4 = st.tabs([
        "Investment Banking",
        "Financial Services",
        "Business Ethics",
        "Business Strategy"
    ])

    # ---- Investment Banking ----
    with tab1:
        st.header("Investment Banking Modules")
        ib_pdfs = ["Module1.pdf", "Module2.pdf", "Module3.pdf", "Module4.pdf", "Module5.pdf"]
        for pdf in ib_pdfs:
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
        st.header("Videos")
        st.write("Video links for Investment Banking will be added here.")
        st.header("Activities")
        st.write("Activities for Investment Banking will be added here.")

    # ---- Financial Services ----
    with tab2:
        st.header("Financial Services Modules")
        st.write("Modules and resources will be added soon.")

    # ---- Business Ethics ----
    with tab3:
        st.header("Business Ethics Modules")
        st.write("Modules and resources will be added soon.")

    # ---- Business Strategy ----
    with tab4:
        st.header("Business Strategy Modules")
        st.write("Modules and resources will be added soon.")
