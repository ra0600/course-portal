import streamlit as st
import os
import pandas as pd
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

st.set_page_config(page_title="Investment Banking & Financial Services Course Portal", layout="wide")

# =============================
# FILE SETUP
# =============================
VISIT_FILE = "app_visits.csv"
RESULT_FILE = "quiz_results.csv"

if not os.path.exists(VISIT_FILE):
    pd.DataFrame(columns=["timestamp"]).to_csv(VISIT_FILE, index=False)

if not os.path.exists(RESULT_FILE):
    pd.DataFrame(columns=["timestamp","quiz","student_name","student_id","score"]).to_csv(RESULT_FILE, index=False)

# Record visit
visit_df = pd.read_csv(VISIT_FILE)
visit_df = pd.concat([visit_df, pd.DataFrame([{"timestamp": datetime.now()}])], ignore_index=True)
visit_df.to_csv(VISIT_FILE, index=False)

# =============================
# PASSWORD SETTINGS
# =============================
PASSWORD = "bbafs23"
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.markdown("<h2 style='text-align:center;'>IBFS Course Portal Login</h2>", unsafe_allow_html=True)
    pwd = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")

if not st.session_state.authenticated:
    login()
    st.stop()

with st.sidebar:
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# =============================
# MAIN TITLE
# =============================
st.markdown(
    "<h1 style='text-align:center; color:#0A3D62;'>Investment Banking & Financial Services Course Portal</h1>",
    unsafe_allow_html=True
)

menu = st.sidebar.selectbox(
    "Select Section",
    ["Course Overview","Modules","Case Study","Video Lectures","Activities & References","Assessment","Admin Analytics"]
)

# =============================
# COURSE OVERVIEW
# =============================
if menu == "Course Overview":
    st.header("Course Overview")
    st.write("""
    - Indian Financial System
    - Housing Finance
    - Leasing & Hire Purchase
    - Mortgage Markets
    - Risk Management
    - Alternative Investments
    """)

# =============================
# MODULES
# =============================
elif menu == "Modules":
    st.header("Course Modules")
    modules = ["Module1.pdf","Module2.pdf","Module3.pdf","Module4.pdf","Module5.pdf"]
    for module in modules:
        if os.path.exists(module):
            with open(module,"rb") as f:
                st.download_button(f"Download {module}",f,file_name=module)

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

