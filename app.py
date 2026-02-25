import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Investment Banking Course Portal",
    page_icon="📘",
    layout="wide"
)

# ---- DARK FINANCE-THEMED BACKGROUND ----
background_url = "https://www.dreamstime.com/chic-dual-color-background-seamless-blend-dark-navy-rich-royal-blue-perfect-sophisticated-elegant-aesthetic-image327881619"
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.8);  /* darker overlay */
        z-index: -1;
    }}
    .stButton>button {{
        color: white;
        background-color: #0ea5e9;
        font-weight: bold;
        border-radius: 30px;
        padding: 12px 25px;
        transition: transform 0.3s, box-shadow 0.3s;
    }}
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(14,165,233,0.4);
    }}
    .stText, .stMarkdown {{
        color: #fff;
    }}
    .module-card {{
        background-color: rgba(20,30,50,0.7);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("IBFS Course Portal Login")
    password_input = st.text_input("Enter Access Code", type="password")
    if st.button("Enter Portal"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
        else:
            st.error("Incorrect Access Code")

# ---- PORTAL CONTENT ----
if st.session_state.authenticated:
    # Hero Section
    st.markdown("""
        <div style="text-align:center;padding:50px 20px">
        <h1 style="font-size:48px;color:#4fd1c5;font-weight:700">Strategic Investment Banking Solutions</h1>
        <p style="max-width:800px;margin:auto;color:#cbd5e1;font-size:18px">
        Access your modules, videos, and activities for each course. Explore resources designed for professional growth in finance.
        </p>
        </div>
    """, unsafe_allow_html=True)

    # Announcements
    st.subheader("📢 Announcements")
    st.info("""
    - Course will begin next week.  
    - Modules and resources will be updated regularly.  
    - Check back here for latest news and updates.  
    """)

    # Tabs for Courses
    tab1, tab2, tab3, tab4 = st.tabs([
        "Investment Banking", "Financial Services", "Business Ethics", "Business Strategy"
    ])

    # ---- Investment Banking Tab ----
    with tab1:
        st.header("Investment Banking Modules")
        ib_pdfs = ["Module1.pdf", "Module2.pdf", "Module3.pdf", "Module4.pdf", "Module5.pdf"]
        for pdf in ib_pdfs:
            with st.container():
                st.markdown(f'<div class="module-card">', unsafe_allow_html=True)
                if os.path.exists(pdf):
                    with open(pdf, "rb") as f:
                        st.download_button(label=f"Download {pdf}", data=f, file_name=pdf, mime="application/pdf")
                else:
                    st.warning(f"{pdf} not found.")
                st.markdown('</div>', unsafe_allow_html=True)

        st.header("Videos")
        st.markdown(f'<div class="module-card">Video links for Investment Banking will be added here.</div>', unsafe_allow_html=True)

        st.header("Activities")
        st.markdown(f'<div class="module-card">Activities for Investment Banking will be added here.</div>', unsafe_allow_html=True)

    # ---- Financial Services Tab ----
    with tab2:
        st.header("Financial Services Modules")
        st.markdown(f'<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Ethics Tab ----
    with tab3:
        st.header("Business Ethics Modules")
        st.markdown(f'<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Strategy Tab ----
    with tab4:
        st.header("Business Strategy Modules")
        st.markdown(f'<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

