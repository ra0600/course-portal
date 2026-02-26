import streamlit as st
import os

st.set_page_config(page_title="Housing Finance Course Portal", layout="wide")

st.title("Housing Finance – Course Portal")

st.markdown("Welcome to the Housing Finance academic portal. Access modules, videos, case studies, and learning activities below.")

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

    st.subheader("Introduction to Housing Finance")
    st.video("https://www.youtube.com/watch?v=9Y7pK3k5QeA")

    st.subheader("How Mortgage Markets Work")
    st.video("https://www.youtube.com/watch?v=1F7kW4FqL6Y")

    st.subheader("Mortgage Risk and Financial Crisis Explanation")
    st.video("https://www.youtube.com/watch?v=2nBPN-MKefA")
# -----------------------------
# Activities & References
# -----------------------------
elif menu == "Activities & References":
    st.header("Learning Activities")

    st.write("### Activity 1")
    st.write("Analyse the structure of housing finance institutions in your country.")

    st.write("### Activity 2")
    st.write("Compare fixed vs floating mortgage rates with real examples.")

    st.write("### Activity 3")
    st.write("Design a low income housing finance model.")

    st.divider()

    st.header("Reference Books")

    reference_book_path = "books/reference_book1.pdf"

    if os.path.exists(reference_book_path):
        with open(reference_book_path, "rb") as f:
            st.download_button(
                "Download Reference Book",
                f,
                "reference_book1.pdf"
            )
    else:
        st.info("Upload reference book inside books folder to enable download.")

