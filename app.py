import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import plotly.graph_objects as go
import plotly.express as px

from streamlit_option_menu import option_menu

from report_generator import create_pdf


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(

    page_title="CrediGuard AI",

    page_icon="🏦",

    layout="wide"

)



# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    with open("model.pkl","rb") as file:

        model = pickle.load(file)

    return model



model = load_model()



# =====================================================
# SIDEBAR
# =====================================================


with st.sidebar:


    st.image(

        "https://img.icons8.com/color/96/bank-building.png",

        width=80

    )


    st.title(
        "CrediGuard AI"
    )


    selected = option_menu(

        menu_title="Navigation",

        options=[

            "Dashboard",

            "Prediction",

            "Model Insights",

            "Business Impact",

            "About"

        ],


        icons=[

            "speedometer2",

            "graph-up",

            "pie-chart",

            "cash-stack",

            "info-circle"

        ],


        default_index=0

    )



# =====================================================
# DASHBOARD
# =====================================================


if selected=="Dashboard":


    st.title(
        "🏦 CrediGuard AI Dashboard"
    )


    st.subheader(
        "Explainable AI Based Loan Default Prediction System"
    )


    st.write(
    """
    CrediGuard AI helps financial institutions predict
    loan default risk and estimate potential financial loss
    before approving loans.
    """
    )



    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.metric(

            "Model",

            "Logistic Regression"

        )


    with c2:

        st.metric(

            "ROC-AUC",

            "0.723"

        )


    with c3:

        st.metric(

            "Explainability",

            "SHAP"

        )


    with c4:

        st.metric(

            "Decision",

            "Risk Based"

        )



    st.divider()



    st.subheader(
        "📌 Project Highlights"
    )


    col1,col2 = st.columns(2)



    with col1:

        st.info(
        """
        ### Machine Learning

        ✔ Loan Default Prediction

        ✔ Class Imbalance Handling

        ✔ Probability Based Risk Score

        ✔ Threshold Optimization
        """
        )



    with col2:

        st.success(
        """
        ### Business Value

        ✔ Expected Loss Calculation

        ✔ Loan Approval Support

        ✔ Financial Risk Analysis

        ✔ Explainable Decisions
        """
        )



# Prediction page will continue in PART 2

# =====================================================
# PREDICTION PAGE
# =====================================================


