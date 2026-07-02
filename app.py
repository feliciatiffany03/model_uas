import streamlit as st
import pandas as pd
from inferencing import CreditScoreInference

st.set_page_config(
page_title="Credit Score Prediction",
page_icon="💳"
)

st.title("💳 Credit Score Prediction System")

model = CreditScoreInference()

st.header("Customer Information")

age = st.number_input("Age", 18, 100, 30)

annual_income = st.number_input(
"Annual Income",
min_value=0.0,
value=50000.0
)

num_bank_accounts = st.number_input(
"Number of Bank Accounts",
min_value=0,
value=2
)

num_credit_card = st.number_input(
"Number of Credit Cards",
min_value=0,
value=2
)

interest_rate = st.number_input(
"Interest Rate",
min_value=0,
value=10
)

outstanding_debt = st.number_input(
"Outstanding Debt",
min_value=0.0,
value=500.0
)

num_loan = st.number_input(
    "Number of Loans",
    min_value=0,
    max_value=20,
    value=2
)

delay_due = st.number_input(
    "Delay From Due Date",
    min_value=0,
    max_value=100,
    value=5
)

num_delayed = st.number_input(
    "Number of Delayed Payments",
    min_value=0,
    max_value=100,
    value=1
)

credit_inquiries = st.number_input(
    "Credit Inquiries",
    min_value=0,
    max_value=100,
    value=2
)

credit_mix = st.selectbox(
"Credit Mix",
["Good", "Standard", "Bad"]
)

payment_min = st.selectbox(
"Payment of Minimum Amount",
["Yes", "No"]
)

if st.button("Predict Credit Score"):
    
    sample = pd.DataFrame({
        "Age":[age],
        "Annual_Income":[annual_income],
        "Monthly_Inhand_Salary":[3000],
        "Num_Bank_Accounts":[num_bank_accounts],
        "Num_Credit_Card":[num_credit_card],
        "Interest_Rate":[interest_rate],
        "Num_of_Loan":[num_loan],
        "Delay_from_due_date":[delay_due],
        "Num_of_Delayed_Payment":[num_delayed],
        "Changed_Credit_Limit":[5],
        "Num_Credit_Inquiries":[credit_inquiries],
        "Outstanding_Debt":[outstanding_debt],
        "Credit_Utilization_Ratio":[25],
        "Total_EMI_per_month":[100],
        "Amount_invested_monthly":[200],
        "Monthly_Balance":[500],
        "Month":["January"],
        "Occupation":["Engineer"],
        "Type_of_Loan":["Personal Loan"],
        "Credit_Mix":[credit_mix],
        "Credit_History_Age":["20 Years and 1 Months"],
        "Payment_of_Min_Amount":[payment_min],
        "Payment_Behaviour":[
            "High_spent_Small_value_payments"
        ]
    })

    prediction = model.predict(sample)

    st.success(
        f"Predicted Credit Score : {prediction}"
    )

