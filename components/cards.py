"""
==========================================================
Prediction Cards Component

Author  : Milind Chavan
Project : Customer Churn Analytics
Version : 2.0
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from config import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


# ==========================================================
# Prediction Cards
# ==========================================================

def render_prediction_cards(
    probability: float,
) -> None:
    """
    Display prediction summary cards.

    Parameters
    ----------
    probability : float
        Predicted probability of customer churn.
    """

    prediction = (
        "Likely to Churn"
        if probability >= 0.50
        else "Not Likely to Churn"
    )

    confidence = max(
        probability,
        1 - probability,
    )

    if probability < LOW_RISK_THRESHOLD:

        risk = "🟢 Low"

    elif probability < MEDIUM_RISK_THRESHOLD:

        risk = "🟡 Medium"

    else:

        risk = "🔴 High"

    st.subheader("📊 Prediction Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="Prediction",
            value=prediction,
        )

    with col2:

        st.metric(
            label="Probability",
            value=f"{probability:.2%}",
        )

    with col3:

        st.metric(
            label="Confidence",
            value=f"{confidence:.2%}",
        )

    with col4:

        st.metric(
            label="Risk Level",
            value=risk,
        )