elif selected=="Prediction":


    st.title("🏦 Loan Risk Assessment")


    st.write(
        "Enter applicant information to predict default probability."
    )



    st.subheader("👤 Personal Information")


    c1,c2 = st.columns(2)



    with c1:


        annual_inc = st.number_input(

            "Annual Income ($)",

            value=60000.0

        )


        emp_length = st.selectbox(

            "Employment Length",

            [

            "< 1 year",
            "1 year",
            "2 years",
            "3 years",
            "4 years",
            "5 years",
            "6 years",
            "7 years",
            "8 years",
            "9 years",
            "10+ years"

            ]

        )



    with c2:


        home_ownership = st.selectbox(

            "Home Ownership",

            [

            "RENT",
            "OWN",
            "MORTGAGE",
            "OTHER"

            ]

        )


        verification_status = st.selectbox(

            "Verification Status",

            [

            "Not Verified",
            "Verified",
            "Source Verified"

            ]

        )



    # ================================
    # LOAN INFORMATION
    # ================================


    st.subheader("💰 Loan Information")


    c3,c4 = st.columns(2)



    with c3:


        loan_amnt = st.number_input(

            "Loan Amount",

            value=10000.0

        )


        term = st.selectbox(

            "Term",

            [36,60]

        )


        int_rate = st.number_input(

            "Interest Rate",

            value=12.5

        )



    with c4:


        installment = st.number_input(

            "Installment",

            value=320.0

        )


        purpose = st.selectbox(

            "Purpose",

            [

            "credit_card",
            "debt_consolidation",
            "home_improvement",
            "small_business",
            "major_purchase",
            "medical",
            "car",
            "vacation",
            "moving",
            "other"

            ]

        )



    # ================================
    # CREDIT INFORMATION
    # ================================


    st.subheader("📈 Credit Information")


    c5,c6 = st.columns(2)



    with c5:


        open_acc = st.number_input(

            "Open Accounts",

            value=8

        )


        total_acc = st.number_input(

            "Total Accounts",

            value=20

        )


        mort_acc = st.number_input(

            "Mortgage Accounts",

            value=1

        )


        pub_rec = st.number_input(

            "Public Records",

            value=0

        )



    with c6:


        revol_bal = st.number_input(

            "Revolving Balance",

            value=5000

        )


        revol_util = st.number_input(

            "Revolving Utilization %",

            value=40.0

        )


        dti = st.number_input(

            "Debt To Income Ratio",

            value=15.0

        )


        pub_rec_bankruptcies = st.number_input(

            "Public Record Bankruptcies",

            value=0

        )



    # ================================
    # ADDITIONAL DETAILS
    # ================================


    st.subheader("📄 Additional Details")



    grade = st.selectbox(

        "Grade",

        [

        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"

        ]

    )



    sub_grade = st.selectbox(

        "Sub Grade",

        [

        "A1","A2","A3","A4","A5",

        "B1","B2","B3","B4","B5",

        "C1","C2","C3","C4","C5",

        "D1","D2","D3","D4","D5",

        "E1","E2","E3","E4","E5",

        "F1","F2","F3","F4","F5",

        "G1","G2","G3","G4","G5"

        ]

    )



    issue_d = st.selectbox(

        "Issue Date",

        [

        "Jan-2016",
        "Apr-2016",
        "Jul-2016",
        "Oct-2016"

        ]

    )



    earliest_cr_line = st.selectbox(

        "Earliest Credit Line",

        [

        "Jan-2000",
        "Jan-2005",
        "Jan-2010",
        "Jan-2012"

        ]

    )



    initial_list_status = st.selectbox(

        "Initial List Status",

        [

        "w",
        "f"

        ]

    )



    application_type = st.selectbox(

        "Application Type",

        [

        "INDIVIDUAL",
        "JOINT"

        ]

    )



    # ================================
    # FEATURE ENGINEERING
    # ================================


    has_bankruptcy = (

        1 if pub_rec_bankruptcies > 0 else 0

    )


    public_record_risk = (

        pub_rec + pub_rec_bankruptcies

    )


    high_utilization = (

        1 if revol_util > 80 else 0

    )



    st.divider()



    predict = st.button(

        "🔍 Predict Loan Risk",

        use_container_width=True

    )



    if predict:


        with st.spinner(

            "Analyzing Applicant Profile..."

        ):


            time.sleep(1)



            input_df = pd.DataFrame({


                "loan_amnt":[loan_amnt],

                "term":[term],

                "int_rate":[int_rate],

                "installment":[installment],


                "grade":[grade],

                "sub_grade":[sub_grade],


                "emp_length":[emp_length],

                "home_ownership":[home_ownership],


                "annual_inc":[annual_inc],

                "verification_status":[verification_status],


                "issue_d":[issue_d],

                "purpose":[purpose],


                "dti":[dti],

                "earliest_cr_line":[earliest_cr_line],


                "open_acc":[open_acc],

                "pub_rec":[pub_rec],


                "revol_bal":[revol_bal],

                "revol_util":[revol_util],


                "total_acc":[total_acc],


                "initial_list_status":[initial_list_status],


                "application_type":[application_type],


                "mort_acc":[mort_acc],


                "pub_rec_bankruptcies":[pub_rec_bankruptcies],


                "loan_income_ratio":[loan_amnt/annual_inc],


                "installment_income_ratio":[installment/annual_inc],


                "has_bankruptcy":[has_bankruptcy],


                "public_record_risk":[public_record_risk],


                "high_utilization":[high_utilization]


            })



            probability = model.predict_proba(

                input_df

            )[0][1]



            threshold = 0.4



            prediction = (

                1 if probability >= threshold else 0

            )



            risk_score = probability*100



            expected_loss = probability*(loan_amnt*0.60)



            # Store values for Business Impact page

            st.session_state["probability"] = probability

            st.session_state["loan_amount"] = loan_amnt

            st.session_state["expected_loss"] = expected_loss



        st.subheader(
            "📊 Prediction Result"
        )



        c1,c2,c3 = st.columns(3)



        c1.metric(

            "Risk Score",

            f"{risk_score:.2f}%"

        )



        c2.metric(

            "Prediction",

            "Default" if prediction==1 else "Non Default"

        )



        c3.metric(

            "Decision",

            "Reject" if prediction==1 else "Approve"

        )



        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=risk_score,

                title={

                    "text":"Default Risk"

                },

                gauge={

                    "axis":{

                        "range":[0,100]

                    }

                }

            )

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )



        st.subheader(
            "💰 Expected Loss"
        )



        st.metric(

            "Estimated Loss",

            f"₹ {expected_loss:,.0f}"

        )



# =====================================================
# MODEL INSIGHTS
# =====================================================


