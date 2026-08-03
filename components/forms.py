"""
==========================================================
Customer Input Form Component

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from prediction import CustomerData


# ==========================================================
# Customer Input Form
# ==========================================================

def render_customer_form(
    geography_encoder,
    gender_encoder,
):
    """
    Render the complete customer input form.

    Parameters
    ----------
    geography_encoder
        Trained OneHotEncoder for Geography.

    gender_encoder
        Trained LabelEncoder for Gender.

    Returns
    -------
    tuple
        (
            customer,
            predict_button
        )
    """

    st.header("👤 Customer Information")

    left_col, right_col = st.columns(2)

    # ======================================================
    # Left Column
    # ======================================================

    with left_col:

        geography = st.selectbox(
            label="🌍 Geography",
            options=geography_encoder.categories_[0],
            key="geography",
        )

        gender = st.selectbox(
            label="👤 Gender",
            options=gender_encoder.classes_,
            key="gender",
        )

        age = st.slider(
            label="🎂 Age",
            min_value=18,
            max_value=92,
            value=35,
            key="age",
        )

        credit_score = st.number_input(
            label="💳 Credit Score",
            min_value=300,
            max_value=900,
            value=650,
            step=1,
            key="credit_score",
        )

        tenure = st.slider(
            label="📅 Tenure",
            min_value=0,
            max_value=10,
            value=5,
            key="tenure",
        )

    # ======================================================
    # Right Column
    # ======================================================

    with right_col:

        balance = st.number_input(
            label="💰 Account Balance",
            min_value=0.0,
            value=50000.0,
            step=1000.0,
            format="%.2f",
            key="balance",
        )

        estimated_salary = st.number_input(
            label="💼 Estimated Salary",
            min_value=0.0,
            value=50000.0,
            step=1000.0,
            format="%.2f",
            key="estimated_salary",
        )

        num_of_products = st.slider(
            label="📦 Number of Products",
            min_value=1,
            max_value=4,
            value=2,
            key="num_products",
        )

        has_credit_card = st.toggle(
            label="💳 Has Credit Card",
            value=True,
            key="has_credit_card",
        )

        is_active_member = st.toggle(
            label="🟢 Active Member",
            value=True,
            key="active_member",
        )

    st.divider()

    # ======================================================
    # Predict Button
    # ======================================================

    predict_button = st.button(
        label="🔍 Predict Churn",
        use_container_width=True,
        type="primary",
    )

    # ======================================================
    # Customer Object
    # ======================================================

    customer = CustomerData(
        geography=geography,
        gender=gender,
        age=age,
        credit_score=credit_score,
        tenure=tenure,
        balance=balance,
        num_of_products=num_of_products,
        has_credit_card=int(has_credit_card),
        is_active_member=int(is_active_member),
        estimated_salary=estimated_salary,
    )

    return customer, predict_button