# =============================
# ASSESSMENT
# =============================
elif menu == "Assessment":
    st.header("Course Assessment")

    quiz_option = st.selectbox(
        "Select Quiz",
        ["Quiz 1","Quiz 2","Quiz 3"]
    )

    student_name = st.text_input("Student Name")
    student_id = st.text_input("Student RRN")

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = {}

    def run_quiz(quiz_key, questions, correct_answers):

        if quiz_key not in st.session_state.quiz_data:
            st.session_state.quiz_data[quiz_key] = {"submitted":False,"score":0,"answers":{}}

        quiz_state = st.session_state.quiz_data[quiz_key]

        if not quiz_state["submitted"]:
            answers = {}
            for i,(q,opts) in enumerate(questions.items()):
                answers[f"q{i+1}"] = st.radio(q,opts,key=f"{quiz_key}_{i}")

            if st.button("Submit Quiz"):
                if student_name=="" or student_id=="":
                    st.warning("Enter student details")
                else:
                    score=0
                    for key in correct_answers:
                        if answers[key]==correct_answers[key]:
                            score+=1

                    quiz_state["submitted"]=True
                    quiz_state["score"]=score
                    quiz_state["answers"]=answers

                    # Save to CSV
                    result_df=pd.read_csv(RESULT_FILE)
                    new_row=pd.DataFrame([{
                        "timestamp":datetime.now(),
                        "quiz":quiz_key,
                        "student_name":student_name,
                        "student_id":student_id,
                        "score":score
                    }])
                    result_df=pd.concat([result_df,new_row],ignore_index=True)
                    result_df.to_csv(RESULT_FILE,index=False)

                    st.rerun()

        else:
            score=quiz_state["score"]
            total=len(correct_answers)
            st.success(f"Score: {score}/{total}")

            # Generate PDF
            pdf_file=f"{quiz_key}_certificate.pdf"
            doc=SimpleDocTemplate(pdf_file,pagesize=A4)
            styles=getSampleStyleSheet()
            elements=[]
            elements.append(Paragraph("<b>Investment Banking & Financial Services</b>",styles["Title"]))
            elements.append(Paragraph("<b>Certificate of Assessment</b>",styles["Title"]))
            elements.append(Spacer(1,1*inch))
            elements.append(Paragraph(f"Student Name: {student_name}",styles["Normal"]))
            elements.append(Paragraph(f"Student ID: {student RRN}",styles["Normal"]))
            elements.append(Paragraph(f"Quiz: {quiz_option}",styles["Normal"]))
            elements.append(Paragraph(f"Score: {score}/{total}",styles["Normal"]))
            doc.build(elements)

            with open(pdf_file,"rb") as f:
                st.download_button("Download PDF Certificate",f,file_name=pdf_file)

            if st.button("Reset Quiz"):
                st.session_state.quiz_data[quiz_key]["submitted"]=False
                st.rerun()

    # QUIZ DEFINITIONS
    if quiz_option=="Quiz 1":
        questions={
            "RBI is the:":["Central Bank","Commercial Bank","Insurance Company","Stock Exchange"],
            "SEBI regulates:":["Bank loans","Capital markets","Insurance","Microfinance"],
            "NABARD supports:":["Agriculture finance","Stock trading","IPO listing","Urban housing"]
        }
        correct={"q1":"Central Bank","q2":"Capital markets","q3":"Agriculture finance"}
        run_quiz("quiz1",questions,correct)

    elif quiz_option=="Quiz 2":
        questions={
            "Mortgage loan secured against:":["Gold","Inventory","Property","Shares"],
            "Floating rate varies with:":["GDP","Market interest rate","Tax rate","Inflation"],
            "EMI stands for:":["Equated Monthly Installment","Electronic Money Input","Equity Market Indicator","Equal Mortgage Index"],
            "Housing finance provides:":["Car loans","Home loans","Business loans","Education loans"],
            "Fixed rate means:":["Interest constant","Interest changes","No interest","Variable repayment"]
        }
        correct={
            "q1":"Property",
            "q2":"Market interest rate",
            "q3":"Equated Monthly Installment",
            "q4":"Home loans",
            "q5":"Interest constant"
        }
        run_quiz("quiz2",questions,correct)

    elif quiz_option=="Quiz 3":
        questions={
            "IPO stands for:":["Initial Public Offer","Internal Public Option","Indian Portfolio Order","Investment Public Office"],
            "Investment banks deal with:":["Retail deposits","Corporate finance","Savings accounts","Agricultural loans"],
            "Underwriting means:":["Selling insurance","Guaranteeing securities","Providing loans","Managing deposits"],
            "M&A belongs to:":["Retail banking","Corporate finance","Microfinance","Rural banking"],
            "Alternative investments include:":["Fixed deposits","Hedge funds","Savings account","Recurring deposits"]
        }
        correct={
            "q1":"Initial Public Offer",
            "q2":"Corporate finance",
            "q3":"Guaranteeing securities",
            "q4":"Corporate finance",
            "q5":"Hedge funds"
        }
        run_quiz("quiz3",questions,correct)

# =============================
# ADMIN ANALYTICS (PROTECTED)
# =============================
elif menu == "Admin Analytics":

    # Initialize admin session state
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False

    if not st.session_state.admin_authenticated:
        st.subheader("Admin Login Required")
        admin_pwd = st.text_input("Enter Admin Password", type="password")

        if st.button("Login as Admin"):
            if admin_pwd == ADMIN_PASSWORD:
                st.session_state.admin_authenticated = True
                st.success("Admin Access Granted")
                st.rerun()
            else:
                st.error("Incorrect Admin Password")

    else:
        st.header("Admin Dashboard")

        visit_df = pd.read_csv(VISIT_FILE)
        result_df = pd.read_csv(RESULT_FILE)

        st.write(f"Total App Opens: {len(visit_df)}")
        st.write(f"Total Quiz Attempts: {len(result_df)}")

        if not result_df.empty:
            st.subheader("Attempts by Quiz")
            st.dataframe(result_df["quiz"].value_counts())

            st.subheader("Average Score by Quiz")
            st.dataframe(result_df.groupby("quiz")["score"].mean())

            st.subheader("All Student Results")
            st.dataframe(result_df)

        if st.button("Logout Admin"):
            st.session_state.admin_authenticated = False
            st.rerun()










