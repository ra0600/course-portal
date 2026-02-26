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
    ["Course Overview", "Modules", "Case Study", "Video Lectures", "Activities & References", "Assessment"]
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
# Assessment Section
# -----------------------------
elif menu == "Assessment":
    st.header("Course Assessment")

    quiz_option = st.selectbox(
        "Select Quiz",
        [
            "Quiz 1 – Indian Financial System",
            "Quiz 2 – Housing Finance",
            "Quiz 3 – Investment Banking"
        ]
    )

    # Common student details
    student_name = st.text_input("Enter Your Full Name")
    student_id = st.text_input("Enter Student ID")

    # Initialize session states dynamically
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = {}

    # Function to run quiz
    def run_quiz(quiz_key, questions, correct_answers):

        if quiz_key not in st.session_state.quiz_data:
            st.session_state.quiz_data[quiz_key] = {
                "submitted": False,
                "score": 0,
                "answers": {}
            }

        quiz_state = st.session_state.quiz_data[quiz_key]

        if not quiz_state["submitted"]:

            answers = {}

            for i, (question, options) in enumerate(questions.items()):
                answers[f"q{i+1}"] = st.radio(question, options, key=f"{quiz_key}_{i}")

            if st.button("Submit Quiz"):

                if student_name == "" or student_id == "":
                    st.warning("Please enter student details before submitting.")
                else:
                    score = 0
                    for key in correct_answers:
                        if answers[key] == correct_answers[key]:
                            score += 1

                    quiz_state["submitted"] = True
                    quiz_state["score"] = score
                    quiz_state["answers"] = answers
                    st.rerun()

        else:
            score = quiz_state["score"]
            total = len(correct_answers)

            st.success(f"Final Score: {score} / {total}")

            st.write("### Answer Review")

            for key in correct_answers:
                st.write(f"Correct Answer: {correct_answers[key]}")
                st.write(f"Your Answer: {quiz_state['answers'][key]}")
                st.write("---")

            result_text = f"""
Investment Banking & Financial Services Course
----------------------------------------------
Quiz: {quiz_option}
Student Name: {student_name}
Student ID: {student_id}

Final Score: {score} / {total}
"""

            st.download_button(
                "Download Result Slip",
                result_text,
                file_name=f"{quiz_key}_result.txt"
            )

            if st.button("Reset Quiz"):
                st.session_state.quiz_data[quiz_key]["submitted"] = False
                st.rerun()

    # -----------------------------
    # QUIZ 1
    # -----------------------------
    if quiz_option == "Quiz 1 – Indian Financial System":

        questions = {
            "1. RBI is the:": ["Central Bank", "Commercial Bank", "Insurance Company", "Stock Exchange"],
            "2. SEBI regulates:": ["Bank loans", "Capital markets", "Insurance", "Microfinance"],
            "3. NABARD supports:": ["Agriculture finance", "Stock trading", "IPO listing", "Urban housing"]
        }

        correct_answers = {
            "q1": "Central Bank",
            "q2": "Capital markets",
            "q3": "Agriculture finance"
        }

        run_quiz("quiz1", questions, correct_answers)

    # -----------------------------
    # QUIZ 2 – 5 QUESTIONS
    # -----------------------------
    elif quiz_option == "Quiz 2 – Housing Finance":

        questions = {
            "1. Mortgage loan is secured against:": ["Gold", "Inventory", "Property", "Shares"],
            "2. Floating rate loans vary with:": ["GDP", "Market interest rate", "Tax rate", "Inflation"],
            "3. EMI stands for:": ["Equated Monthly Installment", "Equal Mortgage Index", "Electronic Money Input", "Equity Market Indicator"],
            "4. Housing finance companies mainly provide:": ["Car loans", "Home loans", "Business loans", "Education loans"],
            "5. Fixed rate loans mean:": ["Interest changes yearly", "Interest remains constant", "No interest", "Variable repayment"]
        }

        correct_answers = {
            "q1": "Property",
            "q2": "Market interest rate",
            "q3": "Equated Monthly Installment",
            "q4": "Home loans",
            "q5": "Interest remains constant"
        }

        run_quiz("quiz2", questions, correct_answers)

    # -----------------------------
    # QUIZ 3 – 5 QUESTIONS
    # -----------------------------
    elif quiz_option == "Quiz 3 – Investment Banking":

        questions = {
            "1. IPO stands for:": ["Initial Public Offer", "Internal Public Option", "Indian Portfolio Order", "Investment Public Office"],
            "2. Investment banks deal primarily with:": ["Retail deposits", "Corporate finance", "Savings accounts", "Agricultural loans"],
            "3. Underwriting means:": ["Selling insurance only", "Guaranteeing issue of securities", "Providing loans", "Managing deposits"],
            "4. Mergers and acquisitions are part of:": ["Retail banking", "Corporate finance", "Microfinance", "Rural banking"],
            "5. Alternative investments include:": ["Fixed deposits", "Hedge funds", "Savings account", "Recurring deposits"]
        }

        correct_answers = {
            "q1": "Initial Public Offer",
            "q2": "Corporate finance",
            "q3": "Guaranteeing issue of securities",
            "q4": "Corporate finance",
            "q5": "Hedge funds"
        }

        run_quiz("quiz3", questions, correct_answers)





