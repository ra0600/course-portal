import streamlit as st
import os

st.set_page_config(page_title="Housing Finance Course Portal", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color:#0A3D62;'>Housing Finance Course Portal</h1>",
    unsafe_allow_html=True
)

st.title("Investment Banking & Financial Services – Course Portal")

st.markdown("Welcome to the IBFS academic portal. Access modules, videos, case studies, and learning activities below.")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Select Section",
    ["Course Overview", "Modules", "Case Study", "Video Lectures", "Activities & References"]
)

# -----------------------------
# Course Overview
# -----------------------------
if menu == "Course Overview":
    st.header("Course Overview")
    st.write("""
    This course covers:
    - Housing finance systems
    - Mortgage markets
    - Risk management
    - Regulatory frameworks
    - Affordable housing finance
    """)

# -----------------------------
# Modules Section
# -----------------------------
elif menu == "Modules":
    st.header("Course Modules")

    modules = [
        "Module1.pdf",
        "Module2.pdf",
        "Module3.pdf",
        "Module4.pdf",
        "Module5.pdf"
    ]

    for module in modules:
        if os.path.exists(module):
            with open(module, "rb") as f:
                st.download_button(
                    label=f"Download {module}",
                    data=f,
                    file_name=module
                )
        else:
            st.warning(f"{module} not found")

# -----------------------------
# Case Study Section
# -----------------------------
elif menu == "Case Study":
    st.header("Case Study – Housing Finance")

    case_path = "cases/housing_finance_case.docx"

    if os.path.exists(case_path):
        with open(case_path, "rb") as f:
            st.download_button(
                "Download Housing Finance Case Study",
                f,
                "housing_finance_case.docx"
            )
    else:
        st.warning("Case study file not found")

# -----------------------------
# Video Section
# -----------------------------
elif menu == "Video Lectures":
    st.header("Video Lectures")

    st.subheader("Leasing vs Hire Purchase")
    st.video("https://youtu.be/Ktnr6fXrurc")

    st.subheader("Factoring vs Forfaiting")
    st.video("https://www.youtube.com/watch?v=tppLiwVukis")

    st.subheader("Role of Investment Banking")
    st.video("https://youtu.be/qCgojEvwcOk")
    
    st.subheader("Introduction to the Indian Financial System")
    st.video("https://youtu.be/CtoCQvO67u4")

    st.subheader("Housing Finance in India")
    st.video("https://youtu.be/-0YJ06Sq_Cs")
    
    st.subheader("The IPO Journey Explained")
    st.video("https://youtu.be/U4f_V5Myph0")
    
    st.subheader("Alternative Investments")
    st.video("https://youtu.be/MMMd3sNq5VY")
# -----------------------------
# Activities & References
# -----------------------------
elif menu == "Activities & References":
    st.header("Learning Activities")

    st.write("### Activity 1")
    st.write("Analyse the structure of housing finance institutions in your country.")

    st.write("### Activity 2")
    st.write("Compare fixed and floating mortgage rate systems.")

    st.write("### Activity 3")
    st.write("Develop a sustainable affordable housing finance model.")

    st.divider()

    st.header("Reference Book")

    book_path = "books/housing_finance_reference.pdf"

    if os.path.exists(book_path):
        with open(book_path, "rb") as f:
            st.download_button(
                "Download Housing Finance Reference Book",
                f,
                "housing_finance_reference.pdf"
            )
    else:
        st.info("Reference book not uploaded yet.")





