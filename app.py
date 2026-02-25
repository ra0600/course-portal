import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Investment Banking Course Portal",
    page_icon="📘",
    layout="wide"
)

# ---- CSS STYLING ----
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 20% 20%, rgba(79,209,197,0.15), transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(14,165,233,0.15), transparent 40%),
                linear-gradient(135deg,#060b17,#0b1220,#060b17);
    color: #ffffff;
}

/* Floating shapes */
.stApp::before, .stApp::after {
    content: "";
    position: fixed;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    filter: blur(120px);
    z-index: -1;
    animation: float 18s ease-in-out infinite alternate;
}
.stApp::before { background: rgba(79,209,197,0.25); top:-120px; left:-120px; }
.stApp::after { background: rgba(14,165,233,0.25); bottom:-150px; right:-150px; animation-delay:6s; }
@keyframes float { from{transform:translateY(0px) translateX(0px)} to{transform:translateY(60px) translateX(40px)} }

/* Login input text and button in white */
.stTextInput>div>div>input {
    color: #ffffff !important;
    background-color: rgba(0,0,0,0.3);
}
.stButton>button {
    all: unset;           /* remove default gray rectangle */
    color: #ffffff !important;       /* white text */
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;
    text-decoration: underline;
}
.stButton>button:hover {
    color: #4fd1c5;
}

/* Module download links as white text */
.stButton>button.download-button {
    all: unset;         
    color: #ffffff !important;
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;
    text-decoration: underline;
}
.stButton>button.download-button:hover {
    color: #4fd1c5;
}

/* Announcement text white */
.announcement-text {
    color: #ffffff;
    font-weight: 500;
    line-height: 1.6;
}

/* Module card styling */
.module-card {
    background: rgba(17,27,51,0.75);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# ---- PASSWORD PROTECTION ----
PASSWORD = "bbafs23"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login screen
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
    st.markdown("""
    <div class="announcement-text">
    <ul>
    <li>Course will begin next week.</li>
    <li>Modules and resources will be updated regularly.</li>
    <li>Check back here for latest news and updates.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Tabs for Courses
    tab1, tab2, tab3, tab4 = st.tabs([
        "Investment Banking", "Financial Services", "Business Ethics", "Business Strategy"
    ])

    # ---- Investment Banking Tab ----
    with tab1:
    st.header("Investment Banking Modules")
    ib_pdfs = ["Module1.pdf", "Module2.pdf", "Module3.pdf", "Module4.pdf", "Module5.pdf"]

    for pdf in ib_pdfs:
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        if os.path.exists(pdf):
            # White download link
            st.markdown(
                f'<a href="{pdf}" download style="color:white;text-decoration:none;font-weight:600;">{pdf}</a>',
                unsafe_allow_html=True
            )
        else:
            st.warning(f"{pdf} not found.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.header("Videos")
    st.markdown('<div class="module-card">Video links for Investment Banking will be added here.</div>', unsafe_allow_html=True)

    st.header("Activities")
    st.markdown('<div class="module-card">Activities for Investment Banking will be added here.</div>', unsafe_allow_html=True)

    # ---- Financial Services Tab ----
    with tab2:
        st.header("Financial Services Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Ethics Tab ----
    with tab3:
        st.header("Business Ethics Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Strategy Tab ----
    with tab4:
        st.header("Business Strategy Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)




