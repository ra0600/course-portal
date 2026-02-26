import streamlit as st
import os

st.set_page_config(page_title="Investment Banking & Financial Services Course Portal", layout="wide")

# -----------------------------
# PASSWORD SETTINGS
# -----------------------------
PASSWORD = "bbafs23"   # ← Change this to your preferred password

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.markdown("<h2 style='text-align:center;'>IBFS Course Portal Login</h2>", unsafe_allow_html=True)
    password_input = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Incorrect password")

# -----------------------------
# LOGIN CHECK
# -----------------------------
if not st.session_state.authenticated:
    login()
    st.stop()

# -----------------------------
# LOGOUT BUTTON
# -----------------------------
with st.sidebar:
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# -----------------------------
# MAIN PORTAL
# -----------------------------
st.markdown(
    "<h1 style='text-align: center; color:#0A3D62;'>Investment Banking & Financial Services Course Portal</h1>",
    unsafe_allow_html=True
)

st.markdown("Welcome to the IBFS academic portal. Access modules, videos, case studies, and learning activities below.")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Select Section",
    ["Course Overview", "Modules", "Case Study", "Video Lectures", "Activities & References", "Quiz"]
)

# -----------------------------
# Course Overview
# -----------------------------
if menu == "Course Overview":
    st.header("Course Overview")
    st.write("""
    This course covers:
    - Indian Financial System
    - Housing finance systems
    - Leasing & Hire Purchase
    - Mortgage markets
    - Risk management
    - Regulatory frameworks
    - Affordable housing finance
    - Alternative Investments
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
    st.video("https://youtu.be/tppLiwVukis")

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


# -----------------------------
# Quiz Section
# -----------------------------
elif menu == "Quiz":
    st.header("IBFS Course Quiz")
    st.write("Answer the following 10 questions:")

    score = 0

    # Question 1
    q1 = st.radio(
        "1. Which institution regulates banks in India?",
        ["SEBI", "RBI", "IRDAI", "NABARD"]
    )
    if q1 == "RBI":
        score += 1

    # Question 2
    q2 = st.radio(
        "2. IPO stands for:",
        ["Initial Public Offer", "Indian Public Offering", "Internal Public Option", "Investment Portfolio Order"]
    )
    if q2 == "Initial Public Offer":
        score += 1

    # Question 3
    q3 = st.radio(
        "3. Leasing is primarily a form of:",
        ["Equity financing", "Debt financing", "Asset financing", "Insurance"]
    )
    if q3 == "Asset financing":
        score += 1

    # Question 4
    q4 = st.radio(
        "4. Factoring is related to:",
        ["Equity shares", "Accounts receivable", "Real estate", "Mutual funds"]
    )
    if q4 == "Accounts receivable":
        score += 1

    # Question 5
    q5 = st.radio(
        "5. Mortgage loan is secured against:",
        ["Machinery", "Inventory", "Property", "Gold"]
    )
    if q5 == "Property":
        score += 1

    # Question 6
    q6 = st.radio(
        "6. SEBI regulates:",
        ["Insurance sector", "Capital markets", "Banking loans", "Microfinance"]
    )
    if q6 == "Capital markets":
        score += 1

    # Question 7
    q7 = st.radio(
        "7. Alternative investments include:",
        ["Savings account", "Fixed deposits", "Hedge funds", "Recurring deposits"]
    )
    if q7 == "Hedge funds":
        score += 1

    # Question 8
    q8 = st.radio(
        "8. Housing finance mainly supports:",
        ["Vehicle loans", "Education loans", "Home purchase", "Gold trading"]
    )
    if q8 == "Home purchase":
        score += 1

    # Question 9
    q9 = st.radio(
        "9. Hire purchase transfers ownership:",
        ["Immediately", "After full payment", "Before payment", "Never"]
    )
    if q9 == "After full payment":
        score += 1

    # Question 10
    q10 = st.radio(
        "10. Investment banks primarily deal with:",
        ["Retail savings", "Government pensions", "Corporate finance and securities", "Agricultural loans"]
    )
    if q10 == "Corporate finance and securities":
        score += 1

    if st.button("Submit Quiz"):
        st.subheader(f"Your Score: {score}/10")

        if score >= 8:
            st.success("Excellent performance!")
        elif score >= 5:
            st.info("Good effort. Review some topics.")
        else:
            st.warning("Please revise the modules and try again.")
