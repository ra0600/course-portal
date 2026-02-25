import streamlit as st
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Investment Banking Course Portal",
    page_icon="📘",
    layout="wide"
)

# ---- CSS for dark card + black download text ----
st.markdown("""
<style>
.stApp { background-color: #0b1220; color: #ffffff; }

.module-card {
    background: rgba(17,27,51,0.75);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
}

/* Make download button look like plain black text */
.stButton>button {
    all: unset;               /* remove default styling */
    color: #000000;           /* black text */
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;
}
.stButton>button:hover {
    color: #4fd1c5;           /* hover color */
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ---- PASSWORD ----
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

# ---- PORTAL ----
if st.session_state.authenticated:
    st.subheader("Investment Banking Modules")
    ib_pdfs = ["Module1.pdf", "Module2.pdf", "Module3.pdf", "Module4.pdf", "Module5.pdf"]
    for pdf in ib_pdfs:
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        if os.path.exists(pdf):
            with open(pdf, "rb") as f:
                st.download_button(label=pdf, data=f, file_name=pdf, mime="application/pdf")
        else:
            st.warning(f"{pdf} not found.")
        st.markdown('</div>', unsafe_allow_html=True)
