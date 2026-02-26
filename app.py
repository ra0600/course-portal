import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Investment Banking Course Portal",
    page_icon="📘",
    layout="wide"
)

# ---- DARK BLUE PROFESSIONAL STYLING ----
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#060b17,#0b1220,#060b17);
    color: #ffffff;
}

/* Floating effect */
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

@keyframes float { 
    from { transform:translateY(0px) translateX(0px) } 
    to { transform:translateY(60px) translateX(40px) } 
}

/* Login input */
div.stTextInput input {
    color:#ffffff;
    background-color:#0b1220;
    border:1px solid #4fd1c5;
}

/* Login button */
div.stButton>button {
    color:#ffffff;
    background-color:#4fd1c5;
    font-weight:600;
    border-radius:6px;
}

/* Download buttons styled as clean white text */
div.stDownloadButton > button {
    background-color: transparent;
    color: white;
    border: none;
    padding: 0;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
}

div.stDownloadButton > button:hover {
    color: #4fd1c5;
    background-color: transparent;
}

/* Module card */
.module-card {
    background: rgba(17,27,51,0.75);
    padding: 15px 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.06);
}

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
            st.rerun()
        else:
            st.error("Incorrect Access Code")

# ---- PORTAL CONTENT ----
if st.session_state.authenticated:

    # Hero Section
    st.markdown("""
    <div style="text-align:center; padding:50px 20px">
        <h1 style="font-size:48px; color:#4fd1c5; font-weight:700;">
        Investment Banking Solutions
        </h1>
        <p style="max-width:800px; margin:auto; color:#cbd5e1; font-size:18px;">
        Access your modules, videos, and activities for each course.
        Explore resources designed for professional growth in finance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Announcements
    st.subheader("📢 Announcements")
    st.markdown("""
    <ul>
        <li>Course materials and videos are available here.</li>
        <li>Modules and resources will be updated regularly.</li>
        <li>Check back here for latest news and updates.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Investment Banking",
        "Financial Services",
        "Business Ethics",
        "Business Strategy"
    ])

    # ---- Investment Banking ----
    with tab1:
        st.header("Investment Banking Modules")

        ib_pdfs = [
            "Module1.pdf",
            "Module2.pdf",
            "Module3.pdf",
            "Module4.pdf",
            "Module5.pdf"
        ]

        for pdf in ib_pdfs:
            if os.path.exists(pdf):
                with open(pdf, "rb") as f:
                    st.download_button(
                        label=pdf,
                        data=f,
                        file_name=pdf,
                        mime="application/pdf",
                        key=pdf
                    )
            else:
                st.warning(f"{pdf} not found.")

        st.header("Videos")
        st.markdown('<div class="module-card">Video links will be added here.</div>', unsafe_allow_html=True)

        st.header("Activities")
        st.markdown('<div class="module-card">Activities will be added here.</div>', unsafe_allow_html=True)

    # ---- Financial Services ----
    with tab2:
        st.header("Financial Services Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Ethics ----
    with tab3:
        st.header("Business Ethics Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)

    # ---- Business Strategy ----
    with tab4:
        st.header("Business Strategy Modules")
        st.markdown('<div class="module-card">Modules and resources will be added soon.</div>', unsafe_allow_html=True)