elif selected=="Model Insights":


    st.title("📊 Model Insights")


    st.write(
    """
    ## Machine Learning Model

    **Algorithm:** Logistic Regression

    **Purpose:** Predict loan default probability

    **Evaluation Metrics:**

    - ROC-AUC Score: 0.723

    - Class balancing applied

    - Probability based prediction

    - Threshold optimization used


    ## Explainable AI (XAI)

    SHAP (SHapley Additive exPlanations) is used
    to understand how each feature influences
    the final prediction.


    Important risk factors:

    ✔ Interest Rate

    ✔ Debt To Income Ratio

    ✔ Revolving Utilization

    ✔ Annual Income

    ✔ Loan Amount

    ✔ Credit History

    """
    )



    st.info(
    """
    SHAP explanation helps banks understand
    why a loan application is considered risky.
    """
    )





# =====================================================
# BUSINESS IMPACT
# =====================================================


elif selected=="Business Impact":



    st.title("💰 Business Impact Analysis")



    st.write(
    """
    Convert machine learning predictions into
    financial decisions for banking operations.
    """
    )



    if "probability" not in st.session_state:


        st.warning(
            "⚠️ Please perform a loan prediction first."
        )


        st.stop()



    probability = st.session_state["probability"]


    loan_amount = st.session_state["loan_amount"]


    expected_loss = st.session_state["expected_loss"]



    # Bank assumptions


    LOSS_GIVEN_DEFAULT = 0.60


    PROCESSING_FEE = 2500



    expected_profit = (

        (1-probability)

        *

        PROCESSING_FEE

    )



    st.subheader(
        "📊 Financial Summary"
    )



    c1,c2,c3 = st.columns(3)



    with c1:


        st.metric(

            "Loan Amount",

            f"₹ {loan_amount:,.0f}"

        )



    with c2:


        st.metric(

            "Expected Loss",

            f"₹ {expected_loss:,.0f}"

        )



    with c3:


        st.metric(

            "Expected Profit",

            f"₹ {expected_profit:,.0f}"

        )




    st.divider()



    # Decision


    st.subheader(
        "🏦 Loan Decision"
    )



    if probability < 0.40:



        recommendation = "Approve"


        st.success(

        """
        ### ✅ APPROVE

        Low default probability.

        Financial risk is acceptable.

        """

        )



    elif probability < 0.60:



        recommendation = "Manual Review"


        st.warning(

        """
        ### 🟡 MANUAL REVIEW

        Moderate risk applicant.

        Additional verification recommended.

        """

        )



    else:



        recommendation = "Reject"


        st.error(

        """
        ### 🔴 REJECT

        High default probability.

        Expected financial loss is high.

        """

        )




    # Financial chart


    st.subheader(
        "📈 Financial Impact"
    )



    chart = pd.DataFrame({

        "Category":

        [

        "Expected Loss",

        "Expected Profit"

        ],


        "Amount":

        [

        expected_loss,

        expected_profit

        ]

    })



    fig = px.bar(

        chart,

        x="Category",

        y="Amount",

        text="Amount",

        title="Loan Financial Impact"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )




    # Risk Category


    st.subheader(
        "📌 Risk Category"
    )



    if probability < 0.40:

        risk="LOW"


    elif probability <0.60:

        risk="MEDIUM"


    else:

        risk="HIGH"



    st.metric(

        "Risk Level",

        risk

    )




    # Summary Table


    summary = pd.DataFrame({


        "Metric":

        [

        "Loan Amount",

        "Default Probability",

        "Expected Loss",

        "Expected Profit",

        "Recommendation"

        ],


        "Value":

        [

        f"₹ {loan_amount:,.0f}",

        f"{probability*100:.2f}%",

        f"₹ {expected_loss:,.0f}",

        f"₹ {expected_profit:,.0f}",

        recommendation

        ]

    })



    st.subheader(
        "📄 Decision Summary"
    )



    st.table(summary)




    # PDF REPORT


    st.divider()



    st.subheader(
        "📄 Generate Loan Report"
    )



    if st.button(
        "Generate PDF Report"
    ):



        create_pdf(

            "Loan_Report.pdf",

            loan_amount,

            0,

            0,

            "N/A",

            "N/A",

            probability,

            recommendation,

            expected_loss

        )



        with open(
            "Loan_Report.pdf",
            "rb"
        ) as file:



            st.download_button(

                label="⬇️ Download Report",

                data=file,

                file_name="Loan_Report.pdf",

                mime="application/pdf"

            )







# =====================================================
# ABOUT PAGE
# =====================================================


elif selected=="About":



    st.title(
        "ℹ️ About CrediGuard AI"
    )



    st.write(
    """
    ## CrediGuard AI

    CrediGuard AI is an Explainable AI based
    loan default prediction system.

    ### Features:

    ✔ Machine Learning Risk Prediction

    ✔ Default Probability Calculation

    ✔ Expected Loss Estimation

    ✔ Business Impact Analysis

    ✔ SHAP Explainability

    ✔ PDF Decision Report


    Developed as an AI powered banking
    decision support system.
    """
    )

